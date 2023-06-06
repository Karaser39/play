import pytest
from time import sleep
from playwright.sync_api import sync_playwright, expect


@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        page = browser.new_page()
        yield page
        browser.close()


def test_diary_CRUD_bloodPressure(page):
    page.goto("https://patient.kode.ru/")
    authorization_button_dev = page.locator("#authorization_button_dev")
    authorization_button_dev.click()
    mail_button = page.locator('button', has_text='yar.promo.zapov.a@gmail.com')
    mail_button.click()
    otp_input = page.locator("#otp_input")
    otp_input.click()
    otp_input.fill("19674")
    feature_toggles_button = page.locator('#feature_toggles_button')
    feature_toggles_button.click()
    tmp_healthCharts_button = page.locator("#tmp_healthCharts_button")
    tmp_healthCharts_button.click()
    tmp_newDiaries_button = page.locator('#tmp_newDiaries_button')
    tmp_newDiaries_button.click()
    confirm_feature_toggles_button = page.locator('#confirm_feature_toggles_button')
    confirm_feature_toggles_button.click()
    diaries_card_open_button = page.locator("#diaries_card_open_button")
    diaries_card_open_button.click()
    bloodPressure_tab_button = page.locator('#bloodPressure_tab_button')
    bloodPressure_tab_button.click()
    bloodPressure_tab_add_button = page.locator('#bloodPressure_add_button')
    bloodPressure_tab_add_button.click()
    systolic_value_input = page.locator("#systolic_value")
    systolic_value_input.click()
    systolic_value_input.fill("120")
    diastolic_value_input = page.locator('#diastolic_value')
    diastolic_value_input.click()
    diastolic_value_input.fill("80")
    bloodPressure_tab_confirm_add_button = page.locator('#bloodPressure_confirm_add_button')
    bloodPressure_tab_confirm_add_button.click()
    delay = 3  # в секундах
    sleep(delay)
    bloodPressure_list_button_0 = page.locator("#bloodPressure_list_button_0")
    bloodPressure_list_value_0 = page.locator("#bloodPressure_list_value_0")
    expect(bloodPressure_list_value_0).to_have_text("120 / 80")
    bloodPressure_list_button_0.scroll_into_view_if_needed()
    page.screenshot(path="diary_add_bloodPressure.png")
    bloodPressure_list_button_0.click()
    bloodPressure_edit_button = page.locator('#bloodPressure_edit_button')
    bloodPressure_edit_button.click()
    systolic_value_input.click()
    systolic_value_input.fill("140")
    diastolic_value_input.click()
    page.keyboard.press("Backspace")
    page.keyboard.press("Backspace")
    diastolic_value_input.fill("99")
    bloodPressure_save_edit_button = page.locator('#bloodPressure_save_edit_button')
    bloodPressure_save_edit_button.click()
    sleep(delay)
    expect(bloodPressure_list_value_0).to_have_text("140 / 99")
    bloodPressure_list_button_0.scroll_into_view_if_needed()
    page.screenshot(path="diary_edit_bloodPressure.png")
    bloodPressure_list_button_0.click()
    bloodPressure_delete_button = page.locator('#bloodPressure_delete_button')
    bloodPressure_delete_button.click()
    sleep(delay)
    bloodPressure_list_button_0.scroll_into_view_if_needed()
    page.screenshot(path="diary_delete_bloodPressure.png")










