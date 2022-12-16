from selene import have
from selene.support.shared import browser


def select(element, option):
    element.click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(option)
    ).first.click()

def select_with_typing(element, option):
    element.type(option).press_enter()
