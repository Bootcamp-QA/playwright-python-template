# Playwright Python Template

Template para crear un proyecto de **Playwright** con **Python** para realizar pruebas end-to-end.

## Descripción

Este proyecto realiza pruebas E2E en la web [Bootcamp QA](https://bootcampqa.com), generando un reporte de resultados y grabaciones en video. Las pruebas se ejecutan tanto en **Chrome** (escritorio) como en **iPhone 12** (móvil, emulado).

## Tecnologías

- ![Python](https://img.shields.io/badge/Python-3.9%2B-blue)  
- ![Playwright](https://img.shields.io/badge/Playwright-v1.39-green)

## Ver Resultados

El estado de las pruebas se puede ver mediante el siguiente badge de **GitHub Actions**:

![Test Workflow](https://github.com/Bootcamp-QA/playwright-python-template/actions/workflows/playwright_tests.yml/badge.svg)

## Requisitos

### Instalación de Python

1. Descarga e instala Python desde su [página oficial](https://www.python.org/downloads/). Asegúrate de seleccionar la versión adecuada para tu sistema operativo (Python 3.9 o superior).
2. Asegúrate de añadir Python a tu `PATH` durante la instalación.

### Instalar Dependencias

Una vez que tengas Python instalado, clona este repositorio y navega a la carpeta del proyecto. Luego, instala las dependencias necesarias ejecutando los siguientes comandos en la terminal:

pip install -r requirements.txt

Luego instala los navegadores para Playwright con:

playwright install

### Ejecutar en Local
Para ejecutar las pruebas en local, usa el siguiente comando en la terminal:
pytest
Si no reconoce el comando pytest puedes ejecutarlo con python
python -m pytest

### Parametros
Para ejecutar en el navegador chrome, firefox o webkit
--browser (chromium, firefox, webkit)

Para ejecutar en modo visible
--headed

Para ejecutar en paralelo
--numprocesses 2

Para emular un dispositivo (escritorio o movil) concreto
Puedes elegir de la lista
https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json
--device="iPhone 12"

# Generar reporte html
Necesario tener instalado pytest-html
--html=report.html

# Generar traza del error
--tracing on (on, off,retain-on-failure)

# Abrir traza del error
playwright show-trace trace.zip

https://playwright.dev/python/docs/test-runners

--video Whether to record video for each test. on, off, or retain-on-failure (default: off).
--screenshot Whether to automatically capture a screenshot after each test. on, off, or only-on-failure (default: off).
--full-page-screenshot Whether to take a full page screenshot on failure. By default, only the viewport is captured. Requires --screenshot to be enabled (default: off).

### Generar codigo
playwright codegen https://bootcampqa.com

### Debugear codigo
set PWDEBUG=1
pytest -s test_visit_page.py  
pytest -s -k  test_visit



