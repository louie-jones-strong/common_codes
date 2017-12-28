#import email
from smtplib import SMTP

server = SMTP('localhost')
server.sendmail("red.pig.guild@gmail.com", "louiej-s@hotmail.co.uk", "test")
server.quit()