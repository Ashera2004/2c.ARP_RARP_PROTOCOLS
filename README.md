# 2c.SIMULATING ARP /RARP PROTOCOLS

## AIM

To write a python program for simulating ARP protocols using TCP.

## ALGORITHM:

## Client:

1. Start the program
2. Using socket connection is established between client and server.
3. Get the IP address to be converted into MAC address.
4. Send this IP address to server.
5. Server returns the MAC address to client.
   
## Server:

1. Start the program
2. Accept the socket which is created by the client.
3. Server maintains the table in which IP and corresponding MAC addresses are
stored.
4. Read the IP address which is send by the client.
5. Map the IP address with its MAC address and return the MAC address to client.

## PROGRAM - ARP

![image](https://github.com/Ashera2004/2c.ARP_RARP_PROTOCOLS/blob/main/Ex_2c_Python%20Code.png)

## OUPUT - ARP

![image](https://github.com/Ashera2004/2c.ARP_RARP_PROTOCOLS/blob/main/Ex_2c_Command%20Prompt.png)

## RESULT
Thus, the python program for simulating ARP protocols using TCP was successfully 
executed.
