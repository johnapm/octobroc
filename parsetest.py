from bs4 import BeautifulSoup as bs
import requests

page = requests.get("https://steamenginecoffee.com.au")

soup = bs(page.text, 'html.parser')

ps=soup.find_all('p')[0].get_text()
print(ps)
