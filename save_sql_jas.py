import mysql.connector
import time ,os
from datetime import datetime


host="remotemysql.com"
user="f6V3kVwxvH"
passwd="sOVnW1130i"
database="f6V3kVwxvH"





###################################### SAVE JASMIN DB : jasmin_db #################################################


def insert_to_db(jsm_user,jsm_email):
	# mydb = mysql.connector.connect(host="sql8.freesqldatabase.com",user="sql8505358",passwd="ILiAHKV4bs",database="sql8505358")
	mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")

	mycursor = mydb.cursor()
	sql = "INSERT INTO jasmin_db (jsm_user, jsm_pass, jsm_email,jsm_acc_status) VALUES (%s, %s, %s, %s)"
	val = (jsm_user, "baba123A*",jsm_email,"NA")
	mycursor.execute(sql, val)
	time.sleep(2)
	print("Saved to Database : [ jasmin_db ]",jsm_user)

	mydb.commit()

##############################################################################################




###############################
# host_sql="db4free.net"
# user="test_db4freex01"
# passwd="SkPsU4PrbQEH!DJ"
# database="test_db4freex01"
############################

# insert_to_db("henry19RRcruz","henry19RRcruz@compis-ahay.cf")