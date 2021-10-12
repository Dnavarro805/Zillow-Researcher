import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from bs4 import BeautifulSoup


# Fetch the service account key JSON file contents
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Minimum required headers in order for the request to return the website HTML
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Accept-Language": "en-US,en;q=0.5"
}

city = "Camarillo"
state = "CA"

url = "https://www.zillow.com/homes/" + city + ",-" + state + "_rb/"

response = requests.get(url, headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

print("All Details:")
all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
print(all_addresses)

all_price_elements = soup.select(".list-card-price")
all_prices = [price.get_text() for price in all_price_elements]
print(all_prices)

all_detail_elements = soup.select(".list-card-details")
all_details = [detail.get_text() for detail in all_detail_elements]
print(all_details)

print("Homes for Sale:")
homes = []
for home in range(len(all_addresses)):
    home += 1
    homes.append(home)
print(homes[-1])

print("The URL's per Listing:")
all_links_elements = soup.select(".list-card-top a")
all_links = []
for link in all_links_elements:
    href = link["href"]
    all_links.append(href)
print(all_links)

print("The ZPID's per Listing:")
ZPID = ''
result = []
for id in all_links:
    result.append(id.split('/')[-2].replace("_zpid", ""))
    ZPID = str(result)
print(ZPID)

print("All Prices per Listing:")
prices = [int(price.get_text().replace("$", "").replace(",", "").replace("+", " ")) for price in all_price_elements]
print(prices)

print("All Bedrooms per Listing:")
all_beds = [int(beds.get_text()[0]) for beds in all_detail_elements]
print(all_beds)

print("All Bathrooms per Listing:")
all_baths = [int(baths.get_text()[5]) for baths in all_detail_elements]
print(all_baths)

print("Total Bedrooms and Bathrooms per Listing:")
all_beds_baths = []
for index in range (0, len(all_beds)):
    all_beds_baths.append(all_beds[index] + all_baths[index])
print(all_beds_baths)

print("All Square Footage per Listing:")
all_sqft = [int(sqft.get_text().replace(",", "")[9:13]) for sqft in all_detail_elements]
print(all_sqft)

print("The average price for a home is:")
average_home_price = sum(prices) / len(all_prices)
print(str(average_home_price))

print("The price per square foot is:")
price_per_sqft = [round(price / sqft, 2) for price, sqft in zip(prices, all_sqft)]
print(str(price_per_sqft))

print("The price per bedrooms is:")
price_per_beds = [round(price / beds, 2) for price, beds in zip(prices, all_beds)]
print(str(price_per_beds))

print("The price per bathrooms is:")
price_per_baths = [round(price / baths, 2) for price, baths in zip(prices, all_baths)]
print(str(price_per_baths))

print("The price per bedrooms and bathrooms is:")
price_per_beds_baths = [round(price / all_beds_baths, 2) for price, all_beds_baths in zip(prices, all_beds_baths)]
print(str(price_per_beds_baths))

data = {
    'URL': all_links,
    'Address': all_addresses,
    'Price': all_prices,
    'Bedrooms': all_beds,
    'Bathrooms': all_baths,
}

dynamic_ID = city + "_" + state

# Save data to firebase
db.collection('Homes').document(dynamic_ID).set(data)
