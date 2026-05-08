import pandas as pd
import requests

# ВСТАВЬТЕ ВАШУ ССЫЛКУ МЕЖДУ КАВЫЧЕК
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRfhXLxZKje5vR1AZhHCMHTQiWr8ZDlKSCvmcNmnNpr2kW5wCKbRWjYbQMdQKWg6Gj3d3oEItUA26jz/pub?output=csv"

def build_site():
    try:
        # Читаем данные
        df = pd.read_csv(SHEET_CSV_URL)
        
        # Начало HTML файла
        html = "<!DOCTYPE html><html lang='ru'><head><meta charset='UTF-8'>"
        html += "<title>hesay.ru — Обзоры и статьи</title>"
        html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        html += "</head><body style='font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px;'>"
        html += "<h1>Последние публикации</h1><hr><ul>"
        
        for _, row in df.iterrows():
            # Заменяем пустые значения на пустую строку, если они есть
            title = str(row['Заголовок'])
            link = str(row['Ссылка'])
            desc = str(row['Анонс'])
            
            html += f"<li style='margin-bottom: 30px;'>"
            html += f"<h2><a href='{link}' style='text-decoration: none; color: #1a73e8;'>{title}</a></h2>"
            html += f"<p style='color: #444; line-height: 1.6;'>{desc}</p>"
            html += f"</li>"
        
        html += "</ul></body></html>"
        
        # Сохраняем файл локально в репозитории
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Файл index.html успешно создан")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    build_site()
