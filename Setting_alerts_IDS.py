import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'alerts@yourdomain.com'
    msg['To'] = 'security@yourdomain.com'

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()