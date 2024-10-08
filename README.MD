# VK Link Shortener

## Описание

VK Link Shortener — это приложение на Python, которое позволяет сокращать длинные ссылки с помощью API ВКонтакте и получать статистику кликов по сокращенным ссылкам. Приложение использует библиотеку `requests для выполнения HTTP-запросов и argparse` для обработки аргументов командной строки.

## Установка

Следуйте этим шагам, чтобы установить и запустить проект:

1. **Клонируйте репозиторий**:

Откройте терминал и выполните следующую команду:

```bash
git clone https://github.com/karaman56/VK-Link-Shortener.git
```

Перейдите в директорию проекта:

```bash
cd VK-Link-Shortener
```

2. **Установите необходимые зависимости**:

Убедитесь, что у вас установлен Python и pip. Затем выполните команду:

```bash
pip install -r requirements.txt
```

3. **Создайте файл `.env`**:

В корневом каталоге проекта создайте файл `.env` и добавьте ваш токен доступа VK:

```plaintext
VK_TOKEN=ваш_токен
```

Замените `ваш_токен` на ваш реальный токен доступа.

## Использование

Запустите скрипт с указанием длинной ссылки и (опционально) токена доступа:

```bash
python VK_LINK_SHORTERNER.py "https://example.com" --token "ваш_токен"
```

Если токен не указан, приложение будет использовать токен из переменной окружения `VK_TOKEN`.

### Примеры команд

1. **Сокращение ссылки**:

   Чтобы сократить длинную ссылку, выполните:

   ```bash
   python VK_LINK_SHORTERNER.py "https://www.example.com/very/long/url"
   ```

   После выполнения команды вы получите сокращенную ссылку.

2. **Получение статистики кликов по сокращенной ссылке**:

   Чтобы получить количество кликов по сокращенной ссылке, выполните:

   ```bash
   python VK_LINK_SHORTERNER.py "https://vk.cc/xyz123"
   ```

   Замените `https://vk.cc/xyz123` на вашу сокращенную ссылку.

## Проверка результата

После выполнения команд вы должны увидеть в консоли:

- Для сокращенной ссылки: сообщение с сокращенной ссылкой.
- Для статистики кликов: сообщение с количеством кликов.

Если вы видите эти сообщения, значит, все работает корректно.
