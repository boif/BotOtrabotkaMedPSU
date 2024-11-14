from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FIO = "Ведищев Борис Вадимович"
GROUP = "24лс3"
TOPIC = "Краниология практика"
GECKODRIVER_PATH = "geckodriver"

def fill_google_form(form_link):
    options = Options()
    options.add_argument("--headless")
    service = Service(GECKODRIVER_PATH)
    driver = webdriver.Firefox(service=service, options=options)

    try:
        driver.get(form_link)

        # Поиск поля для "ФИО"
        fio_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@aria-labelledby="i1 i4"]'))
        )
        fio_input.send_keys(FIO)

        # Поиск поля для "Учебная группа"
        group_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@aria-labelledby="i6 i9"]'))
        )
        group_input.send_keys(GROUP)

        # Поиск поля для "Отрабатываемая тема"
        topic_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@aria-labelledby="i11 i14"]'))
        )
        topic_input.send_keys(TOPIC)

        # Отправка формы
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Отправить"]'))
        )
        submit_button.click()
    finally:
        driver.quit()
