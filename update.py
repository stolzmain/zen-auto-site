import pandas as pd
import requests

# Твоя ссылка на CSV из Google Таблицы
SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRfhXLxZkje5vR1AZhCHMHTQiwr8ZDlKSVmcNmnNpr2kW5WCkBrWjYbqMDQkWg6Gj3d3oEiTUA26jz/pub?output=csv"

def build_site():
    print("Начинаю сборку сайта...")
    try:
        # 1. Пытаемся прочитать таблицу
        df = pd.read_csv(SHEET_CSV_URL)
        
        # Очищаем названия колонок от лишних пробелов (на всякий случай)
        df.columns = df.columns.str.strip()
        
        # 2. Формируем HTML-код страницы
        html = "<!DOCTYPE html><html lang='ru'><head><meta charset='UTF-8'>"
        html += "<title>hesay.ru — Блог</title>"
        html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        html += "<style>body{font-family:sans-serif;max-width:800px;margin:40px auto;padding:20px;line-height:1.6;}"
        html += "h1{border-bottom:2px solid #eee;padding-bottom:10px;}"
        html += "ul{list-style:none;padding:0;} li{margin-bottom:30px;}"
        html += "a{color:#1a73e8;text-decoration:none;font-weight:bold;font-size:1.2em;}"
        html += "a:hover{text-decoration:underline;} p{color:#555;margin:5px 0;}</style>"
        html += "</head><body>"
        html += "<h1>Последние статьи</h1><ul>"
        
        # 3. Перебираем строки таблицы
        for _, row in df.iterrows():
            # Метод .get помогает не падать, если колонка названа чуть иначе
            title = str(row.get('Заголовок', 'Без названия'))
            link = str(row.get('Ссылка', '#'))
            desc = str(row.get('Анонс', ''))
            
            html += f"<li>"
            html += f"<a href='{link}' target='_blank'>{title}</a>"
            html += f"<p>{desc}</p>"
            html += f"</li>"
        
        html += "</ul></body></html>"
        
        # 4. Записываем итоговый файл
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Файл index.html успешно создан из данных таблицы.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        # В случае ошибки создаем файл-оповещение, чтобы FTP не выдал ошибку пустого локального каталога
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(f"<html><body><h1>Сайт в процессе обновления</h1><p>Техническая ошибка: {e}</p></body></html>")
        print("Создан аварийный index.html")

if __name__ == "__main__":
    build_site()
