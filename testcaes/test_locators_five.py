# def test_launch_browser(playwright):
#     browser=playwright.chromium.launch(headless=False)
#     # new window
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://the-internet.herokuapp.com/login")
#     # assert "OrangeHRM" in page.title()
#     page.wait_for_timeout(5000)
#     page.get.by_label("Username").fill("tomsmith")
#     # page.get.by_label("Password").fill("SuperSecretPassword")
#     page.wait_for_timeout(5000)
#     # browser.close()

def test_launch_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/login")
    page.wait_for_timeout(5000)
    page.get_by_label("Username").fill("tomsmith")
    page.wait_for_timeout(5000)
    page.get_by_label("Password").fill("SuperSecretPassword")
    page.wait_for_timeout(5000)
    page.get_by_role("button").click()
    page.wait_for_timeout(5000)


#
# def test_launch_browser(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://the-internet.herokuapp.com/login")
#     page.wait_for_timeout(5000)
#
#     # Fill username using ID
#     page.locator("#username").fill("tomsmith")
#
#     # Fill password using ID
#     page.locator("#password").fill("SuperSecretPassword")
#
#     # Click login button using class name
#     page.locator("button.radius").click()
#
#     page.wait_for_timeout(5000)

# page.locator("//input[@id='username']").fill("tomsmith")