import smtplib
import imghdr
from email.message import EmailMessage 


username="sudhakarpappu123@gmail.com"
password="kayzaggbgumuksek"
def send_mail(img):
    host="smtp.gmail.com"
    port=465
    email_msg=EmailMessage()
    email_msg["Subject"]="New body found"
    email_msg.set_content("hey hello")

    with open(img,"rb") as file:
        cont=file.read()
    email_msg.add_attachment(cont,maintype='image',subtype=imghdr.what(None ,cont))

    gmail=smtplib.SMTP(host,587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username,password)
    gmail.sendmail(username,username,email_msg.as_string())
    gmail.quit()

if __name__=="__main__":
    send_mail(img="images/1.png")