from playwright.sync_api import sync_playwright

# playwright in it global fixture use to setUp things
# object,class, class ksi package se related hota hai
def test_launch_browser(playwright):
    browser=playwright.chromium.launch(headless=False)
    # new window
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert "OrangeHRM" in page.title()
    page.wait_for_timeout(5000)
    browser.close()
# in pythonw e call it function not method