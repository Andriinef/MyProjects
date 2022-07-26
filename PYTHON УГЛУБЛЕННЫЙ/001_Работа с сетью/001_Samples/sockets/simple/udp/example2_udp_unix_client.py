# udp client
import socket

# создаем UNIX UDP-сокет
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
# отправляем данные на UNIX-сокет- файл `unix.sock`
sock.sendto(b'A_Draft Message', 'unix.sock')
