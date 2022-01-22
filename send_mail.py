import smtplib
import ssl
from email.message import EmailMessage
import time
from colorama import Fore
import sys
import os

os.system('cls')

question = input('Do you want to send email [YES/NO] >> ')

while question == '':
    os.system('cls')
    print('Invalid choice!')
    print("")
    question = input('Do you want to send email [YES/NO] >> ')

if question == 'NO':
    print('Exiting...')
    time.sleep(1)
    sys.exit()
elif question == 'YES':
    os.system('cls')
    subject = input('Enter your subject >> ')
    print("")
    body = input('Enter your body >> ')
    print("")
    sender_email = input('Enter your email >> ')
    print("")
    receiver_email = input('Enter receiver email >> ')

    print("")
    password = input(f"Enter password for {sender_email} >> ")
    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
            <br><br>
            <hr>
            <center><p1>This message is send by <a href="mailto:{sender_email}">{sender_email}</a></p1></center>
            <br>
            <center><p>Copyright Giuseppe (c)</p></center>
            <br>
            <center><p2>Made By <a href="mailto:giuseppealehandro@gmail.com">giuseppealehandro@gmail.com</a></p2></center>
        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")

    context = ssl.create_default_context()
    os.system('cls')
    print('Please dont close this program, while sending email!')
    print("")
    print("Sending Email ...")
    print("")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        print('Loggining to server ...')
        time.sleep(2)
        server.login(sender_email, password)
        print("")
        print('Login succesfully')
        print("")
        server.sendmail(sender_email, receiver_email, message.as_string())

    print(f'{Fore.LIGHTGREEN_EX}')
    print(f"Email has been successfully sended to {receiver_email}!")
    print("")   
    print(f'From    : {sender_email}')
    print("")
    print(f"To      : {receiver_email}")
    print("")
    print(f"Subject : {subject}")
    print("")
    print(f"Body    : {body}")