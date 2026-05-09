import pandas as pd
from datetime import datetime

def build_site():
    try:
        # 1. Читаем данные из CSV
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        
        # Теги, которые чаще всего ищут новички
        TAGS = ["японские свечи", "графический анализ", "основы трейдинга", "психология", "криптовалюта"]
        
        # Название сайта как справочника
        SITE_TITLE = "Жить стабильно — Азбука начинающего трейдера и база знаний"
        PAGE_H1 = "Азбука трейдинга: база знаний для начинающих"
        
        # Описание (SITE_DESC) — бьем точно в запросы новичков
        SITE_DESC = "Понятный справочник по трейдингу для новичков. Учимся читать японские свечи, разбираем графический анализ и психологию рынка простыми словами без лишней воды."
        
        # Ключевые слова (SITE_KEYWORDS) — запросы, которые люди вбивают в поиск
        SITE_KEYWORDS = "трейдинг для начинающих, как читать японские свечи, графический анализ с нуля, основы биржевой торговли, база знаний трейдера, азбука инвестирования"
        SITE_URL = "https://hesay.ru/"
        
        # 2. Генерируем index.html
        html = "<!DOCTYPE html><html lang='ru' prefix='og: http://ogp.me/ns#'><head><meta charset='UTF-8'>"
        
        # Защита от кэширования
        html += "<meta http-equiv='cache-control' content='no-cache'><meta http-equiv='expires' content='0'>"
        
        # Базовое SEO
        html += f"<title>{SITE_TITLE}</title>"
        html += f"<meta name='description' content='{SITE_DESC}'>"
        html += f"<meta name='keywords' content='{SITE_KEYWORDS}'>"
        html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        html += f"<link rel='canonical' href='{SITE_URL}'>"
        
        # Open Graph
        html += f"<meta property='og:title' content='{SITE_TITLE}'>"
        html += f"<meta property='og:description' content='{SITE_DESC}'>"
        html += f"<meta property='og:url' content='{SITE_URL}'>"
        html += "<meta property='og:type' content='website'>"
        
        # Фавикон
        html += "<link rel='icon' href='favicon.ico' type='image/x-icon'>"
        # Ссылка на RSS ленту (теперь браузеры увидят значок подписки)
        html += f"<link rel='alternate' type='application/rss+xml' title='RSS лента {SITE_TITLE}' href='{SITE_URL}rss.xml'>"
        # Стили (Исправлены для отображения футера)
        html += """
        <style>
            body{font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width:920px; margin:40px auto; padding:20px; line-height:1.6; color:#333; background:#f0f2f5;}
            .container{background:#fff; padding:20px 35px 35px 35px; border-radius:0 0 12px 12px; box-shadow:0 4px 15px rgba(0,0,0,0.08); margin-top: -20px; position: relative; z-index: 1;}
            h1{margin-top:0; font-size:2.1em; color:#1a1a1a; border-bottom: 3px solid #d32f2f; padding-bottom: 10px;}
            .tags-cloud{margin:20px 0 30px 0; display:flex; flex-wrap:wrap; gap:8px;}
            .tag{background:#e8f0fe; color:#1967d2; padding:4px 12px; border-radius:15px; font-size:0.85em; font-weight:500;}
            ul{list-style:none; padding:0;} 
            li{margin-bottom:45px; border-bottom:1px solid #f0f0f0; padding-bottom:30px;}
            a.title{color:#000; text-decoration:none; font-size:1.4em; font-weight:bold; display:block; margin-bottom:12px;}
            a.title:hover{color:#d32f2f;}
            .read-more{display:inline-block; margin-top:10px; color:#d32f2f; text-decoration:none; font-weight:bold; border:2px solid #d32f2f; padding:6px 18px; border-radius:6px;}
            
            /* Стили футера - ГАРАНТИРОВАННАЯ ВИДИМОСТЬ */
            .footer-section{padding: 25px 35px; background: #fff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); margin-top: 20px; display: block !important;}
            .footer-links{display: flex; gap: 12px; flex-wrap: wrap; margin-top: 15px; visibility: visible !important;}
            .footer-btn{background: #222; color: #fff !important; padding: 12px 20px; text-decoration: none; border-radius: 8px; font-size: 0.9em; font-weight: bold; display: inline-block !important; transition: 0.2s;}
            .footer-btn:hover{background: #d32f2f; color: #fff !important;}
        </style>
        """
        
        html += "</head><body>"

        # Обновленный блок информера: Исправлены скругления углов
        html += """
        <div style="background: #1a1a1a; color: #fff; padding: 15px 0 10px 0; text-align: center; font-size: 0.9em; border-radius: 12px 12px 0 0; border-bottom: 1px solid #333; margin-bottom: -1px; position: relative; z-index: 2;">
            <div id="btc-price-container" style="margin-bottom: 7px; font-weight: 500;">
                ₿ Bitcoin (BTC): <span id="btc-price" style="color: #f2a900; font-weight: bold;">Загрузка...</span>
            </div>
            <div style="font-size: 0.85em; color: #bbb;">
                📢 Активных подписчиков по RSS: <span style="color: #fff; font-weight: bold;">14 796</span> 
                | <a href="/rss.xml" target="_blank" style="color: #d32f2f; text-decoration: none; font-weight: bold; border-bottom: 1px dashed #d32f2f;">[ Подписаться ]</a>
            </div>
        </div>
        
        <script>
            async function getBTCPrice() {
                try {
                    const response = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd');
                    const data = await response.json();
                    const price = data.bitcoin.usd;
                    const formattedPrice = new Intl.NumberFormat('en-US', { 
                        style: 'currency', 
                        currency: 'USD' 
                    }).format(price);
                    document.getElementById('btc-price').innerText = formattedPrice;
                } catch (error) {
                    document.getElementById('btc-price').innerText = 'обновляется...';
                }
            }
            getBTCPrice();
            setInterval(getBTCPrice, 60000);
        </script>
        """
        
        # Основной блок со статьями
        html += "<div class='container'>"
        html += f"<h1>{PAGE_H1}</h1>"
        html += "<div class='tags-cloud'>"
        for tag in TAGS:
            html += f"<span class='tag'>#{tag}</span>"
        html += "</div><ul>"
        
        for _, row in df.iterrows():
            title = str(row.get('Заголовок', ''))
            link = str(row.get('Ссылка', '#'))
            desc = str(row.get('Анонс', ''))
            if title:
                html += f"<li><a href='{link}' class='title' target='_blank'>{title}</a>"
                html += f"<p>{desc}</p>"
                html += f"<a href='{link}' class='read-more' target='_blank'>Читать полностью →</a></li>"
        
        html += "</ul></div>" # Закрываем container
        
        # Отдельный блок футера (Другие проекты)
        html += "<div class='footer-section'>"
        html += "<strong>Другие проекты:</strong>"
        html += "<div class='footer-links'>"
        html += "<a href='https://dzen.ru/mindbug' class='footer-btn' target='_blank'>🧠 Психология</a>"
        html += "<a href='https://dzen.ru/2mom' class='footer-btn' target='_blank'>🤱 Мамам</a>"
        html += "</div></div>"
        
        html += "</body></html>"
        
        # Сохранение index.html
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

        # 3. Sitemap.xml
        now = datetime.now().strftime('%Y-%m-%d')
        sitemap_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{SITE_URL}</loc>
    <lastmod>{now}</lastmod>
    <changefreq>hourly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>'''
        with open("sitemap.xml", "w", encoding="utf-8") as f:
            f.write(sitemap_content)

       # 4. Robots.txt
        robots_content = f'''User-agent: *
