#Name: A S Siddarth
#Reg No. 212224040316
import socket 
s=socket.socket() 
s.connect(('localhost',8000)) 
while True:
      ip=input("Enter logical Address : ") 
      s.send(ip.encode()) 
      print("MAC Address",s.recv(1024).decode())
