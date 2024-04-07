from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    url = "https://selectorshub.com/xpath-practice-page/"

    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto(url)


    # i have used different locators to find the button to have a practise

    # Verify Button is visible
    button = page.locator("button[value='Submit']").is_visible()
    print('button_visible=', button)

    # get the locator and verify text is present
    button = page.get_by_role('button', name='Submit')
    expect(button).to_have_text('Submit')

    # asserting button with inbuilt assert keyword
    button = page.locator("button[value='Submit']").get_attribute('value')
    assert button == 'Submit'

    # Verify Button is not visible
    # button = page.locator("//*[text()='Submit']")
    # expect(button).to_be_hidden()


    # Verify Button is enabled
    button = page.get_by_text('Submit')
    enabled=button.is_enabled()
    print('button_enabled=', enabled)

    # Verify Button is disabled or not clickable
    disabled = button.is_disabled()
    print('button_disabled=', disabled)

    # Verify Button is clickable
    clickable = button.is_editable()
    print('button_clickable=', clickable)

    # click on the button
    button.click()
    print('Button Clicked')
