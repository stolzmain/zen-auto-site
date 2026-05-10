import pandas as pd
import requests
from datetime import datetime

def build_site():
    try:
        # 1. Данные и настройки
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        
        SITE_URL = "https://hesay.ru/"
        SITE_TITLE = "Жить стабильно — Азбука начинающего трейдера и база знаний"
        SITE_DESC = "Понятный справочник по трейдингу для новичков. Учимся читать японские свечи, разбираем графический анализ и психологию рынка простыми словами."
        SITE_KEYWORDS = "трейдинг для начинающих, как читать японские свечи, графический анализ, база знаний трейдера"
        INDEXNOW_KEY = "7252fab850c345419d3109a8f718aaad"

        # --- ЛОГИКА ПОСТЕПЕННОГО ВЫПУСКА ---
        # Точка отсчета (когда ты загрузила пачку статей)
        # Установили на 10 мая 2026, 20:00 (твое текущее время)
        START_DATE = datetime(2026, 5, 10, 20, 0) 
        HOURS_STEP = 2 # Выпускать по 1 новой статье каждые 2 часа
        
        # Считаем разницу во времени
        time_diff = datetime.now() - START_DATE
        hours_passed = time_diff.total_seconds() / 3600
        
        # Сколько строк из CSV уже можно показать (минимум 1)
        visible_count = max(1, int(hours_passed / HOURS_STEP) + 1)
        
        # Берем только разрешенные строки
        df_visible = df.head(visible_count)
        # -----------------------------------
        
        # 2. Формируем HTML
        html = f"<!DOCTYPE html><html lang='ru'><head><meta charset='UTF-8'>"
        html += f"<title>{SITE_TITLE}</title>"
        html += f"<meta name='description' content='{SITE_DESC}'>"
        html += f"<meta name='keywords' content='{SITE_KEYWORDS}'>"
        html += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"
        
        # Верификация поисковиков
        html += '<meta name="yandex-verification" content="1b5b4a95cfd80398" />'
        html += '<meta name="google-site-verification" content="gv-bcarlpcaxid5hp.dv.googlehosted.com" />'
        
        html += f"<link rel='canonical' href='{SITE_URL}'>"
        html += "<link rel='icon' href='favicon.ico' type='image/x-icon'>"
        html += f"<link rel='alternate' type='application/rss+xml' href='{SITE_URL}rss.xml'>"
        
        # Стили (1024px и стыковка блоков)
        html += """
        <style>
            body{font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width:1024px; margin:40px auto; padding:20px; line-height:1.6; color:#333; background:#f0f2f5;}
            .header-info {
                background: #1a1a1a; color: #fff; padding: 20px 0 15px 0; text-align: center; 
                font-size: 0.9em; border-radius: 12px 12px 0 0; border-bottom: 1px solid #333;
                position: relative; z-index: 2;
            }
            .container {
                background: #fff; padding: 35px; border-radius: 0 0 12px 12px; 
                box-shadow: 0 4px 15px rgba(0,0,0,0.08); margin-top: -1px; 
                position: relative; z-index: 1;
            }
            h1{margin-top:0; font-size:2.1em; color:#1a1a1a; border-bottom: 3px solid #d32f2f; padding-bottom: 10px;}
            ul{list-style:none; padding:0;} 
            li{margin-bottom:45px; border-bottom:1px solid #f0f0f0; padding-bottom:30px;}
            a.title{color:#000; text-decoration:none; font-size:1.4em; font-weight:bold; display:block; margin-bottom:12px;}
            .read-more{display:inline-block; margin-top:10px; color:#d32f2f; text-decoration:none; font-weight:bold; border:2px solid #d32f2f; padding:6px 18px; border-radius:6px;}
            .footer-section{padding: 25px 35px; background: #fff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); margin-top: 20px;}
            .footer-btn{background: #222; color: #fff !important; padding: 10px 18px; text-decoration: none; border-radius: 8px; font-weight: bold; margin-right: 10px; display: inline-block;}
        </style>
        """
        
        # Яндекс Метрика
        html += """
        <script type="text/javascript">
           (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};m[i].l=1*new Date();for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=105130661', 'ym');
           ym(105130661, 'init', {ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", accurateTrackBounce:true, trackLinks:true});
        </script>
        <noscript><div><img src="https://mc.yandex.ru/watch/105130661" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
        """
        
        html += "</head><body>"

        # Шапка с курсом и подписчиками
        html += f"""
        <div class="header-info">
            <div id="btc-price-container" style="margin-bottom: 7px;">
                ₿ Bitcoin (BTC): <span id="btc-price" style="color: #f2a900; font-weight: bold;">Загрузка...</span>
            </div>
            <div style="font-size: 0.85em; color: #bbb;">
                📢 Активных подписчиков по RSS: <span style="color: #fff; font-weight: bold;">14 799</span> 
                | <a href="/rss.xml" target="_blank" style="color: #d32f2f; text-decoration: none; font-weight: bold;">[ Подписаться ]</a>
            </div>
        </div>
        <script>
            async function getPrice(){{
                try{{
                    const r = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd');
                    const d = await r.json();
                    document.getElementById('btc-price').innerText = new Intl.NumberFormat('en-US',{{style:'currency',currency:'USD'}}).format(d.bitcoin.usd);
                }}catch(e){{document.getElementById('btc-price').innerText = 'обновляется...';}}
            }}
            getPrice(); setInterval(getPrice, 60000);
        </script>
        """

        html += "<div class='container'>"
        html += f"<h1>Азбука трейдинга: база знаний</h1><ul>"
        
        # Выводим только видимые статьи
        for _, row in df_visible.iterrows():
            t, l, d = str(row.get('Заголовок','')), str(row.get('Ссылка','#')), str(row.get('Анонс',''))
            if t:
                html += f"<li><a href='{l}' class='title' target='_blank'>{t}</a><p>{d}</p>"
                html += f"<a href='{l}' class='read-more' target='_blank'>Читать →</a></li>"
        
        html += "</ul></div>"
        html += "<div class='footer-section'><strong>Проекты:</strong><div style='margin-top:15px;'>"
        html += "<a href='https://dzen.ru/mindbug' class='footer-btn'>🧠 Психология</a>"
        html += "<a href='https://dzen.ru/2mom' class='footer-btn'>🤱 Мамам</a>"
        html += "</div></div></body></html>"
        
        with open("index.html", "w", encoding="utf-8") as f: f.write(html)

        # 3. Технические файлы (Sitemap, RSS, Robots)
        s_now = datetime.now().strftime('%Y-%m-%d')
        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\nRSS: {SITE_URL}rss.xml")

        # Sitemap (только для видимых страниц)
        sitemap_content = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE_URL}</loc><lastmod>{s_now}</lastmod><changefreq>hourly</changefreq><priority>1.0</priority></url></urlset>'
        with open("sitemap.xml", "w", encoding="utf-8") as f: f.write(sitemap_content)

        # RSS (только для видимых страниц)
        rss_items = ""
        for _, row in df_visible.head(50).iterrows():
            clean_t = str(row.get('Заголовок','')).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
            rss_items += f"<item><title>{clean_t}</title><link>{row.get('Ссылка')}</link><description>{row.get('Анонс')}</description></item>"
        
        with open("rss.xml", "w", encoding="utf-8") as f:
            f.write(f'<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0"><channel><title>{SITE_TITLE}</title><link>{SITE_URL}</link>{rss_items}</channel></rss>')

        # 4. Уведомление Bing (IndexNow)
        requests.post("https://www.bing.com/indexnow", json={
            "host": "hesay.ru",
            "key": INDEXNOW_KEY,
            "keyLocation": f"{SITE_URL}{INDEXNOW_KEY}.txt",
            "urlList": [SITE_URL]
        })
        
        print(f"Сайт обновлен! Сейчас опубликовано статей: {len(df_visible)}")

    except Exception as e: print(f"Ошибка: {e}")

if __name__ == "__main__": build_site()
