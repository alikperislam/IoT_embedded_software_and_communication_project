import serial.tools.list_ports
from firebase import firebase

# firebase bağlantı
myDB =firebase.FirebaseApplication("your_firebase_app_url",None)
#print(myDB)

# tanımlamalar
veriler=[]
isik=0
h=0
t=0
f=0
tema=True
#
ports = serial.tools.list_ports.comports()
serialStart = serial.Serial()
#
portlist=[]
for port in ports:
    portlist.append(str(port))
    print(str(port))
secili_port = "COM3"
#
serialStart.baudrate=9600
serialStart.port=secili_port
serialStart.open()
#
try:
    while True:
        if serialStart.in_waiting:
            paket = serialStart.readline()
            myDB.put('/Veriler', "veri", paket.decode('utf'))
except:
    print("bağlanti koptu...")

