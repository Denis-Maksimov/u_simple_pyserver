import socket, select
import io    



class userver:
    """docstring"""
 
    def recurse_bind(self,host, port):
        try:
            self.srv_sock.bind((host, port))
            print("port",port)
        except:
            self.recurse_bind(host, port+1)
            
        pass
    
    def __init__(self,host,port):
        """Constructor"""
        self.srv_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.recurse_bind(host, port)
        self.srv_sock.listen(3)

        self.inputs = [self.srv_sock]  # сокеты, которые будем читать
        self.outputs = []  # сокеты, в которые надо писать
        self.messages ={} # здесь будем хранить сообщения для сокетов
        self.timeout=1.
        pass
    
    def __del__(self):
        """Destrructor"""
        self.srv_sock.close()
        for i in self.inputs:
            i.close()
        for i in self.outputs:
            i.close()
        pass

    def set_timeout(self,seconds:float):
        self.timeout=seconds
        
    def handle_data(self,conn,data:str):
        buffer = io.StringIO(data)
        line=next(buffer)

        conn.send(b"HTTP/1.1 200 OK\r\n")
        conn.send(b"\r\nBeee")
        self.inputs.remove(conn)
        self.outputs.remove(conn)
        conn.close()
        pass

    def read_handle(self,conn):
     
        data = conn.recv(1024)
        if data:
            # если сокет прочитался и есть сообщение 
            # то кладем сообщение в словарь, где 
            # ключом будет сокет клиента
            if self.messages.get(conn, None):
                self.messages[conn].append(data)
            else:
                self.messages[conn] = [data]

            # добавляем соединение клиента в очередь 
            # на готовность к приему сообщений от сервера
            if conn not in self.outputs:
                self.outputs.append(conn)
        else:
            print('Клиент отключился...')
            # если сообщений нет, то клиент
            # закрыл соединение или отвалился 
            # удаляем его сокет из всех очередей
            if conn in self.outputs:
                self.outputs.remove(conn)
            self.inputs.remove(conn)
            # закрываем сокет как положено, тем 
            # самым очищаем используемые ресурсы
            conn.close()
            # удаляем сообщения для данного сокета
            del self.messages[conn]
        pass

    def accept_handle(self,conn):
        # если это серверный сокет, то пришел новый
        # клиент, принимаем подключение
        new_conn, client_addr = conn.accept()
        print('Успешное подключение!')
        print(client_addr)
        # устанавливаем неблокирующий сокет
        # поместим новый сокет в очередь 
        # на прослушивание
        self.inputs.append(new_conn)
        pass


    def write_handle(self,conn):
        msg = self.messages.get(conn, None)
        if len(msg):
            # если есть сообщения - то переводим 
            # его в верхний регистр и отсылаем
            temp = msg.pop(0).decode('utf-8')
            # print(temp)
            self.handle_data(conn,temp)
            

        else:
            # если нет сообщений - удаляем из очереди
            # сокетов, готовых принять сообщение 
            self.outputs.remove(conn)
        pass


    def check(self):
    
        reads, send, excepts = select.select(self.inputs, self.outputs, self.inputs,self.timeout)

        # Далее проверяются эти списки, и принимаются 
        # решения в зависимости от назначения списка

        # список READS - сокеты, готовые к чтению
        for conn in reads:
            if conn == self.srv_sock:
                # если это серверный сокет, то пришел новый
                # клиент, принимаем подключение
                self.accept_handle(conn)
                pass
            else:
                # если это НЕ серверный сокет, то 
                # клиент хочет что-то сказать
                self.read_handle(conn)

        # список SEND - сокеты, готовые принять сообщение
        for conn in send:
            # выбираем из словаря сообщения
            # для данного сокета
            self.write_handle(conn)
            pass

        # список EXCEPTS - сокеты, в которых произошла ошибка
        for conn in excepts:
            print('Клиент отвалился...')
            # удаляем сокет с ошибкой из всех очередей
            self.inputs.remove(conn)
            if conn in self.outputs:
                self.outputs.remove(conn)
            # закрываем сокет как положено, тем 
            # самым очищаем используемые ресурсы
            conn.close()
            # удаляем сообщения для данного сокета
            del self.messages[conn]
            pass


if __name__ == "__main__":
    print("run")
    srv=userver("127.0.0.1",8080)
    for i in range(25):
        srv.check_v2()
    print("Ok")












