from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 320, 'height': 480})

        # Load the file
        file_path = os.path.abspath("gate_interstitial/model6.html")
        page.goto(f"file://{file_path}")

        print("Model 6 loaded.")

        # Select BTC card and Scanner
        btc_card = page.locator("#btc")
        scanner = page.locator("#scanner-zone")

        # Drag BTC to scanner
        btc_box = btc_card.bounding_box()
        scanner_box = scanner.bounding_box()

        if btc_box and scanner_box:
            # Move to card
            page.mouse.move(btc_box["x"] + btc_box["width"]/2, btc_box["y"] + btc_box["height"]/2)
            page.mouse.down()

            # Drag to scanner center
            page.mouse.move(scanner_box["x"] + scanner_box["width"]/2, scanner_box["y"] + scanner_box["height"]/2, steps=10)
            page.mouse.up()
            print("Dropped BTC on Scanner.")

            # Wait for animation and End Screen
            page.wait_for_timeout(2000)

            # Verify End Screen
            end_screen = page.locator("#end-screen")
            if end_screen.is_visible():
                print("End screen is visible.")
                title = page.locator("#end-title").text_content()
                print(f"End Title: {title}") # Should be "Moon Mission"

            page.screenshot(path="verification/model6_btc_result.png")
            print("Screenshot taken.")

        browser.close()

if __name__ == "__main__":
    run()
