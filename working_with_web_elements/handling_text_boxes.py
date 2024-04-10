from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    url = "https://testautomationpractice.blogspot.com/"

    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto(url)

    # Verify Textbox is visible
    textbox = page.locator("//*[@id='name' and @type='text']").is_visible()
    print('textbox_visible=', textbox)


    # Add text in the textbox
    #using fill() method to add text
    page.fill("//*[@id='name']", "Test Automation Practice")

    #using type() method to add text
    page.type("#email", "automation@gmail.com") # delay to see typing

    # using keyboard object to add text
    page.locator("#phone").press('1')
    page.locator("#textarea").press('Shift+A')
    page.locator("#textarea").press('A')
    page.locator("#textarea").press('b')
    page.locator("#textarea").press('c', delay=1000)

    # fetch and assert text
    text_value = page.locator("#name").input_value()
    print('text_value=', text_value)
    assert text_value == 'Test Automation Practice'

    # Delete Text
    page.locator("#email").clear()

    # Update text
    page.locator("#name").clear()
    page.fill("#name", "Test Automation Practice Updated")
    text_value = page.locator("#name").input_value()
    print('text_value=', text_value)
    assert text_value == 'Test Automation Practice Updated'

    # other way to update
    text_value = page.locator("#name").input_value()
    page.fill("#name", text_value + ' Twice')

    # Verify Textbox is not visible
    # textbox = page.locator("#name")
    # expect(textbox).to_be_hidden()


    # Verify Textbox is enabled
    textbox = page.locator("#name").is_enabled()
    print('textbox_enabled=', textbox)

    # Verify Textbox is disabled
    # textbox = page.locator("#name").is_disabled()
    # print('textbox_disabled=', textbox)


