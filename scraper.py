import os
import sys
import requests
from bs4 import BeautifulSoup
import pdfkit

def save_webpage_as_pdf(url, output_path):
    pdfkit.from_url(url, output_path)

def main(url, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Fetch the HTML content of the website
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all links on the page
    links = soup.find_all('a')

    # Loop through each link and save as PDF
    for link in links:
        link_url = link.get('href')
        if link_url and link_url.startswith('http'):
            pdf_filename = link_url.split('/')[-1] + '.pdf'
            pdf_path = os.path.join(output_directory, pdf_filename)
            save_webpage_as_pdf(link_url, pdf_path)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script_name.py website_url output_directory")
        sys.exit(1)

    website_url = sys.argv[1]
    output_directory = sys.argv[2]
    main(website_url, output_directory)
