#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys , subprocess , os ,requests,string,random,datetime
from faker import Faker

# from browser_ import *
# import smtplib compis-ahay.cf 

proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050',}
domains=["@compis-ahay.cf","@n0xi-bl00m.cf","@n0xi.tk","@the-witcher.gq"]
reasonableCharacters = (string.digits + string.ascii_letters )



def password0(minimum=10, maximum=14):
    return ''.join(
        random.choice(reasonableCharacters) for x in range(
            random.randint(minimum, maximum)
        )
    )






def generate_name_add():
	geo_info=[]

	while True:

		fake_a = Faker('en_US')
		adrees_com=fake_a.address()
		street_add=	adrees_com.split("\n")
		street0=street_add[0]
		date_if_birth=fake_a.date_time_between(start_date="-40y",end_date="-20y")
		date_if_birth=date_if_birth.date()
		date_if_birth=date_if_birth.strftime('%d-%m-%Y')

		if "," in street_add[1]:
			city_a=street_add[1].split(",")
			city_=city_a[0]
			zop=city_a[1].split()
			country=zop[0]
			zip00=zop[1]
			break
	while True:
  		fake = Faker('en_US')
  		name_j=fake.name().lower()
  		name2_j=name_j.replace(" ","")
  		timestamp = datetime.datetime.now()
  		vary=password0(2,2)
  		#vva2=random.choice(reasonableCharacters) 
  		t =  str(timestamp.second)+vary
  		email_ja=name_j.replace(" ",t)
  		if len(email_ja) <= 16:
  			#print(t)
  			dom=random.randint(1,len(domains))
  			user_do=email_ja
  			password_do=password0(8,12)
  			real_name=name_j.lower()
  			email_do=email_ja+domains[dom-1]
  			geo_info.append(email_do)
  			geo_info.append(password_do)
  			geo_info.append(real_name)
  			geo_info.append(date_if_birth)
  			geo_info.append(zip00)
  			geo_info.append(user_do)
  			geo_info.append(street0)
  			geo_info.append(city_)
  			geo_info.append(country)
  			#geo_info.append(city_)
  			#geo_info.append(country)
  			#geo_info.append(zip00)
  			#print(geo_info)
  			# print(geo_info)
  			#return user_do,password_do,email_do,real_name,street0,city_,country,zip00  			
  			return geo_info
  			break

  		else :
  			continue
generate_name_add()