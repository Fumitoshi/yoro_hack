# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:40:17 2017

@author: fumitoshi
"""

import bluetooth
import json
import requests

gyro_th = 0.3
acc_th = 0.2
pas_th = 0.5
num = 6
send_msg = "P"
def to_float(a):
    a = [float(i) for i in a]
    return a
def get_personality(gyro,pas,acc):
    pas_max = pas
    acc_avg = acc
    gyro_var = gyro
    if pas_max >pas_th:
        pas_ans = "H"
    else:
        pas_ans = "L"
    if acc_avg >acc_th:
        acc_ans = "H"
    else:
        acc_ans = "L"
    if gyro_var >gyro_th:
        gyro_ans = "H"
    else:
        gyro_ans = "L"
    data = gyro_ans+acc_ans+pas_ans
    if data == "HHH":
        return 1
    elif data == "HHL":
        return 2
    elif data == "HLH":
        return 3
    elif data == "HLL":
        return 4
    elif data == "LHH":
        return 5
    elif data == "LHL":
        return 6
    elif data == "LLH":
        return 7
    elif data == "LLL":
        return 8




# start the program
# set first bluttooth address

bd_addr1 = '00:06:66:6e:32:b9'
bd_addr2 = '00:06:66:72:69:56'
port = 1

sock1 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock2 = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock1.connect((bd_addr1,port))
print("connect 1")
sock2.connect((bd_addr2,port))
print("connect2")
print("OK now connectiong...")
#data = sock.recv(1024)
#dataReadable = data.decode('utf-8')
# sock.send("please")
gyro1 = []
acc1 = []
pas1 = []
hantei = []
aaa = []
sock1.send(send_msg)
while 1:
    data1 = sock1.recv(2048)
    data1 = data1.decode('utf-8')
    hantei = data1.split()
    aaa = hantei + aaa
    if "F" in aaa:
        aaa = aaa[0:aaa.index("F")]
        break
print(aaa)
gyro1 = aaa[-3]
acc1 = aaa[-2]
pas1 = aaa[-1]


gyro2 = []
acc2 = []
pas2 = []
hantei = []
aaa = []
sock2.send(send_msg)
while 1:
    data2 = sock2.recv(2048)
    data2 = data2.decode('utf-8')
    hantei = data2.split()
    aaa = hantei + aaa
    if "F" in aaa:
        aaa = aaa[0:aaa.index("F")]
        break
print(aaa)
gyro2 = aaa[-3]
acc2 = aaa[-2]
pas2 = aaa[-1]

# print each data
print("id: 1")
print(gyro1)
print("=========================")
print(acc1)
print("========================")
print(pas1)
print("id: 2")
print(gyro2)
print("=========================")
print(acc2)
print("=========================")
print(pas2)

sock1.close()
sock2.close()

# str to float
pas1 = float(pas1)
acc1 = float(acc1)
gyro1 = float(gyro1)

pas2 = float(pas2)
acc2 = float(acc2)
gyro2 = float(gyro2)


# make personaldata variables
pdata = []
#pdata.append(get_personality(gyro1,pas1,acc1))
#pdata.append(get_personality(gyro2,pas2,acc2))
pdata.append(5)
pdata.append(2)
pdata.append(3)
pdata.append(7)
pdata.append(2)
pdata.append(8)

json_data =[]
name = ["A","B","C","D","E","F"]
data = []
for i in range(num):
    data.append({"name":name[i],
                "type":pdata[i]})
#     json_data.append({
#             "id": name[i],
#             "type": pdata[i]
#             })
# f = open("D:/yoro_hack/asset/json/data.json","w")
# json.dump(json_data,f,sort_keys=True)
# f.close()
req_post = requests.post("http://localhots:3000/post_request",data = data)