Allow: /
Sitemap: {SITE_URL}sitemap.xml
RSS: {SITE_URL}rss.xml

User-agent: Googlebot
Allow: /

User-agent: Yandex
Allow: /
Clean-param: share_to
'''
        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write(robots_content)

        # 5. Генерация RSS-ленты (rss.xml)
        rss_items = ""
        # Берем данные для ленты (последние 50 статей)
        for _, row in df.head(50).iterrows():
            # Очищаем текст от символов, которые ломают XML
            title = str(row.get('Заголовок', '')).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            link = str(row.get('Ссылка', '#'))
            desc = str(row.get('Анонс', '')).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            
            rss_items += f"""
        <item>
            <title>{title}</title>
            <link>{link}</link>
            <description>{desc}</description>
            <pubDate>{datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0300')}</pubDate>
            <guid isPermaLink="false">{link}</guid>
        </item>"""

        rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
    <title>{SITE_TITLE}</title>
    <link>{SITE_URL}</link>
    <description>{SITE_DESC}</description>
    <language>ru</language>
    <atom:link href="{SITE_URL}rss.xml" rel="self" type="application/rss+xml" />
    {rss_items}
</channel>
</rss>"""

        with open("rss.xml", "w", encoding="utf-8") as f:
            f.write(rss_content)
            
        print("Сайт успешно обновлен, RSS и SEO оптимизированы!")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    build_site()
