from EmailSender import *


class Main:
    def __init__(self):
        your_email = input("Enter Your Email (outlook) : ")
        your_password = input("Enter Your Password : ")
        email = input("please enter the email you want to send a msg : ")
        subject = input("please enter the subject : ")
        msg = input("please enter the msg : ")
        Config(your_email, your_password)
        EmailSender(email, subject, msg).send_email()


if __name__ == "__main__":
    Main()
