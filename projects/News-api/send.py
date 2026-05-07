import smtplib,ssl 

def send(msg):
    host="smtp.gmail.com"
    port=465

    username="sudhakarpappu123@gmail.com"
    password="kayzaggbgumuksek"

    receiver="sudhann04@gmail.com"
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as s:
        s.login(username,password)
        s.sendmail(username,receiver,msg)