import pandas as pd
from datetime import datetime

def build_site():
    try:
        # 1. Читаем данные из CSV
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        
        # Оптимизированный набор тем
        TAGS = ["бизнес", "финансы", "инвестиции", "психология", "криптовалюта", "трейдинг"]
        
        # SEO настройки
        SITE_TITLE = "hesay.ru — Бизнес, Финансы и Трейдинг"
        SITE_DESC = "Обзоры рынков, стратегии инвестирования и психология успеха. Свежие статьи из Дзена 4 раза в день."
        SITE_KEYWORDS = ", ".join(TAGS)
        
        # 2. Генерируем index.html
        html = "<!DOCTYPE html><html lang='ru'><head><meta charset='UTF-8'>"
        html += f"<title>{SITE_TITLE}</title>"
        html += f"<meta name='description' content='{SITE_DESC}'>"
        html += f"<meta name='keywords' content='{SITE_KEYWORDS}'>"
        html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        html += "<link rel='icon' href='favicon.ico' type='image/x-icon'>"
        
        # СТИЛИ
        html += "<style>"
        html += "body{font-family:sans-serif; max-width:750px; margin:40px auto; padding:20px; line-height:1.6; color:#333; background:#f0f2f5;}"
        html += ".container{background:#fff; padding:35px; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.08);}"
        html += "h1{margin-top:0; font-size:2.2em; color:#1a1a1a;}"
        html += ".tags-cloud{margin-bottom:30px; display:flex; flex-wrap:wrap; gap:8px; border-bottom:1px solid #eee; padding-bottom:20px;}"
        html += ".tag{background:#e8f0fe; color:#1967d2; padding:4px 12px; border-radius:15px; font-size:0.85em; font-weight:500; text-transform:lowercase;}"
        html += "ul{list-style:none; padding:0;} li{margin-bottom:45px; position:relative;}"
        html += "a.title{color:#000; text-decoration:none; font-size:1.4em; font-weight:bold; display:block; margin-bottom:12px; line-height:1.3;}"
        html += "a.title:hover{color:#d32f2f;}"
        html += "p{color:#555; font-size:1.05em;}"
        html += ".read-more{display:inline-block; margin-top:10px; color:#d32f2f; text-decoration:none; font-weight:bold; border:2px solid #d32f2f; padding:6px 18px; border-radius:6px; transition:0.3s;}"
        html += ".read-more:hover{background:#d32f2f; color:#fff;}"
        html += "footer{margin-top:60px; padding-top:25px; border-top:2px solid #eee;}"
        html += ".footer-links{display:flex; gap:15px; flex-wrap:wrap; margin-top:15px;}"
        html += ".footer-btn{background:#444; color:#fff; padding:10px 20px; text-decoration:none; border-radius:8px; font-size:0.9em; transition:0.2s;}"
        html += ".footer-btn:hover{background:#000;}"
        html += "</style></head><body>"
        
        html += "<div class='container'>"
        html += "<h1>Статьи в Дзене</h1>"
        
        # БЛОК ХЕШТЕГОВ (ОПТИМИЗИРОВАННЫЙ)
        html += "<div class='tags-cloud'>"
        for tag in TAGS:
            html += f"<span class='tag'>#{tag}</span>"
        html += "</div>"
        
        html += "<ul>"
        for _, row in df.iterrows():
            title = str(row.get('Заголовок', ''))
            link = str(row.get('Ссылка', '#'))
            desc = str(row.get('Анонс', ''))
            if title:
                html += f"<li>"
                html += f"<a href='{link}' class='title' target='_blank'>{title}</a>"
                html += f"<p>{desc}</p>"
                html += f"<a href='{link}' class='read-more' target='_blank'>Читать полностью →</a>"
                html += f"</li>"
        html += "</ul>"
        
        # ФУТЕР
        html += "<footer>"
        html += "<strong>Другие тематические каналы:</strong>"
        html += "<div class='footer-links'>"
        html += "<a href='https://dzen.ru/mindbug' class='footer-btn' target='_blank'>🧠 Психология</a>"
        html += "<a href='https://dzen.ru/2mom' class='footer-btn' target='_blank'>🤱 Мамам</a>"
        html += "</div>"
        html += "</footer>"
        
        html += "</div></body></html>"
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        
        # Генерируем Sitemap
        now = datetime.now().strftime('%Y-%m-%d')
        sitemap = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://hesay.ru/</loc><lastmod>{now}</lastmod><changefreq>hourly</changefreq><priority>1.0</priority></url></urlset>'
        with open("sitemap.xml", "w", encoding="utf-8") as f:
            f.write(sitemap)
            
        print("Сайт и Sitemap успешно обновлены!")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    build_site()
