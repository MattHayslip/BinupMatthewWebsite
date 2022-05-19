from flask import jsonify
import smtplib
import ssl
from email.message import EmailMessage

class emailController:
    def __init__(self):
        self.message = EmailMessage() 

    # set where the email is being sent from
    def setSender(self, sender):
        self.sender = sender

    # set who's receiving
    def setRecepient(self, recipient):
        self.recipient = recipient

    # set the subject of said email
    def setSubject(self, subject):
        self.subject = subject

    # set message to send
    def setMessage(self, message):
        self.message = message

    # security 
    def setCsrfToken(self, token):
        self.token = token

    # sending html document with information
    def attachHtmlDocument(self, documentName):
        self.message.add_alternative(documentName,subtype="html")

    # setting the username for the email
    def setUSR(self, USR):
        self.USR = USR

    # setting the password for the email
    def setPSW(self, PSW):
        self.PSW = PSW

    # * sending the message.
    def send(self):
        try:
            context = ssl.create_default_context() # security

            self.message['From']    = self.sender
            self.message['To']      = self.recipient
            self.message['Subject'] = self.subject

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(
                    self.USR, 
                    self.PSW
                )
                if server.sendmail(self.sender,self.recipient, self.message.as_string()):
                    return True
                    
                else:
                    return False

        except Exception as e:
            # log("send-e-main", str(e))
            return jsonify(
                {
                    "error": str(e)
                }
            )
