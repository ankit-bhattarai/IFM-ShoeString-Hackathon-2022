"""File used to send email warnings"""
import smtplib #importing the module


def send_email(sender_add, password, receiver_add, machine, message):

     #creating the SMTP server object by giving SMPT server address and port number
    smtp_server=smtplib.SMTP("smtp.gmail.com",587)
    smtp_server.ehlo() #setting the ESMTP protocol
    smtp_server.starttls() #setting up to TLS connection
    smtp_server.ehlo() #calling the ehlo() again as encryption happens on calling startttls()
    smtp_server.login(sender_add,password) #logging into out email id
    msg_to_be_sent ="""
    Subject:Warning Machine {} On!
    {}""".format(machine, message)
    new_msg = """From: ABC
To: XYZ
MIME-Version: 1.0
Content-type: text/html
Subject:Warning Machine {} ON!
Hello! <br/><p align="center"> Machine {} ON! Please check it ASAP!</p><hr/>""".format(machine, machine)
    #sending the mail by specifying the from and to address and the message 
    smtp_server.sendmail(sender_add,receiver_add, new_msg)
    print('Successfully the mail is sent') #priting a message on sending the mail
    smtp_server.quit()#terminating the server
