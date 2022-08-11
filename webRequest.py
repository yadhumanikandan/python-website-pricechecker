import smtplib
import requests
from bs4 import BeautifulSoup
import time


URL = 'https://www.flipkart.com/nothing-phone-1-black-256-gb/p/itmeea53a564de47?pid=MOBGCYGPWXYRRNB4&param=98765&otracker=clp_bannerads_1_7.bannerAdCard.BANNERADS_A_mobile-phones-big-saving-days-aug-22-t4r4d43-store_WN3BZVEO1ZPX'

def check_price():
	source = requests.get(URL)

	soup = BeautifulSoup(source.content, 'html.parser')

	price = soup.find('div', {'class':'_30jeq3 _16Jk6d'}).get_text()

	extractPrice = float(price[1:7].replace(',',''))
	print(extractPrice)

	if extractPrice <= 30000:
		send_email()
		print('email has been send')


def send_email():
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login("email@gmail.com","password")
	message = '''the price of the product is now below 30000
				 check the link "https://www.flipkart.com/nothing-phone-1-black-256-gb/p/itmeea53a564de47?pid=MOBGCYGPWXYRRNB4&param=98765&otracker=clp_bannerads_1_7.bannerAdCard.BANNERADS_A_mobile-phones-big-saving-days-aug-22-t4r4d43-store_WN3BZVEO1ZPX"
				 '''
	s.sendmail("fromemailaddress@gmail.com", "toemailaddress@gmail.com", message)
	s.quit()


while True:
	check_price()
	time.sleep(60*60*24)
