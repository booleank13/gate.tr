from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 320, 'height': 480})

        # Get absolute path to the file
        cwd = os.getcwd()
        file_path = f"file://{cwd}/gate_interstitial/model2.html"

        page.goto(file_path)

        # Wait for animations to finish (roughly)
        page.wait_for_timeout(2000)

        # Take a screenshot
        page.screenshot(path="verification/gate_ad_model2.png")

        browser.close()

if __name__ == "__main__":
    run()
