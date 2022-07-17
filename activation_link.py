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
activation_link=""
# nkedqpwtbrmnwtne

	# conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	# gmail_user = 'king00binz@gmail.com'
	# gmail_pwd = 'agoon007'
def connection_imap():
	conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
	gmail_user = 'binhunt3r@gmail.com'
	gmail_pwd = 'nkedqpwtbrmnwtne'

	# conn = imaplib.IMAP4_SSL("imap.zoho.com", 993)
	# gmail_user = 'y05azere@zoho.com'
	# gmail_pwd = 'agoon007A*'
	conn.login(gmail_user, gmail_pwd)
	return conn



def gather_acces(emmail):
	print("search for email :" ,emmail)
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
	# print(status,data[0])
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
		contenet_type=za_body_mail.get_content_type()
		ohh=za_body_mail.get_payload()
		#charset = za_body_mail.get_content_charset()
		html0 = za_body_mail.get_payload()#, str(charset), "ignore"#.encode('utf8', 'replace')
		# print(za_body_mail)

		
		global activation_link
		if "html" in str(contenet_type):
			html_=za_body_mail.get_payload()
			soup=BeautifulSoup(html_,"html.parser")
			APTag = soup.findAll('a')
			for tag in APTag:
				wh_link=tag.get_text()
				# print(wh_link)
				if "hash?hash=3D" in wh_link :
					urls = re.findall(r'hash=3D(.*?)&source', wh_link)
					print(urls)
					# print(wh_link,"ooooooooooooooooooooooooooooooooo")
					monn="https://www.livejasmin.com/en/email-validate-hash?hash=zzzzz&source=signup"
					monn=monn.replace("zzzzz",urls[0])
					activation_link=monn
					
				elif "hash?hash=" in wh_link :
					print(wh_link)
					# global activation_link
					activation_link=wh_link
					
			
		else:
			print(za_body_mail.get_payload())



		# monn="https://www.livejasmin.com/en/email-validate-hash?hash=zzzzz&source=signup"
		# monn=monn.replace("zzzzz",activation_link)
		# 
		# l_a = monn
		# print(activation_link)
		mail.close()
		# input("")
	return activation_link

#gather_acces("alicia20epxlgoodman@biglose3.ml")
#print(link.get('href'))
#read_uniq()
#gather_acces("john21peolg6brown@multi-service-seller.tk")
# emmail="aaron387ifowler@dark-market-crypto.tk"
# emmaily="joshua36Hqgarcia@the-witcher.gq"
# # emmaily="cheryl56uPsmith@the-witcher.gq"
# gather_acces(emmaily)
# print(activation_link)