from playwright.sync_api import Page, expect

def test_homepage_title(page: Page):
    page.goto('http://localhost:8000/')
    expect(page).to_have_title('Credit Association')
    expect(page).to_have_url('http://localhost:8000/')



def test_homepage_header(page: Page):
    page.goto('http://localhost:8000/')
    header = page.get_by_text('Register to become a member')
    expect(header).to_be_visible()
    #    assert header.text_content() == 'Register to become a member'
 
def test_homepage_copyright(page: Page):
    page.goto('http://localhost:8000/')
    copyright = page.get_by_test_id('copyright')
    #assert copyright.text_content() == '© 2025'
    expect(copyright).to_contain_text('© 2025')
 