import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'suraj.jha'
email['to'] = 'rsurajjha@gmail.com'
email['subject'] = 'you won 1111 rs!'

email.set_content('i am python master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('test@gmail.com','pass@123')
    smtp.send_message(email)

    print('all good boss!')