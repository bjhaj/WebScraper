# WebScraper

A command line tool that scrapes every link on a website and saves it as a PDF.

## Dependencies

You will need to have `wkhtmltopdf` installed to use this tool. Here's how to install it on different operating systems:

### macOS

Open a terminal and execute the following command to install `wkhtmltopdf` using Homebrew:

```bash
brew install --cask wkhtmltopdf
```

### Windows
1) Open a web browser and go to the `wkhtmltopdf` download page: https://wkhtmltopdf.org/downloads.html
2) Choose the appropriate Windows version for your system (e.g., Windows 64-bit) and download the installer.
3) Run the installer and follow the installation instructions.

### Linux
Open a terminal and execute the following command to install `wkhtmltopdf`:

On Debian/Ubuntu-based systems:
```bash
sudo apt-get install wkhtmltopdf
```
On Fedora:
```bash
sudo apt-get install wkhtmltopdf
```
On CentOS:
```bash
sudo yum install wkhtmltopdf
```

## Running the Tool
After you have `wkhtmltopdf` installed, you can run the WebScraper tool using the following command:
```bash
python web_scraper.py website_url output_directory
```



