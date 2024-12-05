import requests

# URL файла
url = "https://gbcdn.mrgcdn.ru/uploads/asset/6189865/attachment/e9ef150e280e5b181a9507ec02733aaf.ipynb"

# Скачивание файла
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Сохранение файла
    with open("downloaded_hw1.ipynb", "wb") as file:
        file.write(response.content)
    print("Файл успешно скачан и сохранен как 'downloaded_hw1.ipynb'.")
else:
    print("Ошибка при скачивании файла:", response.status_code)