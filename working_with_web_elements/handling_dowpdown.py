from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    url = "https://testautomationpractice.blogspot.com/"

    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto(url)

    # Verify dropdown is visible
    dropdown = page.locator("//*[@id='country']").is_visible()
    print('dropdown_visible=', dropdown)

    # Select the value from the dropdown
    dropdown = page.locator("#country")
    dropdown.select_option('india')


    #Verify value selected in dropdown
    selected_option = dropdown.evaluate('(dropdown) => dropdown.value', dropdown)
    print('selected_option=', selected_option)
    assert selected_option == 'india'

    # Verify dropdown is not visible
    # dropdown = page.locator("#country")
    # expect(dropdown).to_be_hidden()

    # Verify dropdown is enabled
    dropdown = page.locator("#country").is_enabled()
    print('dropdown_enabled=', dropdown)

    # Verify dropdown is disabled
    # dropdown = page.locator("#country").is_disabled()
    # print('dropdown_disabled=', dropdown)

    # Verify dropdown is clickable
    dropdown = page.locator("#country").is_editable()
    print('dropdown_clickable=', dropdown)

    # Select multiple values from the dropdown
    dropdown = page.locator("#colors")
    dropdown.select_option(['red', 'green'])
    selected_options = dropdown.evaluate('(element) => Array.from(element.selectedOptions).map(option => option.value)', dropdown)
    print('selected_options=', selected_options)
    assert selected_options == ['red', 'green']
