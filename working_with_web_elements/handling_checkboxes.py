from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    url = "https://testautomationpractice.blogspot.com/"

    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto(url)

    # Verify checkboxes is visible
    checkboxes = page.locator("//*[@id='wednesday' and @type='checkbox']").is_visible()
    print('checkboxes_visible=', checkboxes)


    # Get the locator and verify checkboxes is present
    checkboxes = page.locator("#friday")
    checkboxes_value = checkboxes.evaluate('(element) => element.parentElement.innerText')
    print('checkboxes_text=', checkboxes_value)
    assert checkboxes_value == 'Friday'

    # Verify checkboxes is not visible
    # checkboxes = page.locator("#monday")
    # expect(checkboxes).to_be_hidden()


    # Verify checkboxes is enabled
    checkboxes = page.locator("#tuesday").is_enabled()
    print('checkboxes_enabled=', checkboxes)

    # Verify checkboxes is disabled or not clickable
    # checkboxes = page.locator("#monday").is_disabled()
    # print('checkboxes_disabled=', checkboxes)

    # Verify checkboxes is clickable
    checkboxes = page.locator("#saturday").is_editable()
    print('checkboxes_clickable=', checkboxes)

    # click on the checkboxes
    page.locator("#saturday").check()

    # Verify checkboxes is selected or not selected
    checkboxes = page.locator("#saturday").is_checked()
    print('checkboxes_selected=', checkboxes)


    # uncheck the checkboxes
    page.locator("#saturday").uncheck()


