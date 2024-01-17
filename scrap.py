import requests
from bs4 import BeautifulSoup
import json

def extract_links(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the <a> tags, which typically contain hyperlinks
    links = soup.find_all('a')

    # Extract and filter the href attribute from each link
    # Select links that do not start with 'http://' or 'https://'
    urls = [link.get('href') for link in links if link.get('href') and not link.get('href').startswith(('http://', 'https://',"#"))]

    # Remove duplicates by converting the list to a set, then back to a list
    unique_urls = list(set(urls))

    return unique_urls

# Example usage
url = 'https://docs.flame-engine.org/1.14.0/'  # Replace with the URL you want to scrape
extracted_links = extract_links(url)

# Write the extracted links to a JSON file
with open('extracted_links.json', 'w') as file:
    json.dump(extracted_links, file)

print("Extracted links written to extracted_links.json")
