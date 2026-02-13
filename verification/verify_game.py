from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 320, 'height': 480})

        # Load the file directly from the filesystem
        cwd = os.getcwd()
        filepath = f"file://{cwd}/gate_interstitial/gate_crypto_catcher.html"
        page.goto(filepath)

        # Wait a bit for game loop to run and things to spawn
        page.wait_for_timeout(2000)

        # Take a screenshot
        page.screenshot(path="verification/gate_game.png")

        browser.close()

if __name__ == "__main__":
    run()
