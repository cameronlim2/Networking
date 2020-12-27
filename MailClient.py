from socket import *
import ssl
import base64

mailServer = 'smtp.csus.edu'
serverPort = 587

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, serverPort))
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != '220':
    print(' 220 reply not received from server.')

heloCommand = 'HELO Alice\r\n'
print("Sending First HELO")
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

print("Sending MAIL FROM")
mailFromCommand = 'MAIL FROM: cameron.lim351@gmail.com\r\n'
clientSocket.send(mailFromCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv[:3] != '250':
	print('250 reply not received from server.')

print("Sending RCPT TO command")
rcptToCommand = 'RCPT TO: cameron.lim351@gmail.com\r\n'
clientSocket.send(rcptToCommand)
recv1 = clientSocket.recv(1024) 
print recv1 
if recv1[:3] != '250':
	print '250 reply not received from server.'

print("Sending DATA Command")
dataCommand = 'DATA \r\n' 
clientSocket.send(dataCommand) 
recv1 = clientSocket.recv(1024)	
print recv1 
if recv1[:3] != '354':       
	print '354 reply not received from server.' 

print("Send Message DATA")
msg = "SUBJECT: SMPT Mail Test\n Test Mail: It worked!\n.\r\n"

clientSocket.send(msg)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print('250 reply not received from  server')

quitCommand = 'QUIT\r\n'
clientSocket.send('QUIT\r\n')
recv1 = clientSocket.recv(1024)	
print recv1 
if recv1[:3] != '221':       
	print '221 reply not received from server.' 