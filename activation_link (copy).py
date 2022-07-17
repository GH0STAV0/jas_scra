import smtplib
import time
import imaplib
import email
import bs4
import re
from bs4 import BeautifulSoup
from faker import Faker
import datetime
import random
import string
import subprocess as sp
from urllib.parse import quote
imaplib._MAXLINE = 80000
def save_it(finall):
	with open('shift_url2','a') as f:
	        f.write(finall+"\n")
	        f.close()

activation=[]
	# conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	# gmail_user = 'king00binz@gmail.com'
	# gmail_pwd = 'agoon007'
def connection_imap():

	conn = imaplib.IMAP4_SSL("imap.zoho.com", 993)
	gmail_user = 'y05azere@zoho.com'
	gmail_pwd = 'agoon007A*'
	conn.login(gmail_user, gmail_pwd)
	return conn



def gather_acces(emmail):
	print("search for email :" +emmail)
	magic_formul='(TO "<xxxxx>" SUBJECT "Verify your email")'
	magic_formul=magic_formul.replace("xxxxx",emmail)
		# magic_formul='(SUBJECT "Verify your email address")'

	# magic_formul=magic_formul.replace("xxxxx",emmail)
	# magic_formul=magic_formul.encode("US-ASCII")
	mail=connection_imap()
	mail.select('INBOX')
	status, data = mail.search(None, magic_formul)
	# for num in data[0].split():
	# # Retrieve email message by ID
	# 	tmp, data = mail.fetch(num, '(RFC822)')
	# 	print('Message: {0}\n'.format(data[0][1]))
	# # 	break
	
	ids = data[0]
	print(status,data[0])
	unread_msg_nums = data[0].split()
	print (" [ ",len(unread_msg_nums)," ]",flush=True,end= " ")
	if len(unread_msg_nums) == 0 :
		print("NOTHING FOUND")
		mail.close()
		
		time.sleep(8)
		gather_acces(emmail)


	
	for emailid in unread_msg_nums:
		resp3, data3 = mail.uid("fetch", emailid,"(RFC822)" )#mail.uid('search', None, "ALL")
		result, data = mail.fetch(emailid, "(RFC822)")
		email_body = data[0][1].decode("utf-8")
		# print(data[0][1])
		za_body_mail = email.message_from_string(email_body)
		iii=za_body_mail.get_content_type()
		ohh=za_body_mail.get_payload()
		#charset = za_body_mail.get_content_charset()
		html0 = za_body_mail.get_payload()#, str(charset), "ignore"#.encode('utf8', 'replace')
		print(za_body_mail)
		input("")
		if za_body_mail.is_multipart():
			for part in za_body_mail.get_payload():
				print(part.get_content_type())
				if part.get_content_type() == 'text/plain' :
					# print(part.get_content_type())
					kkk=part.get_payload()
					payload=part.get_payload(decode=True).decode(part.get_content_charset('utf-8'))
					# print(payload)
					# print(kkk)
		else:
			print(za_body_mail.get_payload())
		# print(za_body_mail.get_payload()[0])
		# print(payload)
		# input("")
		# urls=re.findall(u'"(https.*?)"' , payload)
		urls = re.findall(r'http://|https://tr.*', payload)
		urlsw = re.findall(r'http://.*|https://.*', payload)
		if len(urlsw) == 0:
			print('the list is empty')
			activation=urls[2]
		else :
			activation=urlsw[2]
		# print(', '.join(urls))
		# input("")
		l_a = activation.split()
		print(l_a[0])
		mail.close()
	return l_a[0]

#gather_acces("alicia20epxlgoodman@biglose3.ml")
#print(link.get('href'))
#read_uniq()
#gather_acces("john21peolg6brown@multi-service-seller.tk")
# emmail="aaron387ifowler@dark-market-crypto.tk"
emmaily="james2MFburke@compis-ahay.cf"
gather_acces(emmaily)