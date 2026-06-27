from time import sleep

from playwright.sync_api import Page, expect, BrowserContext, Dialog


def test_visible(page: Page):
    page.goto("https://www.qa-practice.com/elements/input/simple")
    reqt = page.locator("#req_text")
    reqb = page.locator("#req_header")
    expect(reqt).not_to_be_visible()
    expect(reqt).to_be_hidden()
    reqb.click()
    print("абракадабра")
    expect(reqt).to_be_visible()

def test_enabled_and_selected(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/disabled")
    butoon = page.locator("#submit-id-submit")
    expect(butoon).to_be_disabled()
    page.locator("#id_select_state").select_option("Enabled")
    expect(butoon).to_be_enabled()
    expect(butoon).to_have_text("Submit")
    expect(butoon).to_contain_text("ubm")

def test_value(page: Page):
    value = "qwert"
    page.goto("https://www.qa-practice.com/elements/input/simple")
    input_field = page.locator("#id_text_string")
    input_field.fill(value)
    expect(input_field, f"input value is not {value}").to_have_value("text")

def test_focused(page: Page):
    page.goto("https://www.google.com/")
    field = page.locator("[name='q']")
    expect(field).to_be_focused()
    page.locator(".o3j99.qarstb").click()
    expect(field).not_to_be_focused()

def test_tabs(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/link")
    link = page.locator("#new-page-link")
    with context.expect_page() as new_page:
        link.click()
    new_page = new_page.value
    result_text = new_page.locator("#result-text")
    expect(result_text).to_have_text("I am a new page in a new tab")
    new_page.close()
    sleep(2)
    page.get_by_role("link", name="New tab button").click()
    sleep(2)

def test_d_n_d(page: Page):
    page.goto("https://www.qa-practice.com/elements/dragndrop/boxes")
    drag_me = page.locator("#rect-draggable")
    drop_here = page.locator("#rect-droppable")
    drag_me.drag_to(drop_here)
    result_drag = page.locator("#text-droppable")
    expect(result_drag).to_be_visible()
    expect(result_drag).to_have_text("Dropped!")

def accept_alert(alert: Dialog):
    alert.accept()

def accept_alert_with_text(alert: Dialog):
    alert.accept("Vadim")

def dismiss_alert(alert: Dialog):
    alert.dismiss()

def test_alert_easy(page: Page):


    page.goto("https://www.qa-practice.com/elements/alert/alert#")
    # page.on("dialog", accept_alert)
    # page.on("dialog", lambda dialod: dialod.accept())
    page.locator(".a-button").click()


def test_dismiss_alert_with_canceled(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", dismiss_alert)
    page.locator(".a-button").click()

    expect(page.locator("#result-text")).to_have_text("Cancel")


def test_accept_alert_with_canceled(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.on("dialog", accept_alert)
    page.locator(".a-button").click()
    expect(page.locator("#result-text")).to_have_text("Ok")


def test_alert_prompt(page: Page):
    page.goto("https://www.qa-practice.com/elements/alert/prompt")
    page.on("dialog", accept_alert_with_text)
    page.locator(".a-button").click()
    expect(page.locator("#result-text")).to_have_text("Vadim")
    sleep(3)

