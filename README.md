# Telegram Weather Bot

Этот репозиторий содержит пример Telegram-бота, который выдаёт прогноз погоды на неделю по данным Яндекс.Погоды.

## Настройка

1. Сгенерируйте токен Telegram-бота через [@BotFather](https://t.me/BotFather).
2. Получите ключ API Яндекс.Погоды в [личном кабинете разработчика](https://developer.tech.yandex.ru/).
3. Экспортируйте переменные окружения `TELEGRAM_TOKEN` и `YANDEX_API_KEY` со своими значениями:

```bash
export TELEGRAM_TOKEN=ВАШ_ТЕЛЕГРАМ_ТОКЕН
export YANDEX_API_KEY=ВАШ_API_КЛЮЧ
```

4. Установите зависимости:

```bash
pip install python-telegram-bot requests
```

5. Запустите бота:

```bash
python bot.py
```

После запуска отправьте боту название города, и он ответит прогнозом погоды на неделю.

## Создание deb-пакета

Для сборки deb-пакета выполните:

```bash
bash build_deb.sh
```

Файл `build/telegram-weather-bot.deb` можно установить командой:

```bash
sudo dpkg -i build/telegram-weather-bot.deb
```
