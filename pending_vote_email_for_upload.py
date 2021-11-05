import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def outlook_mail():
    from_address = 'automation-team@xyz.com'

    votes_mapping = [
        ['abc', '35'],
        ['def', '43'],

    ]



    for vote in votes_mapping:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        login = vote[0]+'@amazon.com'
        pending = vote[1]

        cc = ['mno@amazon.com', 'pqe@amazon.com', 'mnr@amazon.com']
        cc_list = ','.join(cc)

        print(vote)

        message = 'To: {}\n' \
                  'Cc: {}\n' \
                  'Subject:RISE !! Reminder for voting\n\n' \
                  'Hello Reviewer,\n\n' \
                  'There are {} nomination pending in your queue for voting, requesting you to cast your votes before EO Monday (6th Sep 2021).\n\n' \
                  'Regards, Team RISE !!' \
                  ''.format(login,cc_list, pending)

        try:
            smtpObj = smtplib.SMTP('sample.xyz.com: 99')
            smtpObj.sendmail(from_address, login, message)
            print(login, 'mail successfully sent')
        except smtplib.SMTPException as ex:
            print(ex)
            print(login, 'Problem in sending mail')

if __name__ == '__main__':
    outlook_mail()