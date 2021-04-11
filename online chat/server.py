import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.3.36',12345))
group1={}
name = {}
max = {}
block = {}
password = {}
while 1:
        try:
                data,ip = s.recvfrom(2048)
                if data.decode().split()[1] == 'cg':
                        group1[data.decode().split()[2]] = []
                        grrrr = data.decode().split()[2]
                        cc = len(group1[data.decode().split()[2]])
                        max[grrrr] = data.decode().split()[3]
                        block[grrrr] = data.decode().split()[4]
                        password[grrrr] = data.decode().split()[5]
                elif data.decode().split()[1] == 'join':
                    namee = data.decode().split()[2]
                    if data.decode().split()[3] == password.get(namee):
                        if len(group1[namee]) <= int(max.get(namee)) - 1:
                            if ip not in group1[namee]:
                                group1[namee].append(ip)
                                name[ip]=namee
                        else:
                            s.sendto(f'комната {namee} заполнена'.encode(),ip)
                    else:
                        s.sendto(f'пароль от комнаты {namee} неверен'.encode(), ip)
                if data.decode().split()[1] == 'list':
                    for i in group1.keys():
                        if block.get(i) == '1':
                            s.sendto(f'{i}  -  {len(group1.get(i))}|{max.get(i)}'.encode(), ip)
                            if ip in group1.get(i):
                                group1[i].remove(ip)
                for iii in name.keys():
                    print(iii)
                    if ip == iii:
                        print(name.get(iii))
                        for iiii in name.keys():
                                if name.get(iii) == name.get(iiii):
                                    if iiii != ip:
                                        s.sendto(data,iiii)
        except:
                pass