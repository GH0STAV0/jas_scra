from stem import Signal
from stem.control import Controller
from stem import CircStatus

import sys , subprocess , os ,requests,string,random,datetime ,time


proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050',}

controller = Controller.from_port(port=9051)

def call_ip0():
	s = requests.Session()
	s.proxies = proxies
	r = s.get('https://api.ipify.org')
	# print(r.text)
	m_ip=r.text
	return m_ip

######################################################
######################################################


def fix_tor():
	print(" FIXING TOR  CONNECTION : ",end='',flush=True)
	with open(os.devnull, 'wb') as hide_output:
		exit_code = subprocess.Popen(['service', "tor", 'restart'], stdout=hide_output, stderr=hide_output).wait()
		if exit_code==0:
			print("TOR FIXED")



########################  T   O   R ################

def renew_tor():
	# print("Tor is Ready !!! : ", end='')
	controller.authenticate()
	controller.signal(Signal.NEWNYM)
	time.sleep(controller.get_newnym_wait())
	for circ in controller.get_circuits():
		if circ.status != CircStatus.BUILT:
			continue
		exit_fp, exit_nickname = circ.path[-1]
	exit_desc = controller.get_network_status(exit_fp, None)
	exit_address = exit_desc.address if exit_desc else 'unknown'
	# print(exit_address)
	# print(" [ @K ]")
	tor_ip=call_ip0()
	print("Tor is Ready !!! : ",tor_ip)

######################################################



# fix_tor()
