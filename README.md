# BotOtrabotkaMedPSU

This project is a Google Form link checker bot that automatically scans for new form links in provided text, identifying both short and long Google Form URLs.
Features

    Detects both short (https://forms.gle/) and long (https://docs.google.com/forms/) Google Form links.
    Can parse and extract form links from text content.
    Outputs the detected form link if found.

Prerequisites

    Python 3.7+
    Selenium (for automated form interaction)
    Chrome WebDriver or Firefox Geckodriver (depending on your browser preference)

Installation

    Clone the repository:

git clone https://github.com/your-username/google-form-link-checker-bot.git
cd google-form-link-checker-bot

Set up a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

    Download the WebDriver:
        For Chrome, download ChromeDriver.
        For Firefox, download Geckodriver.

    Ensure the WebDriver is in your system PATH or provide the path to it in your script.

Usage

    Define the text content that the bot will scan for Google Form links.

post_text = "Text containing a Google Form link, e.g., https://forms.gle/example or https://docs.google.com/forms/d/e/example/viewform?usp=sf_link"

Run the script to detect Google Form links:

python form_link_checker.py

Example output:

    Found form link: https://forms.gle/example

Code Explanation

The main detection logic uses a regular expression to capture both short and long Google Form links:

form_link = re.search(r'(https://forms\.gle/\S+|https://docs\.google\.com/forms/d/e/\S+/viewform\S*)', post_text)

    https://forms\.gle/\S+ matches short Google Form URLs.
    https://docs\.google\.com/forms/d/e/\S+/viewform\S* matches long Google Form URLs.

If a link is found, it is printed to the console.
Troubleshooting

    Ensure that your WebDriver matches the version of the browser you’re using.
    If you encounter NoSuchElementException, check that the form fields are correctly targeted by their XPath or CSS selectors.
