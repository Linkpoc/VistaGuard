import socket, time

def socket_port_normal(ip):
    list = [21, 22, 80, 81, 88, 443, 1080, 1433, 1521, 3306, 3389, 5000, 6379, 7001, 8080, 8081, 8088, 8888, 27017, 50636]
    for port in list:
        try:
            s = socket.socket()
            s.settimeout(1)  # 设置无法连接情况下超时时间，提升扫描效率
            s.connect((ip, port))
            print(f"端口: {port} 可用.")
            s.close()
        except:
            pass
        time.sleep(1)  # 设置休眠时间


if __name__ == '__main__':
    socket_port_normal('127.0.0.1')  # 固定端口扫描
