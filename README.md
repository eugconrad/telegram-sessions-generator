# 📇 Telegram sessions generator
<img src="https://i.imgur.com/b5HoydJ.jpeg"></img>  

<div align="center">

  <a href="https://img.shields.io/github/repo-size/Conradk10/telegram-sessions-generator" alt="GitHub repo size"><img src="https://img.shields.io/github/repo-size/Conradk10/telegram-sessions-generator" /></a>
  <a href="https://img.shields.io/github/issues/Conradk10/telegram-sessions-generator" alt="GitHub issues"><img src="https://img.shields.io/github/issues/Conradk10/telegram-sessions-generator" /></a>
  <a href="https://img.shields.io/github/license/Conradk10/telegram-sessions-generator" alt="GitHub"><img src="https://img.shields.io/github/license/Conradk10/telegram-sessions-generator" /></a>

</div>

- Скрипт для генерации сессий (файлов с расширением .session) для использования в других моих проектах с библиотекой Telethon
## 💡 Обосенности:
- Неограниченное количество созданий сессий без необходимости перезапуска скрипта
## 🛠 Установка:
1. Клонируем репозиторий   
`git clone https://github.com/Conradk10/telegram-sessions-generator.git`   
2. Переходим в директорию  
`cd telegram-sessions-generator`  
3. Создаем виртуальное окружение   
`python3 -m venv env`   
4. Активируем виртуальное окружение   
`source env/bin/activate`   
5. Устанавливаем зависимости   
`python3 -m pip install -r requirements.txt`
## ⚙️ config.py
- Получение `API_ID` и `API_HASH` из `config.py`   
1. Для начала нужно перейти по <a href="https://my.telegram.org/apps">этой</a> или <a href=https://my.telegram.org/auth>этой</a> ссылке   
2. Ввести номер телефона и нажать `API development tools`   
3. Создать приложение заполнив данные на свое усмотрение (если не создано ранее)  
4. Скопировать `App api_id` и `App api_hash` и заменить в файле `config.py` соответствующие переменные новыми значениями
- `SESSIONS_DIR` отвечает за директорию с файлами сессий (`*.session`)   
## ▶️ Запуск:
Запускаем скрипта осуществляем с активированным виртуальным окружением с помощью команды   
`python3 main.py`
## 📝 Зависимости:
```
hikka-tl==1.24.10
loguru==0.6.0
```
