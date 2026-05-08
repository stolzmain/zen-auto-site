import pandas as pd
import os

# Твоя ссылка на CSV из Google Таблицы
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRfhXLxZkje5vR1AZhCHMHTQiwr8ZDlKSVmcNmnNpr2kW5WCkBrWjYbqMDQkWg6Gj3d3oEiTUA26jz/pub?output=csv"

def build_site():
    try:
        # Читаем таблицу
        df = pd.read_csv(SHEET_CSV_URL)
        
        # Убираем пробелы из названий колонок на случай случайных ошибок
        df.columns = df.columns.str.strip()
        
        # Формируем чистый HTML
        html = "<!DOCTYPE html><html lang='ru'><head><meta charset='UTF-8'>"
        html += "<title>hesay.ru — Мой Блог</title>"
        html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        html += "</head><body style='font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; line-height: 1.6;'>"
        html += "<h1>Последние статьи</h1><hr><ul>"
        
        for _, row in df.iterrows():
            # Безопасное получение данных из колонок
            title = str(row.get('Заголовок', 'Без названия'))
            link = str(row.get('Ссылка', '#'))
            desc = str(row.get('Анонс', ''))
            
            html += f"<li style='margin-bottom: 25px; list-style: none;'>"
            html += f"<h2><a href='{link}' style='color: #007bff; text-decoration: none;'>{title}</a></h2>"
            html += f"<p style='color: #555;'>{desc}</p>"
            html += f"</li>"
        
        html += "</ul></body></html>"
        
        # Записываем файл
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
            
        print("Файл index.html успешно создан в корне репозитория")
        
    except Exception as e:
        print(f"Ошибка при создании HTML: {e}")

if __name__ == "__main__":
    build_site()
