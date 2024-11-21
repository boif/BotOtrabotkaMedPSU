import requests
import re

ACCESS_TOKEN = "vk1.a.wI69TmevYcNEr-l_axmmx7gZAMoLXibJrLt2o-GZ0DyWJyeA9psSKxM8ekU34HZWhPhVeNY0bCV6XXPjG1oyeafH3EKJonMhCFOsqAKhMgjQBeGpwGjT3KNQCsoyDpCIfK64_fh9qjRJgilZxrekDDXSxWMPDy18GTTDA5YOw1DOqwU4J29DBWM0e-INkehhMcShvqno3RXzCsyE25nfFA"
OWNER_ID = "boif3x"


def get_latest_post():
    url = f"https://api.vk.com/method/wall.get?owner_id={OWNER_ID}&count=10&access_token={ACCESS_TOKEN}&v=5.131"

    try:
        response = requests.get(url).json()

        if 'response' in response and 'items' in response['response'] and len(response['response']['items']) > 0:
            # Перебираем все посты и ищем тот, где есть ссылка на Google форму
            for post in response['response']['items']:
                post_text = post.get('text', '')

                # Ищем ссылку на Google форму в тексте поста
                form_link = re.search(r'https://(?:forms\.gle/\S+|docs\.google\.com/forms/d/e/\S+/viewform\S*)', post_text)

                # Проверяем вложения на наличие ссылки
                link_from_attachment = None
                if 'attachments' in post:
                    for attachment in post['attachments']:
                        if attachment['type'] == 'link':
                            url = attachment['link'].get('url', '')
                            if 'docs.google.com/forms' in url or 'forms.gle' in url:
                                link_from_attachment = url
                                break

                # Если ссылка найдена, возвращаем текст поста и ссылку на форму
                if form_link:
                    return post_text, form_link.group(0)
                elif link_from_attachment:
                    return post_text, link_from_attachment

            print("Не найдено постов с ссылкой на форму.")
            return None, None

        else:
            print("Нет доступных постов.")
            return None, None

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API ВКонтакте: {e}")
        return None, None
    except KeyError as e:
        print(f"Ошибка в структуре ответа: {e}")
        return None, None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None, None
