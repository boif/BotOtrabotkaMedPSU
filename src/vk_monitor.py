import requests
import re

ACCESS_TOKEN = "vk1.a.ZAbDb84oF69OQ7p23CF_VYDD2GdqOodFz7yqYKiOZWhJsc6syBFWVCWQFLtxByPkSzmJbpj5ulqZHkjf2rMJc6BM9mLHd78AK_yJXZQ0xlu4E5lRwx39YCorVE5oDIGyXuzwDQYRcR-agXXpkPtZS80GeNQkake4k__NZDsazuqW0YmSrdJnuQ6Dg8wXJZOOeifBRZ69FYYTN1nCK7rTHw&expires_in=86400"
OWNER_ID = "boif3x"


def get_latest_post():
    # Формируем URL для запроса
    url = f"https://api.vk.com/method/wall.get?owner_id={OWNER_ID}&count=1&access_token={ACCESS_TOKEN}&v=5.131"

    try:
        # Отправляем запрос
        response = requests.get(url).json()

        # Проверяем, есть ли посты в ответе
        if 'response' in response and 'items' in response['response'] and len(response['response']['items']) > 0:
            post_text = response['response']['items'][0]['text']
            # Ищем ссылку на Google форму в тексте поста
            form_link = re.search(r'(https://forms\.gle/\S+|https://docs\.google\.com/forms/d/e/\S+/viewform\S*)', post_text)
            return post_text, form_link.group(0) if form_link else None
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