# Бот, который умеет распознавать речь

![gif](bot_interaction.gif)

## Чтобы запустить бота, необходимо:

1. Создайте файл .env по следующему примеру:
```
TG_BOT_TOKEN='12345798:HGUygugUguGuyGuyguGOguygYugyugbhfd'
USER_TG_CHAT_ID=123456789
GOOGLE_APPLICATION_CREDENTIALS='some_nameUBUguGyubbO.json'
DIALOG_FLOW_PROJECT_ID='name_of_project'
VK_GROUP_TOKEN='token_of_your_group_in_vk'
```
2. Возьмите в GOOGLE_APPLICATION_CREDENTIALS json файл со всеми данными, необходимыми для работы с api и скопируйте его себе в репозиторий.
3. Установите зависимости
```sh
pip install -r requirements.txt
```
4. Запустить телеграмм локально, выпонив команду
```sh
python3 tg.py
```
или vk бота, выполнив каманду
```sh
python3 vk.py
```


Dialogflow — это платформа от Google для понимания естественного языка, которую вы можете использовать для создания омниканальных чат-ботов.
