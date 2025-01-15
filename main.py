import csv
import requests
from lxml import html

#url for the product search
product = 'Computer Printers'
url = "https://www.ebay.com/b/{}/1245/bn_320031".format(product.replace(" ", "-"))

#sending request to the ebay url and parsing the data
response = requests.get(url)
a= html.fromstring(response.text)
scraped_data = []

while True:
    #Extract items from the current page
    container = a.xpath("//ul[contains(@class, 'brwrvr__item-results brwrvr__item-results--list')]")
   
    if container:
        items= container[0].xpath(".//li[contains(@class, 'brwrvr__item-card brwrvr__item-card--list')]")
    else:
        items= []
    
    if not items:
        break
    
    #Loop through each item and extract data
    for item in items:
        #Extracting title of the product
        title = "".join(item.xpath(".//h3[@class='textual-display bsig__title__text']//text()"))

        #Extracting the brand of the product
        brand="".join(item.xpath(".//div[@class='bsig brw-signal bsig--subheader']//span[@class='textual-display bsig__generic bsig__listingCondition']//span[last()]//text()"))

        #Extracting the price of the product
        price="".join(item.xpath(".//span[@class='textual-display bsig__price bsig__price--displayprice']/text()"))

        #Extracting the no of reviews for the product
        review_count="".join(item.xpath(".//span[@class='textual-display bsig__product-review__count']/text()"))

        # Extracting stars (ratings) from the product page
        stars="".join(item.xpath(".//div[@class='star-rating']/@aria-label"))

        # Appending the extracted data to the list
        scraped_data.append([title, brand, price, review_count, stars])

     # Check if there is a next page
    next_page = "".join(a.xpath("//a[@class='pagination__next icon-link']/@href"))
    if not next_page:
        break

    # Go to the next page
    response = requests.get(next_page)
    if response.status_code != 200:
        break

    # Update the parsed page for the next iteration
    a = html.fromstring(response.text)


    # Save the scraped data to a CSV file
with open('computer_printers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Brand', 'Price', 'Review_count', 'Rating'])
    writer.writerows(scraped_data)