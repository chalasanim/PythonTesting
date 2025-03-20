from playwright.sync_api import sync_playwright
import re

with sync_playwright() as play :
    #launch browser
    browser = play.chromium.launch(headless=False)

    #create new page
    page = browser.new_page()

    page.goto("https://fakestore.testelka.pl/")

    page.get_by_role("link", name="Store").click()

    headings = page.get_by_role("heading").all_text_contents()

    for heading in headings:
        print(heading)


    