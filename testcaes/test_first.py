import re
from playwright.sync_api import Page

def test_first_exm(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.set_viewport_size(({"width":1920, "height":1080}))
    page.wait_for_timeout(5000)
    title=page.title()
    print("Page of the title"+title)
    assert "OrangeHRM" in title