#Here are some common use cases for browser contexts:

#Isolation: 
#        You can create multiple contexts to isolate different sets of cookies, local storage, and other browsing data. This can be useful for testing scenarios where you want to start with a clean browsing state for each test case.

Parallelization: 
#        By using multiple browser contexts, you can run tests in parallel, as each context operates independently.

#Authentication testing: 
#        You can simulate different authentication scenarios by using separate contexts with different sets of login credentials or authentication tokens.

#Privacy testing: 
#        Browser contexts allow you to test privacy features such as browser fingerprinting or tracking protection by isolating browsing data between contexts.


from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    url = "https://playwright.dev/python/"
    # Launch the Chrome Browser
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    print(dir(browser))

    context1=   browser.new_context(no_viewport=True)
    page1 = context1.new_page()
    page1.goto(url)

    # To Print the all opened browser Contexts
    print(browser.contexts)

    context2 = browser.new_context(no_viewport=True)
    page2 = context2.new_page()
    page2.goto(url)

    # To Print the all opened browser Contexts
    print(browser.contexts)

    # To Close the single browser context
    context1.close()

    # To Print the all opened browser Contexts
    print(browser.contexts)

    browser.close()
