import pytest, logging
from playwright.sync_api import sync_playwright

#This file configures Playwright settings and fixtures:
# Configure logging

logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)


# Create a logger
logger = logging.getLogger("pytest")

#usage  pytest.logger.info("Test execution started")

# Make the logger available to all tests
def pytest_configure():
    # Attach the logger to the pytest namespace
    pytest.logger = logger



@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # Launch the browser (Chromium by default)
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    # Create a new page for each test
    page = browser.new_page()
    yield page
    page.close()

# Shared settings for all tests
@pytest.fixture(autouse=True)
def setup(page):
    # Set a base URL (optional)
    page.set_default_timeout(100000)  # Set default timeout
    #page.goto("http://127.0.0.1:3000")  # Replace with your base URL
    page.goto("https://fakestore.testelka.pl/")

'''Configure Browsers (Optional)
To run tests on multiple browsers (like Chromium, Firefox, and WebKit), 
you can parameterize the browser fixture:'''

@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
def browser(request):
    with sync_playwright() as p:
        # Launch the selected browser
        if request.param == "chromium":
            browser = p.chromium.launch(headless=False)
        elif request.param == "firefox":
            browser = p.firefox.launch(headless=False)
        elif request.param == "webkit":
            browser = p.webkit.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(autouse=True)
def trace_test(page):
    # Start tracing
    page.context.tracing.start(screenshots=True, snapshots=True)

    yield

    # Stop tracing and save the trace
    page.context.tracing.stop(path="trace.zip")
