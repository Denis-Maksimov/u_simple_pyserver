import uhttp,re,json

class uhtml(uhttp.uhttp):
    def __init__(self,port=8080) -> None:
        super().__init__(port)

        
        self.params={}
        # self.local_params=[]
        #remap index to file
        self.file_pages={
            "index":["test.html",200],
            "style.css":["style.css",200],
            "script.js":["script.js",200],
            "404":["test.html",404],
            "418":["test.html",418],
        }
        self.gen_pages={
            "params.json":[self.parsm,200],
            "set_params":[self.setparsm,200],
        }
        
        self.regex=re.compile(R"(\S+)=(\S+)")

    def parsm(self,conn):
        line=json.dumps(self.params)
        conn.send(line.encode())
        pass

    def setparsm(self,conn):

        line=json.loads(self.post)
        for p in line:
            self.params.update({p:line[p]})
        # conn.send(line.encode())
        pass

    def set_param(self,param,value:list):
        self.params[param]=value
        pass

    def get_param(self,param)->list:
        try:
            return self.params[param]
        except:
            return False

        

    def send_file(self,conn,file):
        with open(file) as file_handler:
            for line in file_handler:
                conn.send(line.encode())

    def parse_url(self):
        s=self.url
        ur=s.split("?",1)
        if ur.__len__()>=2:
            for math in ur[1].split("&"):
                a=self.regex.findall(math)
                try:
                    self.params.update({a[0][0]:a[0][1].split("+")})
                except:
                    pass
        print(ur[0])
        return ur[0]


    def check_url(self,conn,parsed_url):
        try:
            if parsed_url in self.file_pages:
                foo=self.file_pages[parsed_url]
                self.send_code(conn,foo[1])
                self.send_file(conn,foo[0])
            elif parsed_url in self.gen_pages:
                foo=self.gen_pages[parsed_url]
                self.send_code(conn,foo[1])
                foo[0](conn)
            else:
                self.check_url(conn,"404")
        except KeyError:
            self.check_url(conn,"404")

    def generate_html(self,conn)->None:

        print(self.url)
        self.check_url(conn, self.parse_url())            
        return


if __name__ == "__main__":
    print("run")
    srv=uhtml(8080)
    srv.set_param("name",['false'])
    srv.set_param("fubar",['123.0','1645'])
    srv.set_param("fuck",['123.0','1645'])
    for i in range(35):
        srv.check()
        # print(i,"seconds more later")
        # print(srv.get_param("name"))
        print( json.dumps(srv.params))
        pass
    print("Ok")
