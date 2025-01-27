import os
from playwright.sync_api import sync_playwright

# Get the current directory where the script is located
current_directory = os.getcwd()

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        try:
            print(f"Launching {browser_type.name}...")
            browser = browser_type.launch(headless=True)  # Set headless=False if you want to see the browser
            page = browser.new_page()
            page.goto('https://whatsmybrowser.org/', wait_until="domcontentloaded")  # Wait until page is loaded

            # Define the screenshot path using the script's current directory
            screenshot_path = os.path.join(current_directory, 'tests/screenshots', f'example-{browser_type.name}.png')
            
            # Take the screenshot
            page.screenshot(path=screenshot_path)
            print(f"Screenshot created: {screenshot_path} for {browser_type.name}")

            browser.close()  # Always close the browser after use
        except Exception as e:
            print(f"Error with {browser_type.name}: {e}")
            browser.close()  # Ensure the browser gets closed even in case of error
