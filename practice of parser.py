import requests
from bs4 import BeautifulSoup
import re
link = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = BeautifulSoup(link.text,'html.parser')
def country(souper):
    country_list = []
    for country_infos in souper :
        countries_info = (re.sub(r'\s+',' ',country_infos.text).strip())
        country_list.append(countries_info)

    country_info_20 = (country_list[0:20])
    return (country_info_20)

pop = country(souper = soup.find_all('span' , attrs={'class' : 'country-population'}))
area = country(souper = soup.find_all('span' , attrs={'class' : 'country-area'}))
capital = country(souper = soup.find_all('span' , attrs={'class' : 'country-capital'}))
name = country(souper = soup.find_all('h3' , attrs={'class' : 'country-name'}))





















'''
import requests
import bs4
from bs4 import BeautifulSoup
import re
link = requests.get('https://www.scrapethissite.com/pages/simple/')
soup = BeautifulSoup(link.text,'html.parser')
country_name = soup.find_all('h3' , attrs={'class' : 'country-name'})
country_list = []
for country in country_name :
    countries = (re.sub(r'\s+',' ',country.text).strip())
    country_list.append(countries)

country_20 = (country_list[0:20])
print(country_20)

country_capital = soup.find_all('span' , attrs={'class' : 'country-capital'})
country_capital_list = []
for country in country_capital :
    countries_capital = (re.sub(r'\s+',' ',country.text).strip())
    country_capital_list.append(countries_capital)

country_capital_20 = (country_capital_list[0:20])
print(country_capital_20)

country_population = soup.find_all('span' , attrs={'class' : 'country-population'})
country_population_list = []
for country_pop in country_population :
    countries_capital = (re.sub(r'\s+',' ',country_pop.text).strip())
    country_population_list.append(countries_capital)

country_population_20 = (country_population_list[0:20])
print(country_population_20)


country_area = soup.find_all('span' , attrs={'class' : 'country-area'})
country_area_list = []
for country_areas in country_area :
    countries_area = (re.sub(r'\s+',' ',country_areas.text).strip())
    country_area_list.append(countries_area)

country_area_20 = (country_area_list[0:20])
print(country_area_20)
'''