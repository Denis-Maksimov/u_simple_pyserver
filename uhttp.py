import socket,usrv,io,re


class uhttp(usrv.userver):

    def __init__(self,port=8080) -> None:
        super().__init__("127.0.0.1",port)
        self.header=re.compile(R"(GET|POST)\s+\/([\S]{0,})\s+HTTP\/1.1")
        self.remeta=re.compile(R"^\s{0,}(\S+)\b\s{0,}:\s{0,}(.+)$")
        self.method=''
        self.url=''
        self.post=''
        self.meta = {}
        self.codes={
            200:b"200 OK",
            400:b"400 Bad Request",
            404:b"404 Not Found",
            418:b"418 I'm a teapot",
        }

    def __del__(self):
        """Destrructor"""
        print("del2 ok")

        pass
    def generate_html(self,conn:socket)->int:
        return "since I'm a teapot so I cannot brew coffee.. So sorry(("

    def send_code(self,conn:socket,code:int):
        if not self.codes[code]:
            code=418
        conn.send(b"HTTP/1.1 ")
        conn.send(self.codes[code])
        conn.send(b"\r\n\r\n")

    def handle_data(self,conn,data:str):
        err=200
        while True:
            buffer = io.StringIO(data)
            line=next(buffer,False)
            if not line:
                self.send_code(conn,400)
                break

            fubar=self.header.findall(line)
            self.method=fubar[0][0]
            self.url=fubar[0][1]

            while line:
                line=next(buffer,False)
                if line:
                    fubar=self.remeta.findall(line)
                    if fubar:
                        dict.update(self.meta,{fubar[0][0]:fubar[0][1]})
                    else:
                        self.post=buffer.read()
                        break
                else:
                    self.post=''
                pass
            
            print(self.post)
            if self.method != 'GET' and self.method != 'POST':
                self.send_code(conn,418) 
            break
        
        self.generate_html(conn)
        conn.close()
        self.inputs.remove(conn)
        self.outputs.remove(conn)


if __name__ == "__main__":
    print("run")
    srv=uhttp()
    for i in range(25):
        srv.check()
        pass
    print("Ok")

