
def login_hermiona(page):
    customer_login_button = page.locator('button', has_text='Customer Login')
    customer_login_button.click()
    you_name_list = page.locator("#userSelect")
    you_name_list.click()
    page.keyboard.press("H")
    page.keyboard.press("Enter")


def deposite_100(page):

    deposite_button = page.locator('button', has_text='Deposit ')
    deposite_button.click()
    amount_input = page.locator('[placeholder="amount"]')
    amount_input.click()
    amount_input.fill("100")
    deposite_sumbit_button = page.locator(".btn.btn-default")
    deposite_sumbit_button.click()



