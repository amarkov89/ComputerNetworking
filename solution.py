from socket import *


def smtp_client (port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond Gradescope
    #mailserver = ("smtp.nyu.edu", 25)
    #Create socket called clientSocket and establish a TCP connection with mailserver and port
    #Fill in start
    clientSocket = socket (AF_INET, SOCK_STREAM)
    port, mailserver = clientSocket.connect()
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print (recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send Mail From command and print server response.
    #Fill in start
    MAILFROM = "MAIL FROM: <student@nyu.edu> \r\n"
    clientSocket.send(MAILFROM.encode())
    recv2 = clientSocket.recv(1024)
    #print("Server response to mail from command: " + recv2)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')
    #Fill in end

    #Send RCPT TO command and print server response.
    #Fill in start
    RCPTTO = "RCPT TO: <am6131@nyu.edu> \r\n"
    clientSocket.send(RCPTTO.encode())
    recv3 = clientSocket.recv(1024)
    #print("Server respone to Rcpt To Command: " + recv3)
    #if recv1[:3] != '250':
        #print("250 reply not received from server.")
    #Fill in end

    #Send DATA command and print server response.
    #Fill in start
    DATA = "DATA\r\n"
    clientSocket.send(DATA.encode())
    recv4 = clientSocket.recv(1024)
    #print("Server response to DATA command: " + recv4)
    #if recv1[:3] != '250':
        #print("250 reply not received from server.")
    #Fill in end

    #Send message data
    # Fill in start
    SUBJECT = "SUBJECT: SMTP TEST \r\n\r\n"
    clientSocket.send(SUBJECT.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recvMsg = clientSocket.recv(1024)
    #print("Message data response: " + recvMsg.decode())
    #if recv1[:3] != '250':
        #print("250 reply not received from server.")
    #Fill in end

    #Message end with a single period.
    #Fill in start

    #Fill in end

    #Send QUIT command and get server response.
    #Fill in start
    clientSocket.send("QUIT\r\n".encode())
    message = clientSocket.recv(1024)
#print(message)
    clientSocket.close()
    sys.exit()
#Fill in end

if __name__ == '__main__':
    smtp_client(1025,'127.0.0.1')
