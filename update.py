import pandas as pd
import requests
from datetime import datetime

def build_site():
    try:
        # 1. Данные и настройки
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        
        SITE_URL = "https://stolzmain.github.io/hesay/"
        SITE_TITLE = "Жить стабильно — Азбука начинающего трейдера и база знаний"
        SITE_DESC = "Понятный справочник по трейдингу для новичков. Учимся читать японские свечи, разбираем графический анализ и психологию рынка."
        SITE_KEYWORDS = "трейдинг для начинающих, как читать японские свечи, графический анализ, база знаний трейдера"
        INDEXNOW_KEY = "7252fab850c345419d3109a8f718aaad"

        # --- НАСТРОЙКА ОЧЕРЕДИ ---
        # 90 статей публикуются сразу, последующие (92-я строка в CSV и далее) — каждые 2 часа
        INITIAL_COUNT = 90 
        START_DATE = datetime(2026, 5, 10, 21, 0) 
        HOURS_STEP = 2 
        
        # Расчет текущего шага очереди
        time_diff = datetime.now() - START_DATE
        hours_passed = max(0, time_diff.total_seconds() / 3600)
        new_articles_count = int(hours_passed / HOURS_STEP)
        
        visible_count = INITIAL_COUNT + new_articles_count
        
        # Берем строки и переворачиваем (самые новые — всегда сверху)
        df_visible = df.head(visible_count).iloc[::-1]
        # ---------------------------
        
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
        
        # СТИЛИ (Таймлайн, 1024px и адаптивность под мобильные)
        html += """
        <style>
            body{font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width:1024px; margin:40px auto; padding:20px; line-height:1.6; color:#333; background:#f0f2f5;}
            .header-info {
                background: #1a1a1a; color: #fff; padding: 25px 0; text-align: center; 
                border-radius: 12px 12px 0 0; position: relative; z-index: 2;
            }
            .container {
                background: #fff; padding: 40px 60px; border-radius: 0 0 12px 12px; 
                box-shadow: 0 4px 15px rgba(0,0,0,0.08); position: relative; z-index: 1;
            }
            h1{margin-top:0; font-size:2.2em; color:#1a1a1a; border-bottom: 3px solid #d32f2f; padding-bottom: 15px; margin-bottom: 40px;}
            
            /* Линия таймлайна */
            .timeline {position: relative; padding-left: 40px; list-style: none;}
            .timeline::before {content: ''; position: absolute; left: 7px; top: 10px; bottom: 10px; width: 2px; background: #e0e0e0;}
            
            /* Элемент списка (пост) */
            .post-item {position: relative; margin-bottom: 50px;}
            
            /* Круглый маркер на линии */
            .post-item::before {
                content: ''; position: absolute; left: -40px; top: 8px; 
                width: 14px; height: 14px; background: #fff; 
                border: 3px solid #d32f2f; border-radius: 50%; z-index: 2;
            }
            
            .post-title {color: #000; text-decoration: none; font-size: 1.5em; font-weight: bold; display: block; margin-bottom: 10px; transition: 0.2s;}
            .post-title:hover {color: #d32f2f;}
            .post-desc {color: #555; font-size: 1.05em; margin-bottom: 15px;}
            
            .read-btn {display: inline-block; color: #d32f2f; text-decoration: none; font-weight: bold; border: 2px solid #d32f2f; padding: 8px 20px; border-radius: 8px; font-size: 0.9em; transition: 0.3s;}
            .read-btn:hover {background: #d32f2f; color: #fff;}

            /* Блок Вебмастерам */
            .webmaster-section {background: #fff; padding: 30px; border-radius: 12px; margin-top: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.08);}
            .wm-title {font-weight: bold; font-size: 0.9em; color: #777; margin-bottom: 15px; text-transform: uppercase;}
            .wm-grid {display: flex; flex-wrap: wrap; gap: 20px; align-items: center;}
            .wm-link {color: #444; text-decoration: none; font-size: 0.95em; display: flex; align-items: center; gap: 5px;}
            .wm-link:hover {text-decoration: underline;}
            
            /* Подвал с проектами */
            .footer-projects {padding: 25px 35px; background: #1a1a1a; color: #fff; border-radius: 12px; margin-top: 20px; display: flex; align-items: center; gap: 20px; flex-wrap: wrap;}
            .proj-btn {background: #333; color: #fff !important; padding: 8px 15px; text-decoration: none; border-radius: 6px; font-size: 0.85em; font-weight: bold;}
            
            @media (max-width: 768px) {
                .container {padding: 30px 20px;}
                .timeline {padding-left: 25px;}
                .timeline::before {left: 4px;}
                .post-item::before {left: -25px; width: 10px; height: 10px; border-width: 2px;}
                .post-title {font-size: 1.25em;}
            }
        </style>
        """
        
        # Яндекс Метрика
        html += """
        <script type="text/javascript">
           (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};m[i].l=1*new Date();for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=105130661', 'ym');
           ym(105130661, 'init', {ssr:true, webvisor:true, clickmap:true, accurateTrackBounce:true, trackLinks:true});
        </script>
        <noscript><div><img src="https://mc.yandex.ru/watch/105130661" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
        """
        
        html += "</head><body>"

        # Шапка с курсом, RSS, Дзеном и RuTube
        html += f"""
        <div class="header-info">
            <div id="btc-price" style="color: #f2a900; font-weight: bold; font-size: 1.2em;">₿ Bitcoin (BTC): Загрузка...</div>
            <div style="font-size: 0.85em; color: #bbb; margin-top: 8px; display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; align-items: center;">
                <span>📢 RSS: 15 103 <a href="/rss.xml" target="_blank" style="color: #d32f2f; text-decoration: none; font-weight: bold;">[Подписаться]</a></span>
                <span style="color: #444;">|</span>
                <a href="https://dzen.ru/stable" target="_blank" style="color: #fff; text-decoration: none; font-weight: bold;">🟢 Наш Дзен</a>
                <span style="color: #444;">|</span>
                <a href="https://rutube.ru/channel/78405170/" target="_blank" style="color: #fff; text-decoration: none; font-weight: bold;">🔴 RuTube канал</a>
            </div>
        </div>
        """

        # Основной контент (Таймлайн лента)
        html += "<div class='container'><h1>Азбука трейдинга: база знаний</h1>"
        # 👇 НОВАЯ СТРОКА – подпись с датой и временем сборки
        html += f"<div style='font-size:0.85em; color:#777; margin-bottom:30px;'>Обновлено через git: {datetime.now().strftime('%Y-%m-%d %H:%M')}</div>"
        html += "<ul class='timeline'>"
        
        for _, row in df_visible.iterrows():
            t, l, d = str(row.get('Заголовок','')), str(row.get('Ссылка','#')), str(row.get('Анонс',''))
            if t:
                html += f"<li class='post-item'>"
                html += f"<a href='{l}' class='post-title' target='_blank'>{t}</a>"
                html += f"<p class='post-desc'>{d}</p>"
                html += f"<a href='{l}' class='read-btn' target='_blank'>Читать →</a>"
                html += f"</li>"
        
        html += "</ul></div>"

        # Блок инструментария Вебмастеров
        html += """
        <div class="webmaster-section">
            <div class="wm-title">Вебмастерам:</div>
            <div class="wm-grid">
                <a href="https://webmaster.yandex.ru/" class="wm-link" target="_blank">🔴 Яндекс.Вебмастер</a>
                <a href="https://search.google.com/search-console" class="wm-link" target="_blank">🔵 Google Search Console</a>
                <a href="https://www.bing.com/webmasters" class="wm-link" target="_blank">🟢 Bing Webmaster Tools</a>
                <a href="https://webmaster.mail.ru/" class="wm-link" target="_blank">🟠 Mail.ru Вебмастер</a>
            </div>
        </div>
        """

        # Футер с проектами и отметкой верификации DuckDuckGo
        html += f"""
        <div class="footer-projects">
            <strong>Проекты:</strong>
            <a href="https://dzen.ru/mindbug" class="proj-btn" target="_blank">🧠 Психология</a>
            <a href="https://dzen.ru/2mom" class="proj-btn" target="_blank">🤱 Мамам</a>
            <div style="margin-left: auto; font-size: 0.8em; color: #777;">DuckDuckGo verified via IndexNow</div>
            zdsf4xjgnevbm1w1
        </div>
        
        <script>
            async function getPrice(){{
                try{{
                    const r = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd');
                    const d = await r.json();
                    document.getElementById('btc-price').innerText = '₿ Bitcoin (BTC): ' + new Intl.NumberFormat('en-US',{{style:'currency',currency:'USD'}}).format(d.bitcoin.usd);
                }}catch(e){{document.getElementById('btc-price').innerText = '₿ Bitcoin (BTC): обновляется...';}}
            }}
            getPrice(); setInterval(getPrice, 60000);
        </script>
        </body></html>
        """
        
        # Запись файлов инфраструктуры сайта
        with open("index.html", "w", encoding="utf-8") as f: f.write(html)
        
        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\nRSS: {SITE_URL}rss.xml")

        # Создание RSS-ленты (максимум 50 последних вышедших постов)
        rss_items = ""
        for _, row in df_visible.head(50).iterrows():
            clean_t = str(row.get('Заголовок','')).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
            rss_items += f"<item><title>{clean_t}</title><link>{row.get('Ссылка')}</link><description>{row.get('Анонс')}</description></item>"
        
        with open("rss.xml", "w", encoding="utf-8") as f:
            f.write(f'<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0"><channel><title>{SITE_TITLE}</title><link>{SITE_URL}</link>{rss_items}</channel></rss>')

        # Обновление Карты сайта
        s_now = datetime.now().strftime('%Y-%m-%d')
        sitemap_content = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{SITE_URL}</loc><lastmod>{s_now}</lastmod><changefreq>hourly</changefreq><priority>1.0</priority></url></urlset>'
        with open("sitemap.xml", "w", encoding="utf-8") as f: f.write(sitemap_content)

        # 4. Одновременный Пинг в две поисковые системы (Bing + Яндекс) через IndexNow
        endpoints = ["https://www.bing.com/indexnow", "https://yandex.com/indexnow"]
        for url in endpoints:
            try:
                requests.post(url, json={
                    "host": "hesay.ru",
                    "key": INDEXNOW_KEY,
                    "keyLocation": f"{SITE_URL}{INDEXNOW_KEY}.txt",
                    "urlList": [SITE_URL]
                }, timeout=10)
            except Exception:
                pass
            
        print(f"Сайт успешно пересобран! Опубликовано постов на таймлайне: {len(df_visible)}")

    except Exception as e: 
        print(f"Критическая ошибка сборки: {e}")

if __name__ == "__main__": 
    build_site()
