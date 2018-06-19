# import libraries
import urllib.request
from bs4 import BeautifulSoup

# specify the urls
quote_page = ['https://www.airbnb.co.uk/rooms/10422593?location=Edinburgh&s=-3aifuLg',
'https://www.airbnb.co.uk/rooms/19278160?s=51', 'https://www.airbnb.co.uk/rooms/14531512?s=51']

for pg in quote_page:
    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(pg)

    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    # get the property name
    propertyname = soup.find('h1', attrs={'class':'_1xu9tpch'}).get_text()
    print("Property Name: " + propertyname)

    # get the property type
    propertytype = soup.find('div', attrs={'class':'_4efw5a'}).get_text()
    print("Property Type: " + propertytype)

    # get No. of bedrooms
    if "1 bed" in soup.get_text():
        print("No. of bedrooms: 1")
    elif "2 beds" in soup.get_text():
        print("No. of bedrooms: 2")
    elif "3 beds" in soup.get_text():
        print("No. of bedrooms: 3")
    else:
        print("More than 3 bedrooms")

    # get No. of bathrooms
    if "1 bath" in soup.get_text():
        print("No. of bathrooms: 1")
    elif "2 baths" in soup.get_text():
        print("No. of bathrooms: 2")
    elif "3 baths" in soup.get_text():
        print("No. of bathrooms: 3")
    else:
        print("More than 3 bathrooms")

    # get list of amenities
    amenities = [element.text for element in soup.find_all('div', attrs={'class':'_ncwphzu'}, limit=8)]
    # tidy up list
    amenities = list(map(lambda s: s.strip(), amenities))
    # remove 1st two items from list (these are not amenities)
    amenities = amenities[2:]
    print("First 6 Amenities: ", amenities)
