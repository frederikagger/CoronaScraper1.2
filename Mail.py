import smtplib


def sendMail(body):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('frederikagger123@gmail.com', 'password')

        subject = 'Corona updates'
        msg = f'Subject: {subject},\n\n{body}'
        smtp.sendmail('frederikagger123@hotmail.com', 'frederikagger@hotmail.com', msg)
