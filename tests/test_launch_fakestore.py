from playwright.sync_api import expect
import logging

# Create a logger

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def test_has_title(page):
    # The setup fixture has already navigated to the Playwright website
    # Expect a title "to contain" a ......
    expect(page).to_have_title("FakeStore – Sklep do nauki testowania")

def test_get_started_link(page):
    # The setup fixture has already navigated to the Playwright website
    page.get_by_role("link", name="Store").click()

   #Expect the page to have a heading with the name "Installation"
    expect(page.get_by_role("heading", name="Wybierz podróż dla siebie!")).to_be_visible()

