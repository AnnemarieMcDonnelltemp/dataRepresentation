import requests
import csv
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/clare-1/property-for-sale?page=1")
#page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
#print (soup.prettify())
home_file = open('week03MyHome1.csv', mode='w') 
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard" )
print(listings)
for listing in listings:
   entry = []
    
price = listing.find(class_="PropertyListingCard__Price").text
entry.append(price)
address = listing.find(class_="PropertyListingCard__Address").text
entry.append(address)

#print(entry)
home_writer.writerow(entry)
home_file.close()