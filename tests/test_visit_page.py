# Test que abre la página principal en ambos dispositivos
def test_visit_page(browser_context):
    page = browser_context
    page.goto("https://bootcampqa.com")
    assert page.title() == "Bootcamp QA"