import random,datetime,string , os ,time ,subprocess , sys , requests ,re ,emoji , json ,io
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pydub import AudioSegment
import speech_recognition as sr
import drive_chrome

import cnf_add
import username_gen
import activation_link
import tor_pro
import mod_vpn2
import save_sql_jas
# import mod_vpn2
# import drive_md
# import t00l

import config_set

urls_BVB="https://www.livejasmin.com/en/auth/sign-up"
user_agent = cnf_add.user_agent
sz=''

mmsg=["hi","hey","hey bb","HI","Hi","how are you", "wow", "so pretty ","hellow","heyyyy"]
def end_proc(driver):

	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass
	try:
		print("Close Display ...... ",end='')
		display.stop()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except:
		pass
	try:
		print("Clean LOGS ...... ",end='')
		os.system('rm /var/log/openvpn/openvpn.log')
		os.system('rm test1.wav ipifo.json')
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i chromedriver | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		exit(0)
	except:
		pass

def stage_1():
	try:
		sys_use_agent=re.findall('\(.*?\)',user_agent)[0]
		
	except Exception as e:
		sys_use_agent="eereee"




	try:
		#print (urls_BVB)
		os.system("rm -rf /tmp/.* > /dev/null 2>&1")
		# os.system("rm l05_00 ") 
		# os.system("clear && sleep 1")
		global sz
		width ,height=cnf_add.resolution_func()
		sz=height+","+width
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+urls_BVB+' :check_mark_button: :alien:'))
		print("System     : "+sys_use_agent)
		print("Resolution : "+sz)
		print ( "-------------------------------------------------------")

	except Exception as error:
		print (str(error))






def browser_op(driver):
	print ( "-------------------------------------------------------")
	user_arr_info=username_gen.generate_name_add()
	mod_vpn2.fnc_vpn ()
	driver.get(urls_BVB)
	try:
		print("Click Cookies ..... ", end='')
		Accept_Cookies=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-container"]/main/div[2]/div[1]/button[1]')))
		Accept_Cookies.click()
		print('[ ok ]')
	except Exception as e:
		print('browser_op error')
		exit(0)

	try:
		print("Fill Details ..... ", end='')
		username=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'username')))
		username.click()
		username.send_keys(user_arr_info[5],Keys.TAB,"baba123A*",Keys.TAB,user_arr_info[0])
		time.sleep(2)
		signup_submit=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'signup_submit')))
		signup_submit.click()
		# input('toggle_sidebar_button')
		try:
			signup_submit=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'toggle_sidebar_button')))
			print('Successful Sing-Up')
		except Exception as e:
			print(str(e))



		# print('[ ok ]')
		print(user_arr_info[5])
		print(user_arr_info[0])
	except Exception as e:
		print('browser_op error')
	print ( "-------------------------------------------------------")
	emmaily=user_arr_info[0]
	# print(emmaily)
	time.sleep(7)
	try:
		svg_allert=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.svgicon.svgicon-alert')))
		print('NOT ACTIVATED')
		link_activ=activation_link.gather_acces(emmaily)
		driver.get(link_activ)
		check_activation_sql(user_arr_info)
		time.sleep(3)
		exit(0)
		# get_offer(driver)
		# input('gjhgjh')

	except Exception as e:
		print('noononoonon')

	# svgicon svgicon-alert
	
	# print(link_activ)
	# insert_to_db(jsm_user,jsm_email)
	
	
	
	


def check_activation_sql(log_use):
	jsm_user=log_use[5]
	jsm_email=log_use[0]
	save_sql_jas.insert_to_db(jsm_user,jsm_email)

def get_offer(driver):
	# driver.refresh()
	# driver.get("https://livejasmin.com/en/free/purchase/credit-card#!payment/header")
	# https://www.livejasmin.com/en/free/chat-html5/AdelDarling
	driver.get("https://www.livejasmin.com/en/free/chat-html5/AdelDarling")
	# driver.get("https://www.livejasmin.com/en/free/chat-html5/KittyDivinita")
	# //*[@id="applet_container"]/div/div[3]/div[1]/div[2]/input[2]  https://www.livejasmin.com/en/free/chat-html5/AdelDarling
	try:

		random_msg=random.choice(mmsg)
		chat_input=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="applet_container"]/div/div[3]/div[1]/div[2]/input[2]')))
		print(random_msg)
		chat_input.click()
		chat_input_2=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="applet_container"]/div/div[3]/div[1]/div[2]/input[2]')))

		# //*[@id="applet_container"]/div/div[3]/div[1]/div[2]/input[2]
		chat_input_2.send_keys(random_msg,Keys.ENTER)
		input('2222222')
		end_proc(driver)
	except Exception as e:
		print('NOT ONLINE ...',e)

	input('2222222')
	exit(0)
	# //*[@id="firstbill"]/div/div[1]/div[1]/button
	close_button=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="firstbill"]/div/div[1]/div[1]/button')))
	close_button.click()
	time.sleep(3)
	get_free_button=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="firstbill"]/div[1]/div[2]/div/input')))
	get_free_button.click()
	time.sleep(3)
	number_fra=driver.find_elements_by_tag_name("iframe")
	iframes = driver.find_elements_by_xpath("//iframe")
	print(str(len(iframes)))
	for index , iframe in enumerate(iframes):
		yhio=iframe.get_attribute('src')
		print(str(index)+" -- "+iframe.get_attribute('src'))
		if "ccard?platform" in yhio:
			driver.switch_to.frame(index)
			time.sleep(3)
			print("SWITCH TO : "+yhio)
			username=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'first_name')))
			username.click()
			time.sleep(1)
			username.send_keys("baba123A*")
			input('close_button')
			# first_name

	# //*[@id="firstbill"]/div[1]/div[2]/div/input

	input('close_button')


def starting_point():
	try:
		print('starting_point()')
		stage_1()
		# print(sz)
		driver = drive_chrome.build_driver(sz)
		driver.maximize_window()
		browser_op(driver)
	except Exception as e:
		print('starting_point() errrr',e)



def main():
	
	print("main")
	# tor_pro.renew_tor()
	starting_point()



if __name__ == '__main__':

	main()










# 	try:
# 		width ,height=cnf_bvb.resolution_func()
# #		print("OPEN DISPLAY  WEB-SITE ...... ",end='',flush=True)
# # size=(width,height)
# 		# display = Display(visible=1,size=(width,height)).start()
# 		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))

# 	except Exception as error:
# 		print(str(error))