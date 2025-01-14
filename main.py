import os
import hashlib
import requests
from datetime import datetime

# URL of the page to monitor
URL = 'https://www.ccgeventos.com.br/informa-es-do-evento-e-registro/treasure-cup-one-piece-card-game'  # Change this to your desired page

# File to store the previous day's page content hash
SNAPSHOT_FILE = 'page_snapshot.txt'

def fetch_page_content(url):
    """Fetch the content of the web page."""
    response = requests.get(url)
    return response.text

def save_snapshot(content_hash):
    """Save the content hash to a file."""
    with open(SNAPSHOT_FILE, 'w') as file:
        file.write(content_hash)

def get_saved_snapshot():
    """Retrieve the saved snapshot content hash from the file."""
    if os.path.exists(SNAPSHOT_FILE):
        with open(SNAPSHOT_FILE, 'r') as file:
            return file.read()
    return None

def get_content_hash(content):
    """Generate a hash for the content."""
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def check_if_page_changed():
    """Check if the page has changed compared to the previous day."""
    # Fetch current page content
    current_content = fetch_page_content(URL)
    current_hash = get_content_hash(current_content)

    # Get the previous day's saved snapshot
    saved_hash = get_saved_snapshot()

    if saved_hash is None:
        print("No snapshot found. Saving current page content.")
        save_snapshot(current_hash)
        return False  # No change yet, because it's the first time

    # Compare hashes
    if current_hash == saved_hash:
        print(f"The page has changed since the last check on {datetime.now().strftime('%Y-%m-%d')}.")
        save_snapshot(current_hash)  # Save the new content
        raise Exception("The page has changed since the last check")
    else:
        print(f"No change detected. The page is the same as yesterday ({datetime.now().strftime('%Y-%m-%d')}).")
        return False  # No change

# Main function to check page change
if __name__ == "__main__":
    check_if_page_changed()
