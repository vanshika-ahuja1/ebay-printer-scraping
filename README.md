# eBay Data Scraping for Computer Printers

This project demonstrates how to perform web scraping on eBay's product listings, specifically for **computer printers**. The project uses the `requests` library to fetch pages and the `lxml` library to parse the HTML and extract relevant information such as product title, brand, price, review count, and star rating.

## Libraries Used
- `requests`: To send HTTP requests and retrieve HTML pages.
- `lxml`: To parse the HTML content and extract the required data using XPath.

## Description

This project fetches product data for **Computer Printers** from eBay and stores it in a **CSV** file. The program scrapes information such as:

- **Title**: The title of the product
- **Brand**: The brand of the product
- **Price**: The price of the product
- **Review Count**: The number of reviews the product has received
- **Star Rating**: The rating of the product in stars

The script navigates through eBay's product pages, extracts the relevant data, and saves it into a CSV file called `computer_printers.csv`.
