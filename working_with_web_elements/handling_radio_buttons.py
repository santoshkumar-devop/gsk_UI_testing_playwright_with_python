from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    url = "https://testautomationpractice.blogspot.com/"

    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto(url)

    # Verify Radio button is visible
    radio_button = page.locator("//*[@id='male' and @type='radio']").is_visible()
    print('radio_button_visible=', radio_button)


    # Get the locator and verify Radio button is present
    radio_button = page.locator("#female")
    radio_button_value = radio_button.evaluate('(element) => element.parentElement.innerText')
    print('radio_button_text=', radio_button_value)
    assert radio_button_value == 'Female'

    # Verify Radio button is not visible
    # radio_button = page.locator("#male")
    # expect(radio_button).to_be_hidden()


    # Verify Radio button is enabled
    radio_button = page.locator("#male").is_enabled()
    print('radio_button_enabled=', radio_button)

    # Verify Radio button is disabled or not clickable
    # radio_button = page.locator("#male").is_disabled()
    # print('radio_button_disabled=', radio_button)

    # Verify Radio button is clickable
    radio_button = page.locator("#male").is_editable()
    print('radio_button_clickable=', radio_button)

    # click on the Radio button
    page.locator("#female").check()

    # Verify Radio button is selected or not selected
    radio_button = page.locator("#female").is_checked()
    print('radio_button_selected=', radio_button)


