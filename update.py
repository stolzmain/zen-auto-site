import pandas as pd

def build_site():
    try:
        # Читаем файл из этой же папки
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        
        html = "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>hesay.ru</title></head>"
        html += "<body style='font-family:sans-serif; max-width:600px; margin:auto; padding:20px;'>"
        html += "<h1>Статьи в Дзене</h1><ul>"
        
        for _, row in df.iterrows():
            html += f"<li><a href='{row['Ссылка']}'><b>{row['Заголовок']}</b></a><p>{row['Анонс']}</p></li>"
        
        html += "</ul></body></html>"
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Файл index.html создан из data.csv")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    build_site()
