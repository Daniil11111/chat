import socket
import threading
def l():
    while True:
        data = s.recv(2048).decode()
        print(data)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
te = input('ник > ')
s.bind(('',0))
s.sendto(f'{te} присоединился на сервер'.encode(),('192.168.3.36',12345))
l = threading.Thread(target=l)
l.start()
while 1:
    kl = input('')
    if kl == 'createroom':
        name = input('название сервера: ')
        maxx = input('введите максимальное количество игроков: ')
        on = input('смогут ли люди видеть ваш сервер: ')
        if on == 'y' or 'yes' or 'да':
            on = '1'
        else:
            on = '0'
        password = input('пароль от сервера: ')
        text = f'[{te}] cg {name} {maxx} {on} {password}'
        s.sendto(text.encode(), ('192.168.3.36', 12345))
    elif kl == 'join':
        namee = input('введите комнату: ')
        nam = input('введите пароль от комнаты: ')
        textt = f'[{te}] join {namee} {nam}'
        s.sendto(textt.encode(), ('192.168.3.36', 12345))
    s.sendto(f'[{te}] {kl}'.encode(),('192.168.3.36',12345))




