import time
from vk_monitor import get_latest_post
from form_filler import fill_google_form

FORM_CHECK_INTERVAL = 5

# Данные пользователей
users = [
    {"fio": "Ведищев Борис Вадимович", "group": "24лс3", "topic": "Краниология практика"},
    {"fio": "Абакумова Полина Александровна", "group": "24лс3", "topic": "Остеоартрология практика"}
]

def main():
    print('Запуск бота...')
    while True:
        print("Проверка на наличие новой формы...")
        try:
            post_text, form_link = get_latest_post()
            if form_link:
                print(f"Найдена ссылка на форму: {form_link}")
                # Заполнение формы для каждого пользователя
                for user in users:
                    print(f"Заполнение формы для {user['fio']}...")
                    fill_google_form(form_link, user['fio'], user['group'], user['topic'])
                    print(f"Форма для {user['fio']} успешно заполнена.")
                break
            else:
                print("Форма не найдена, следующая проверка через несколько секунд.")
        except Exception as e:
            print(f"Произошла ошибка при выполнении цикла: {e}")
        time.sleep(FORM_CHECK_INTERVAL)

if __name__ == "__main__":
    main()
