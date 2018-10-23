import telepot
import time
import requests
from bs4 import BeautifulSoup

token = 'Insert your telegram token'
bot = telepot.Bot(token)

def main(cmd):
	text = cmd['text']
	response = requests.get('https://www.imdb.com/find?ref_nv_sr_fnq=' + text + '&s=all')
	soup = BeautifulSoup(response.text, 'html.parser')
	tag = soup.find('tr',{'class':'findResult odd'})
	html = tag.find('a')
	url = 'https://www.imdb.com' + html['href']
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	tag = soup.find('span', attrs={'itemprop':'ratingValue'})
	rate = tag.text
	bot.sendMessage(cmd['chat']['id'], rate)
	
print('bot is listening')
bot.message_loop(main)

while True:
	time.sleep(10)