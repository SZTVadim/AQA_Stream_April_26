import re

from playwright.sync_api import sync_playwright, expect, Page, BrowserContext

# Селекторы и Локаторы в Playwright

# CSS
orange = ".orangehrm-login-branding" # точка говорит что мы ищем по классу
all_page = "#app"  # ищем по id
login = ".oxd-form-actions.orangehrm-login-action"  # ищем по нескольким классам

# XPath
orange_ = "//div[@class='orangehrm-login-branding']" # точка говорит что мы ищем по классу
all_page_ = "//div[@id='app']"  # ищем по id
login_ = "//*[contains(@class,'orangehrm-login-action')]"  # ищем по одному классу, если их при этом несколько
hard_xpath = "//div[@id='app']//h5[contains(@class,'orangehrm-login-title')]/../../*[@class='orangehrm-login-branding']"

# запускаем PW
# устанавливаем модуль pytest_playwright  (сайт для того чтобы найти нужный пакет https://pypi.org/) pip install pytest-playwright
# устанавливаем модуль playwright pip install playwright
# устанавливаем браузеры playwright install
def test_first_ui(page: Page):
    # with sync_playwright() as p:  # Запускаем сам playwright
        # browser = p.chromium.launch(headless=False, slow_mo=1000, timeout=60000)  # запускаем браузер
        # browser = p.chromium.launch(headless=False, timeout=60000)  # запускаем браузер
        # browser = p.chromium.launch(headless=True)  # запускаем браузер
        # context = browser.new_context()  # создается сессия
        # page = context.new_page()  # открываем страницу
        # page.locator("").locator("").get_by_role("button",name="username").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("[name='username']").fill("Admin")
    page.locator("[name='password']").press_sequentially("admin123", delay=100)
    page.locator("[type='submit']").click()
    expect(page.locator(".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")).to_be_visible()
    expect(page.locator(".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")).to_have_text("Dashboard")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    expect(page).to_have_title("OrangeHRM")

def test_added_employee(page: Page):
    # Логин
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("[name='username']").fill("Admin")
    page.locator("[name='password']").fill("admin123")
    page.locator("[type='submit']").click()
    expect(page).to_have_url(re.compile(r".*dashboard.*"))
    # Список сотрудников → Add
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    page.get_by_role("button", name="Add").click()
    # Форма
    page.get_by_role("textbox", name="First Name").fill("John")
    page.get_by_placeholder("lastName").fill("Doe")
    page.get_by_role("button", name="Save").click()
    # Проверки
    expect(page.locator("h6", has_text="Personal Details")).to_be_visible()
    expect(page.get_by_label("First Name")).to_have_value("John")
    expect(page.get_by_label("Last Name")).to_have_value("Doe")