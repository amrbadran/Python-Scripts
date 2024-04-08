import smtplib
from Config import *


class EmailSender:

    def __init__(self, email_dest, subject, msg):
        self.emailDest = email_dest
        self.subject = subject
        self.msg = msg

    def send_email(self):
        conn = self.__conf_email()
        conn.sendmail(Config.EMAIL, self.emailDest,
                      "Subject: " + self.subject + "\n\n" + self.msg
                      )
        conn.quit()
        print("You Have Sent the msg to an email : " + self.emailDest)
    def __conf_email(self):
        conn = smtplib.SMTP('smtp.office365.com', 587)
        conn.ehlo()
        conn.starttls()
        conn.login(Config.EMAIL, Config.PASSWORD)

        return conn
