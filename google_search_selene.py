from selene import browser, be, have


browser.open('http://google.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
