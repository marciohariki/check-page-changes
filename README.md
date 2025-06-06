# Website Hash Checker

This repository contains a Python script to monitor changes on a specified website. It works by checking the hash of the website's content and sending an email alert if any changes are detected. The script is scheduled to run daily using GitHub Actions.

---

## Prerequisites

1. **Python Version**  
   Ensure you have **Python 3** installed. You can verify your Python version by running:
   ```bash
    python3 --version

    Required Packages
    The script requires the requests library. Install it using:

    pip install requests

## How to Use

1. Clone the Repository

Clone this repository to your local machine:

    git clone https://github.com/your-username/website-hash-checker.git
    cd website-hash-checker


2. Configure the Script
Edit the script to specify:
- The URL of the website to monitor.
- Email credentials and recipients for notifications.

3. Run the Script Locally (Optional)
You can test the script locally by running:
   ```bash
   python3 check_website.py

## GitHub Actions Setup

This repository includes a pre-configured GitHub Actions workflow to automate the hash check. The workflow runs the script daily and sends an email notification if a change is detected.
Steps:

1. Set Up Repository Secrets

In your GitHub repository, navigate to Settings > Secrets and variables > Actions and add the following secrets:
    EMAIL_USERNAME: Your email address.
    EMAIL_PASSWORD: Your email password or app-specific password.

2. Workflow Configuration

The included workflow file (.github/workflows/daily_page_check.yml) is already configured to:
    Run the script daily at 12:00 AM UTC.
    Send an email alert if the hash changes.

3. Commit and Push

Commit and push your changes to activate the workflow:

    git add .
    git commit -m "Set up hash checker with GitHub Actions"
    git push

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to reach out for any issues or suggestions!