from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    url = "https://playwright.dev/python/"
    # Launch the Chrome Browser in Headless Mode
    # browser = playwright.chromium.launch()

    # Print The Browser Type
    # print(browser.browser_type)

    # Print Browser Version
    # print(browser.version)

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
    print(dir(page))

    # Goto to website
    page.goto(url)

    # Get The Url
    fetch_url = page.url
    print(fetch_url)

    # Get The title of Page
    page_title = page.title()
    print(page_title)

    # Refresh the Browser
    page.reload()


    # one step backward in the browser history
    page.goto("https://www.google.com")
    page_title = page.title()
    print(page_title)

    # Navigate to Previous Page
    page.go_back()

    page_title = page.title()
    print(page_title)


    # one step forward in the browser history

    # Navigate to Next Page
    page.go_forward()

    page_title = page.title()
    print(page_title)

    # Get the source of a Current Page
    page_source = page.content()
    #print(page_source)

    # Close The Browser
    browser.close()

    # To CLose the Multiple Opened Browsers
    # Store all opened browser instances in a list and iterate one by one to close

    # for browser in browsers:
    #     browser.close()
