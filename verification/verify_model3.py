from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 320, 'height': 480})

        # Get absolute path to the file
        cwd = os.getcwd()
        file_path = f"file://{cwd}/gate_interstitial/model3.html"

        page.goto(file_path)

        # 1. Take screenshot of locked state
        page.screenshot(path="verification/gate_ad_model3_locked.png")

        # 2. Interact: Drag the slider to unlock
        # Get the slider handle bounding box
        handle = page.locator("#sliderHandle")
        box = handle.bounding_box()

        if box:
            # Simulate drag
            page.mouse.move(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
            page.mouse.down()
            # Move to the right
            page.mouse.move(box["x"] + 250, box["y"] + box["height"] / 2, steps=10)
            page.mouse.up()

            # Wait for animation
            page.wait_for_timeout(1500)

            # 3. Take screenshot of unlocked state
            page.screenshot(path="verification/gate_ad_model3_unlocked.png")

        browser.close()

if __name__ == "__main__":
    run()
