import pandas as pd

def build_site():
    try:
        # Читаем данные
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        
        html = "<!DOCTYPE html><html lang='ru'><head><meta charset='UTF-8'>"
        html += "<title>hesay.ru — Статьи в Дзене</title>"
        html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        html += "<style>body{font-family:sans-serif; max-width:700px; margin:40px auto; padding:20px; line-height:1.6; color:#333;}"
        html += "h1{border-bottom: 2px solid #000; padding-bottom: 10px;}"
        html += "ul{list-style:none; padding:0;} li{margin-bottom:40px; border-bottom:1px solid #eee; padding-bottom:20px;}"
        html += "a.title{color:#000; text-decoration:none; font-size:1.4em; font-weight:bold;}"
        html += "a.title:hover{color:#d32f2f;}"
        html += ".read-more{display:inline-block; margin-top:10px; color:#d32f2f; text-decoration:none; font-weight:bold; border:1px solid #d32f2f; padding:5px 15px; border-radius:5px;}"
        html += ".read-more:hover{background:#d32f2f; color:#fff;}</style>"
        html += "</head><body>"
        html += "<h1>Статьи в Дзене</h1><ul>"
        
        for _, row in df.iterrows():
            title = str(row.get('Заголовок', 'Без названия'))
            link = str(row.get('Ссылка', '#'))
            desc = str(row.get('Анонс', ''))
            
            html += f"<li>"
            html += f"<a href='{link}' class='title' target='_blank'>{title}</a>"
            html += f"<p>{desc}</p>"
            # ВОТ ОНА — КНОПКА «ЧИТАТЬ ДАЛЕЕ»
            html += f"<a href='{link}' class='read-more' target='_blank'>Читать далее →</a>"
            html += f"</li>"
        
        html += "</ul></body></html>"
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Файл index.html успешно обновлен с кнопками!")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    build_site()
