import asyncio
from vk_monitor import get_latest_post
from form_filler import fill_forms_with_sessions

FORM_CHECK_INTERVAL = 1  # Интервал проверки формы (в секундах)

# Данные пользователей
users = [
    {"fio": "Ведищев Борис Вадимович", "group": "24лс3", "topic": "Остеоартрология теория"},
    {"fio": "Абакумова Полина Александровна", "group": "24лс3", "topic": "Остеоартрология практика"}
]

# Максимальное количество параллельных задач
MAX_CONCURRENT_TASKS = 2


async def main():
    print("Запуск бота...")
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_TASKS)

    while True:
        print("Проверка наличия новой формы...")
        try:
            post_text, form_link = get_latest_post()  # Проверка на наличие нового поста
            if form_link:
                print(f"Найдена ссылка на форму: {form_link}")

                # Запускаем процесс заполнения формы
                await fill_forms_with_sessions(form_link, users, semaphore)
                print("Все формы успешно заполнены.")
                break  # Завершаем выполнение бота
            else:
                print("Форма не найдена. Повторная проверка через несколько секунд.")
        except Exception as e:
            print(f"Произошла ошибка при выполнении: {e}")
        await asyncio.sleep(FORM_CHECK_INTERVAL)  # Задержка перед следующей проверкой


if __name__ == "__main__":
    asyncio.run(main())
