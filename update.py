import pandas as pd
from datetime import datetime

def build_site():
    try:
        # 1. Читаем данные из CSV
        # Убедитесь, что файл data.csv лежит в той же папке
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        
        # Оптимизированный набор тем (хештеги)
        TAGS = ["бизнес", "финансы", "инвестиции", "психология", "криптовалюта", "трейдинг"]
        
        # SEO настройки
        SITE_TITLE = "Бизнес, Финансы и Трейдинг — аналитика и стратегии"
        PAGE_H1 = "Бизнес, финансы и трейдинг: аналитика"
        SITE_DESC = "Актуальные обзоры рынков, стратегии инвестирования и психология успеха. Свежие статьи 4 раза в день."
        SITE_KEYWORDS = ", ".join(TAGS) + ", аналитика рынка"
        
        # 2. Генерируем index.html
        html = "<!DOCTYPE html><html lang='ru'><head><meta charset='UTF-8'>"
        
        # Защита от кэширования (чтобы пользователи сразу видели новые статьи)
        html += "<meta http-equiv='cache-control' content='no-cache'>"
        html += "<meta http-equiv='expires' content='0'>"
        
        # Мета-теги для SEO и Яндекса
        html += f"<title>{SITE_TITLE}</title>"
        html += f"<meta name='description' content='{SITE_DESC}'>"
        html += f"<meta name='keywords' content='{SITE_KEYWORDS}'>"
        html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        html += "<meta name='robots' content='index, follow'>"
        
        # Фавикон (должен лежать в корне сайта)
        html += "<link rel='icon' href='favicon.ico' type='image/x-icon'>"
        
        # Стили оформления
        html += """
        <style>
            body{font-family:sans-serif; max-width:750px; margin:40px auto; padding:20px; line-height:1.6; color:#333; background:#f0f2f5;}
            .container{background:#fff; padding:35px; border-radius:12px; box-shadow:0 4px 15px rgba(0,0,0,0.08); margin-bottom: 20px;}
            h1{margin-top:0; font-size:2.1em; color:#1a1a1a; border-bottom: 2px solid #d32f2f; padding-bottom: 10px;}
            .tags-cloud{margin:20px 0 30px 0; display:flex; flex-wrap:wrap; gap:8px;}
            .tag{background:#e8f0fe; color:#1967d2; padding:4px 12px; border-radius:15px; font-size:0.85em; font-weight:500;}
            ul{list-style:none; padding:0;} 
            li{margin-bottom:45px; border-bottom:1px solid #f0f0f0; padding-bottom:30px;}
            a.title{color:#000; text-decoration:none; font-size:1.4em; font-weight:bold; display:block; margin-bottom:12px; transition: 0.2s;}
            a.title:hover{color:#d32f2f;}
            .read-more{display:inline-block; margin-top:10px; color:#d32f2f; text-decoration:none; font-weight:bold; border:2px solid #d32f2f; padding:6px 18px; border-radius:6px; transition: 0.3s;}
            .read-more:hover{background:#d32f2f; color:#fff;}
            .footer-section{padding: 25px 35px; background: #fff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08);}
            .footer-links{display:flex; gap:12px; flex-wrap:wrap; margin-top:15px;}
            .footer-btn{background:#222; color:#fff !important; padding:12px 20px; text-decoration:none; border-radius:8px; font-size:0.95em; font-weight:bold; transition: 0.2s;}
            .footer-btn:hover{background:#d32f2f;}
        </style>
        """
        
        html += "</head><body>"
        
        # Основной блок контента
        html += "<div class='container'>"
        html += f"<h1>{PAGE_H1}</h1>"
        
        # Облако тегов
        html += "<div class='tags-cloud'>"
        for tag in TAGS:
            html += f"<span class='tag'>#{tag}</span>"
        html += "</div><ul>"
        
        # Список статей
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
        
        html += "</ul></div>"
        
        # Футер с тематическими каналами
        html += "<div class='footer-section'>"
        html += "<strong>Другие тематические проекты:</strong>"
        html += "<div class='footer-links'>"
        html += "<a href='https://dzen.ru/mindbug' class='footer-btn' target='_blank'>🧠 Психология</a>"
        html += "<a href='https://dzen.ru/2mom' class='footer-btn' target='_blank'>🤱 Мамам</a>"
        html += "</div></div>"
        
        html += "</body></html>"
        
        # Записываем index.html
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Файл index.html обновлен.")

        # 3. Генерируем sitemap.xml автоматически
        now = datetime.now().strftime('%Y-%m-%d')
        sitemap_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://hesay.ru/</loc>
    <lastmod>{now}</lastmod>
    <changefreq>hourly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>'''
        with open("sitemap.xml", "w", encoding="utf-8") as f:
            f.write(sitemap_content)
        print(f"Sitemap обновлен: {now}")

        # 4. Генерируем robots.txt автоматически
        robots_content = f'''User-agent: *
Allow: /
Sitemap: https://hesay.ru/sitemap.xml

User-agent: Yandex
Allow: /
Clean-param: share_to
'''
        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write(robots_content)
        print("Файл robots.txt обновлен.")

    except Exception as e:
        print(f"Ошибка выполнения: {e}")

if __name__ == "__main__":
    build_site()
