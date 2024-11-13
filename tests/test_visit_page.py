from playwright.sync_api import Page, expect

@pytest.mark.scenario_name("Singup with empty email")
def test_visit(page: Page):
    print("Given user visit homepage")
    page.goto("https://bootcampqa.com")
    

