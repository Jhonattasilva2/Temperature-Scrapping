import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

html = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp', headers=headers).content

soup = BeautifulSoup(html, 'html.parser')

temperatura_maxima = soup.find(id='max-temp-1').text
temperatura_minima = soup.find(id='min-temp-1').text
text = soup.find(class_='-gray -line-height-24 _center').text

print(f'A temperatura mínima é: {temperatura_minima}C')
print(f'A temperatura máxima é: {temperatura_maxima}C')
print(text)

