# Upbit Listing Watcher Bot 🤖

Бот следит за появлением новых монет в KRW-парах на Upbit и отправляет уведомления в Telegram.

## Установка

1. Установите Python 3.11
2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Укажите свой `TOKEN` и `CHAT_ID` в `bot.py`
4. Запустите:

```bash
python bot.py
```

Бот каждые 5 минут проверяет API Upbit и каждые 5 часов сообщает, что он активен.
