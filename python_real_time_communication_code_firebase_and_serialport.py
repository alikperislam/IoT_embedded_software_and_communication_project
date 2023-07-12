import serial.tools.list_ports
from firebase import firebase

# firebase bağlantı
myDB =firebase.FirebaseApplication("https://roomiotapp-default-rtdb.europe-west1.firebasedatabase.app/",None)
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



# ---------------------- firebase kütüphane notlar --------------------
# data save
"""data = {
    "fahren" : 1,
    "nem" : 2,
    "sicaklik" : 0,
    "tema" : 3,
    "isikveri" : 0
}
"""
#myDB.post('/Veriler/datas',data)
# data update
#myDB.put('/Veriler',"Fahren",32)



"""
veriler=paket.decode('utf').split('/')
isik=veriler[0]
h=veriler[1]
t=veriler[2]
f=veriler[3]
tema=veriler[4]
#-----------------

#myDB.put('/Veriler', "Fahrenheit", f)
myDB.put_async('/Veriler', "Nem", h)
myDB.put_async('/Veriler', "Sicaklik", t)
myDB.put_async('/Veriler', "Tema", tema)

# -----------------
print(isik)
print(h)
print(t)
print(h)
print(tema)
print("******************************")
"""
