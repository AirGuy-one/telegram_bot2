# Бот, который умеет распознавать речь

## Чтобы запустить telegram бота, необходимо:

1. Создайте файл .env по следующему примеру:
```
TG_BOT_TOKEN='12345798:HGUygugUguGuyGuyguGOguygYugyugbhfd'
USER_TG_CHAT_ID=123456789
GOOGLE_APPLICATION_CREDENTIALS='some_nameUBUguGyubbO.json'
DIALOG_FLOW_PROJECT_ID='name_of_project'
```
2. Установите зависимости
```sh
pip install -r requirements.txt
```
3. Запустить файл локально, выпонив команду
```sh
python3 tg_bot.py
```

## Чтобы запустить vk бота, необходимо:

1. Создайте файл .env по следующему примеру:
```
GOOGLE_APPLICATION_CREDENTIALS='some_nameUBUguGyubbO.json'
DIALOG_FLOW_PROJECT_ID='name_of_project'
VK_GROUP_TOKEN='token_of_your_group_in_vk'
```
2. Установите зависимости
```sh
pip install -r requirements.txt
```
3. Запустить файл локально, выпонив команду
```sh
python3 vk_bot.py
```

Dialogflow — это платформа от Google для понимания естественного языка, которую вы можете использовать для создания омниканальных чат-ботов.
