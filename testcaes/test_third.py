from playwright.sync_api import sync_playwright

Edge_Path="C:\Program Files (x86)\Microsoft\Edge\Application"

def test_execution_in_edge():
    with sync_playwright() as p:
        # browser=p.chromium.launch(executable_path=Edge_Path,headless=False)
        browser = p.chromium.launch(headless=False)
        page=browser.new_page()
        # page.goto("https://www.google.co.uk/")
        page.goto("https://www.google.com")
        page.wait_for_timeout(2000)
        page.goto("https://www.facebook.com/")
        page.wait_for_timeout(2000)
        page.go_back()
        page.wait_for_timeout(2000)
        page.go_forward()
        page.wait_for_timeout(2000)
        page.reload()
        title=page.title()
        print("page titile is:",title)
        # page.wait_for_timeout(15000)
        # page.goto("https:// www.facebook.com /")
