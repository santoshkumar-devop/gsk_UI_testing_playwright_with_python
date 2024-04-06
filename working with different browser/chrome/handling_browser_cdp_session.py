# In Playwright, new_browser_cdp_session is a method that allows you to establish a new Chrome DevTools Protocol (CDP) session for the entire browser instance. The Chrome DevTools Protocol is a set of tools and APIs for automating, debugging, and profiling Chromium-based browsers.

# When you create a new CDP session using new_browser_cdp_session, you gain access to low-level browser functionalities and debugging capabilities provided by the Chrome DevTools Protocol. This can be useful for advanced browser automation tasks or for accessing features not directly exposed through Playwright's high-level API.


from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    url="https://playwright.dev/python/"
    # Launch the Chrome Browser
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])

    # Open the New Page
    page = browser.new_page(no_viewport=True)

    cdp_session = page.context.new_cdp_session(page)

    # protocol methods can be called with 'session.send' method.
    cdp_session.send("Animation.enable")

    # protocol events can be subscribed to with 'session.on' method.
    cdp_session.on("Animation.animationCreated", lambda: print("animation created!"))

    # other methods to use
    # cdp_session.detach()
    # cdp_session.remove_listener()
    # cdp_session.once()

    page.goto(url)

    browser.close()
