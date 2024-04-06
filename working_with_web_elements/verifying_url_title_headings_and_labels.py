from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    url = "https://testautomationpractice.blogspot.com/"

    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)
    page.goto(url)

############################################################################

    # URL PATH VALIDATION
    current_url = page.url

    # asserting url with inbuilt assert keyword
    assert current_url == url

    # asserting url with web first assertions
    expect(page).to_have_url(url)

############################################################################

    # PAGE TITLE VALIDATION
    page_title = page.title()

    # asserting title with inbuilt assert keyword
    assert page_title == 'Automation Testing Practice'

    # asserting with web first assertions
    expect(page).to_have_title('Automation Testing Practice')

############################################################################

    # HEADINGS VALIDATION ( Positive Case )
    # To verify Heading is visible
    page.locator("//*[@class='title' and contains(., 'Automation Testing Practice')]").is_visible()

    # To get the locator and verify text is present
    heading = page.locator('h1.title')
    expect(heading).to_have_text('Automation Testing Practice')

    # asserting title with inbuilt assert keyword
    # inner_text() -> will fetch the text from the locator
    heading = page.locator('h1.title').inner_text()
    assert heading == 'Automation Testing Practice'


    # Verifying heading is not visible

    # heading = page.locator("//*[@class='title' and contains(., 'Automation Testing Practice')]")
    # expect(heading).to_be_hidden()


############################################################################

    # LABELS VALIDATION ( Positive Case )
    # To verify Label is visible
    page.locator("//*[@for='textbox' and contains(., 'Name:')]").is_visible()

    # To get the locator and verify text is present
    label = page.locator("//*[@for='textbox' and contains(., 'Name:')]")
    expect(label).to_have_text('Name:')
    # For loose validation
    expect(label).to_contain_text('Nam')

    # asserting label with inbuilt assert keyword
    # inner_text() -> will fetch the text from the locator
    label = page.locator("//*[@for='textbox' and contains(., 'Name:')]").inner_text()
    assert label == 'Name:'

    # Verifying label is not visible

    # label = page.locator("//*[@for='textbox' and contains(., 'Name:')]")
    # expect(label).to_be_hidden()

    browser.close()
