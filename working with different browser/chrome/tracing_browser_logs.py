from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    url="https://playwright.dev/python/"

    # Launch the Chrome Browser
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])

    # Start tracing the logs and store in a variable ( can be used for debugging )
    start_tracing = browser.start_tracing()

    # Open the New Page
    page = browser.new_page(no_viewport=True)

    # Navigate to website
    page.goto(url)

    # Stop Tracing the Logs
    stop_tracing = browser.stop_tracing()

    # Close The Browser
    browser.close()
