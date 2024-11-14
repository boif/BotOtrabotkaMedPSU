import time
from vk_monitor import get_latest_post
from form_filler import fill_google_form
from cnf.config import FORM_CHECK_INTERVAL

def main():
    print('Запуск бота...')
    while True:
        print("Проверка на наличие новой формы...")
        try:
            post_text, form_link = get_latest_post()
            if form_link:
                print(f"Найдена ссылка на форму: {form_link}")
                fill_google_form(form_link)
                print("Форма успешно заполнена.")
                break
            else:
                print("Форма не найдена, следующая проверка через несколько секунд.")
        except Exception as e:
            print(f"Произошла ошибка при выполнении цикла: {e}")
        time.sleep(FORM_CHECK_INTERVAL)

if __name__ == "__main__":
    main()
