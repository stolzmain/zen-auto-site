import pandas as pd

def build_site():
    try:
        # Читаем данные
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        
        html = "<!DOCTYPE html><html lang='ru'><head><meta charset='UTF-8'>"
        html += "<title>hesay.ru — Статьи</title>"
        html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        html += "<style>body{font-family:sans-serif; max-width:700px; margin:40px auto; padding:20px; line-height:1.6; color:#333;}"
        html += "h1{border-bottom: 2px solid #000; padding-bottom: 10px; margin-bottom: 30px;}"
        html += "ul{list-style:none; padding:0;} li{margin-bottom:50px; border-bottom:1px solid #eee; padding-bottom:30px;}"
        html += ".title{color:#000; text-decoration:none; font-size:1.4em; font-weight:bold; display:block; margin-bottom:10px;}"
        html += "</style></head><body>"
        html += "<h1>Статьи в Дзене</h1><ul>"
        
        for _, row in df.iterrows():
            title = str(row.get('Заголовок', 'Без названия'))
            link = str(row.get('Ссылка', '#'))
            desc = str(row.get('Анонс', ''))
            
            # Стили кнопки вынесены прямо в тег для надежности
            btn_style = "display:inline-block; padding:10px 20px; background-color:#d32f2f; color:#fff; text-decoration:none; border-radius:5px; font-weight:bold; margin-top:10px;"
            
            html += f"<li>"
            html += f"<a href='{link}' class='title' target='_blank'>{title}</a>"
            html += f"<p>{desc}</p>"
            html += f"<a href='{link}' target='_blank' style='{btn_style}'>Читать далее →</a>"
            html += f"</li>"
        
        html += "</ul></body></html>"
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Файл index.html обновлен. Кнопка теперь со встроенными стилями.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    build_site()
