import requests
import re

ACCESS_TOKEN = "vk1.a.ZAbDb84oF69OQ7p23CF_VYDD2GdqOodFz7yqYKiOZWhJsc6syBFWVCWQFLtxByPkSzmJbpj5ulqZHkjf2rMJc6BM9mLHd78AK_yJXZQ0xlu4E5lRwx39YCorVE5oDIGyXuzwDQYRcR-agXXpkPtZS80GeNQkake4k__NZDsazuqW0YmSrdJnuQ6Dg8wXJZOOeifBRZ69FYYTN1nCK7rTHw&expires_in=86400"
OWNER_ID = "dr.yana_alexandrovna"


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


# Пример использования функции
post_text, google_form_link = get_latest_post()
if post_text:
    print("Текст поста:", post_text)
if google_form_link:
    print("Ссылка на форму Google:", google_form_link)
else:
    print("Ссылка на форму Google не найдена.")
