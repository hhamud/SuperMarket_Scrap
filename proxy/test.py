import random


with open('proxy-list.txt', 'r') as f:
        listcomp = [i for i in f]
        x = random.choice(listcomp)
        base = 'http://'
        ports = x.split(":")[1]
        ip = x.split(":")[0]
        proxy = base + ip
        print(x)
        print(proxy)
        print(ports)



# with open('proxy-list.txt', 'r') as f:
#     for i in f:
#         base = 'http://'
#         ports = i.split(":")[1]
#         ip = i.split(":")[0]
#         proxy = base + ip
#         print(proxy)
#         print(ports)