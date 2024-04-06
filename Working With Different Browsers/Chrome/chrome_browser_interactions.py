from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Launch the Chrome Browser in Headless Mode
    # browser = playwright.chromium.launch()

    # Print The Browser Type
    # print(browser.browser_type)
    
    # Launch the Chrome Browser in Headful Mode
    # browser = playwright.chromium.launch(headless=False)

    # Launch the Chrome Browser in Headful Mode and define the execution speed
    # browser = playwright.chromium.launch(headless=False, slow_mo=5000)
  
    # Launch the Chrome Browser in Headful Mode and Maximize The Window
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])

    # Open the New Page in Browser
    # page = browser.new_page()  

    # no_viewport=True, gives you more control over the viewport size and allows you to manage the browser window's size and behavior according to your requirements.
    page = browser.new_page(no_viewport=True)  

    # Goto to website
    page.goto("https://www.letskodeit.com/practice")

    # Close The Browser
    browser.close()
