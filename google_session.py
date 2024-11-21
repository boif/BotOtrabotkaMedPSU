import asyncio
from playwright.async_api import async_playwright

async def create_sessions():
    async with async_playwright() as p:
        # Создаем две сессии для пользователей
        browser1 = await p.chromium.launch_persistent_context(
            user_data_dir="./user_data_1",  # Первая папка с сессией
            headless=False,  # Видимый браузер
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-extensions",
                "--disable-dev-shm-usage",
                "--no-sandbox"
            ],
        )

        browser2 = await p.chromium.launch_persistent_context(
            user_data_dir="./user_data_2",  # Вторая папка с сессией
            headless=False,  # Видимый браузер
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-extensions",
                "--disable-dev-shm-usage",
                "--no-sandbox"
            ],
        )

        # Пример перехода на Google и авторизации
        page1 = await browser1.new_page()
        await page1.goto('https://accounts.google.com/')
        print("Авторизуйтесь в Google на первом аккаунте. Нажмите Enter, чтобы продолжить...")
        input()  # Ожидаем, пока пользователь авторизуется

        page2 = await browser2.new_page()
        await page2.goto('https://accounts.google.com/')
        print("Авторизуйтесь в Google на втором аккаунте. Нажмите Enter, чтобы продолжить...")
        input()  # Ожидаем, пока пользователь авторизуется

        print("Сессии для пользователей созданы и сохранены!")

        # После этого браузеры не будут закрыты, они останутся с сессиями.

        # Закрытие браузеров после завершения работы (если нужно)
        await browser1.close()
        await browser2.close()

# Запуск создания сессий
asyncio.run(create_sessions())
