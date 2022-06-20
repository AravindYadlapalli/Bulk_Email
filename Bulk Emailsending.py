import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'Hello': 'hello123@gmail.com',
    '1D': 'onedirection@gmail.com',
    'Zayn': 'zaynmalik786@gmail.com',
    'Harry': 'harrystyles@google.com',
    'Gigi': 'gigihadid@gmail.com'
}


def get_email_info():
    talk('To Whom you wanna send this email:')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject for your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey User. Your email is sent')
    talk('Do you want to send more emails?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
