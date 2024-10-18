import os
import pytest
from playwright.sync_api import sync_playwright

# Hook que configura el navegador en modo escritorio y móvil
@pytest.fixture(scope="function", params=lambda request: request.config.getoption("--browser").split(','))
def browser_context(request):
    with sync_playwright() as p:
        # Verificamos si estamos en un entorno CI (como GitHub Actions)
        headless = bool(os.getenv("CI", False))

        # Determina si se debe grabar video
        record_video = request.config.getoption("--recordvideo").lower() == 'true'

        # Configuración del navegador
        if request.param == "desktop":
            browser = p.chromium.launch(headless=headless)
            context = browser.new_context(record_video_dir="videos/desktop" if record_video else None)
        elif request.param == "mobile":
            iphone_12 = p.devices["iPhone 12"]
            browser = p.chromium.launch(headless=headless)
            context = browser.new_context(
                **iphone_12,
                record_video_dir="videos/mobile" if record_video else None
            )
        else:
            raise ValueError(f"Navegador no soportado: {request.param}")

        page = context.new_page()
        yield page  # Devuelve la página para las pruebas
        context.close()
        browser.close()

# Añadir opciones de línea de comandos
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="desktop", help="Specify the browsers: desktop or mobile")
    parser.addoption("--recordvideo", action="store", default="false", help="Enable or disable video recording: true or false")


