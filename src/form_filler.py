import asyncio
from playwright.async_api import async_playwright

async def fill_google_form_async(form_link, fio, group, topic, semaphore, browser):
    async with semaphore:
        page = await browser.new_page()  # Открываем новую вкладку

        try:
            print(f"Переход на форму: {form_link}")
            await page.goto(form_link, wait_until="load")  # Переход на форму и ожидание загрузки
            print("Страница загружена!")

            # Проверка наличия полей
            await page.fill('//input[@aria-labelledby="i1 i4"]', fio)  # Заполнение поля FIO
            print(f"Заполнение поля FIO: {fio}")

            await page.fill('//input[@aria-labelledby="i6 i9"]', group)  # Заполнение поля group
            print(f"Заполнение поля Group: {group}")

            await page.fill('//input[@aria-labelledby="i11 i14"]', topic)  # Заполнение поля topic
            print(f"Заполнение поля Topic: {topic}")

            await page.click('//span[text()="Отправить"]')  # Отправка формы
            print(f"Форма для {fio} успешно отправлена.")

            # Пытаемся дождаться изменения страницы (например, сообщение о успешной отправке)
            await page.wait_for_selector('text=Спасибо за отправку!')  # Пример ожидания подтверждения
            print(f"Форма для {fio} успешно отправлена и подтверждена.")

        except Exception as e:
            print(f"Ошибка при заполнении формы для {fio}: {e}")
        finally:
            await page.close()  # Закрываем вкладку

async def fill_forms_with_sessions(form_link, users, semaphore):
    async with async_playwright() as p:
        # Запуск браузера для первого пользователя с первой сессией
        browser1 = await p.chromium.launch_persistent_context(
            user_data_dir="./user_data_1",  # Первая папка с сессией
            headless=True,  # Видимый браузер
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-extensions",
                "--disable-dev-shm-usage",
                "--no-sandbox"
            ],
        )

        # Запуск браузера для второго пользователя с второй сессией
        browser2 = await p.chromium.launch_persistent_context(
            user_data_dir="./user_data_2",  # Вторая папка с сессией
            headless=True,  # Видимый браузер
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-extensions",
                "--disable-dev-shm-usage",
                "--no-sandbox"
            ],
        )

        # Запуск задач для всех пользователей
        tasks = [
            fill_google_form_async(form_link, user['fio'], user['group'], user['topic'], semaphore, browser1 if i == 0 else browser2)
            for i, user in enumerate(users)
        ]
        await asyncio.gather(*tasks)

        # Закрытие браузеров после всех задач
        await browser1.close()
        await browser2.close()