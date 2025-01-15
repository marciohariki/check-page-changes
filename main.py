import requests
from bs4 import BeautifulSoup

# URL of the page to monitor
URL = 'https://www.ccgeventos.com.br/informa-es-do-evento-e-registro/treasure-cup-one-piece-card-game'  # Change this to your desired page
TARGET_STRING = "Esse evento está esgotado."

# Function to check if the string is present on a webpage
def check_page_for_string(url, target_string):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if the target string is in the page content
        if target_string in soup.get_text():
            raise Exception(f'The string "{target_string}" was not found on the page.')

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to fetch the page: {e}")
        return False



# Main function to check page change
if __name__ == "__main__":
    check_page_for_string(URL, TARGET_STRING)
