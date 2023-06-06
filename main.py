import pytest
from playwright.sync_api import sync_playwright, expect


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=50)
#     page = browser.new_page()
#
#     page.goto("https://www.google.ru/")
#     search_input = page.locator("[name='q']")
#     search_input.fill("ебать ты лох")
#     page.keyboard.press("Enter")
#     memepedia_title = page.locator('[href="https://memepedia.ru/ebat-ty-lox/"]').locator("h3")
#     print(memepedia_title.inner_text())
#     page.screenshot(path="example.png")
#     expect(memepedia_title).to_have_text("Какой же ты лох (мем с двумя гопниками в шапках)")
#
#     browser.close()


@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_memepedia_title(page):
    page.goto("https://www.google.ru/")
    search_input = page.locator("[name='q']")
    search_input.fill("ебать ты лох")
    page.keyboard.press("Enter")
    memepedia_title = page.locator('[href="https://memepedia.ru/ebat-ty-lox/"]').locator("h3")
    print(f"\n{memepedia_title.inner_text()}")
    page.screenshot(path="example.png")
    expect(memepedia_title).to_have_text("Какой же ты лох (мем с двумя гопниками в шапках)")
