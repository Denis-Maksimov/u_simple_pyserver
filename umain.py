import uhtml


if __name__ == "__main__":
    print("run")
    srv=uhtml.uhtml(8080)
    for i in range(35):
        srv.check()
        print(i,"seconds more later")
        pass
    print("Ok")










