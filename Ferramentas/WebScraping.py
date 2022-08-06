# Desenvolvendo o web scraping, pega informações http de um site, pega todo html e analisa.
from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebendo o conteudo da requisição http do site...
soup = BeautifulSoup(site, 'html.parser')
#objeto soup baixando do site o html

#print(soup.prettify())
#transforma o html em string e o print exibe
# temperatura = soup.find("span", class_="block _margin-b-5 -gray")
temperatura = soup.find("h4", class_="-gray-dark-2 -font-base -bold")
#
print(temperatura.string)
print(soup.a)
print(soup.title)
print(soup.title.string)
print(soup.find('admin'))


