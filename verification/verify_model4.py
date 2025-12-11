from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 320, 'height': 480})

        # Get absolute path to the file
        cwd = os.getcwd()
        file_path = f"file://{cwd}/gate_interstitial/model4.html"

        page.goto(file_path)

        # 1. Take screenshot of initial state (Scratched surface visible)
        page.screenshot(path="verification/gate_ad_model4_initial.png")

        # 2. Simulate Scratching
        # Canvas coordinates
        center_x, center_y = 160, 240

        # Perform a "Z" scratch pattern
        page.mouse.move(50, 50)
        page.mouse.down()
        page.mouse.move(270, 50, steps=10)
        page.mouse.move(50, 430, steps=10)
        page.mouse.move(270, 430, steps=10)
        page.mouse.up()

        # 3. Take screenshot of scratched state
        page.screenshot(path="verification/gate_ad_model4_scratched.png")

        # 4. Scratch more to trigger auto-reveal
        page.mouse.move(160, 240)
        page.mouse.down()
        # Scribble in the middle
        for i in range(10):
            page.mouse.move(100, 200 + i*10, steps=2)
            page.mouse.move(220, 200 + i*10, steps=2)
        page.mouse.up()

        # Wait for fade out animation
        page.wait_for_timeout(1000)

        # 5. Take screenshot of revealed state
        page.screenshot(path="verification/gate_ad_model4_revealed.png")

        browser.close()

if __name__ == "__main__":
    run()
