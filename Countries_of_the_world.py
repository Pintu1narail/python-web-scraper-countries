import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.scrapethissite.com/pages/simple/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://google.com'
}

with open('country_info.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Country name", "Capital", "Population", "Area"])
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    country_details = soup.find_all('div', class_="col-md-4 country")
    
    for country in country_details:
        name = country.find('h3', class_='country-name').get_text(strip=True)
        capital = country.find('span', class_='country-capital').get_text(strip=True)
        population = country.find('span', class_='country-population').get_text(strip=True)
        area = country.find('span', class_='country-area').get_text(strip=True)
        
        writer.writerow([name, capital, population, area])
        
print("Data scraping Completed!")