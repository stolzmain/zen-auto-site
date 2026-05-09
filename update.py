import pandas as pd
from datetime import datetime

def build_site():
    try:
        # 1. Читаем данные из CSV
        df = pd.read_csv("data.csv")
        df.columns = df.columns.str.strip()
        
        TAGS = ["японские свечи", "графический анализ", "основы трейдинга", "психология", "криптовалюта"]
        
        SITE_TITLE = "Жить стабильно — Азбука начинающего трейдера и база знаний"
        PAGE_H1 = "Азбука трейдинга: база знаний для начинающих"
        SITE_DESC = "Понятный справочник по трейдингу для новичков. Учимся читать японские свечи, разбираем графический анализ и психологию рынка простыми словами."
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
        
        # Фавикон и RSS
        html += "<link rel='icon' href='favicon.ico' type='image/x-icon'>"
        html += f"<link rel='alternate' type='application/rss+xml' title='RSS лента {SITE_TITLE}' href='{SITE_URL}rss.xml'>"
        
        # Стили
        html += """
        <style>
            body{font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width:1024px; margin:40px auto; padding:20px; line-height:1.6; color:#333; background:#f0f2f5;}
            
            /* Темная шапка */
            .header-info {
                background: #1a1a1a; color: #fff; padding: 15px 0 10px 0; text-align: center; 
                font-size: 0.9em; border-radius: 12px 12px 0 0; border-bottom: 1px solid #333;
                position: relative; z-index: 2;
            }
            
            /* Белый контейнер: убраны верхние скругления для стыковки */
            .container{
                background:#fff; padding:35px; border-radius:0 0 12px 12px; 
                box-shadow:0 4px 15px rgba(0,0,0,0.08); margin-top: -1px; 
                position: relative; z-index: 1;
            }
            
            h1{margin-top:0; font-size:2.1em; color:#1a1a1a; border-bottom: 3px solid #d32f2f; padding-bottom: 10px;}
            .tags-cloud{margin:20px 0 30px 0; display:flex; flex-wrap:wrap; gap:8px;}
            .tag{background:#e8f0fe; color:#1967d2; padding:4px 12px; border-radius:15px; font-size:0.85em; font-weight:500;}
            ul{list-style:none; padding:0;} 
            li{margin-bottom:45px; border-bottom:1px solid #f0f0f0; padding-bottom:30px;}
            a.title{color:#000; text-decoration:none; font-size:1.4em; font-weight:bold; display:block; margin-bottom:12px;}
            a.title:hover{color:#d32f2f;}
            .read-more{display:inline-block; margin-top:10px; color:#d32f2f; text-decoration:none; font-weight:bold; border:2px solid #d32f2f; padding:6px 18px; border-radius:6px;}
            
            .footer-section{padding: 25px 35px; background: #fff; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); margin-top: 20px;}
            .footer-links{display: flex; gap: 12px; flex-wrap: wrap; margin-top: 15px;}
            .footer-btn{background: #222; color: #fff !important; padding: 12px 20px; text-decoration: none; border-radius: 8px; font-size: 0.9em; font-weight: bold; transition: 0.2s;}
            .footer-btn:hover{background: #d32f2f;}
        </style>
        """
        
        # Яндекс Метрика
        html += """
        <script type="text/javascript">
            (function(m,e,t,r,i,k,a){
                m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
                m[i].l=1*new Date();
                for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
                k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)
            })(window, document,'script','https://mc.yandex.ru/metrika/tag.js?id=105130661', 'ym');
            ym(105130661, 'init', {ssr:true, webvisor:true, clickmap:true, ecommerce:"dataLayer", referrer: document.referrer, url: location.href, accurateTrackBounce:true, trackLinks:true});
        </script>
        <noscript><div><img src="https://mc.yandex.ru/watch/105130661" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
        """
        
        html += "</head><body>"

        # Информер: Курс BTC + Подписчики
        html += """
        <div class="header-info">
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
                    const formattedPrice = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(price);
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
        
        html += "</ul></div>" 
        
        # Футер
        html += """
        <div class='footer-section'>
            <strong>Другие проекты:</strong>
            <div class='footer-links'>
                <a href='https://dzen.ru/mindbug' class='footer-btn' target='_blank'>🧠 Психология</a>
                <a href='https://dzen.ru/2mom' class='footer-btn' target='_blank'>🤱 Мамам</a>
            </div>
        </div>
        """
        
        html += "</body></html>"
        
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)

        # 3. Robots.txt и Sitemap.xml (без изменений)
        with open("robots.txt", "w", encoding="utf-8") as f:
            f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\nRSS: {SITE_URL}rss.xml")

        # 4. RSS.xml
        rss_items = ""
        for _, row in df.head(50).iterrows():
            t = str(row.get('Заголовок', '')).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            l = str(row.get('Ссылка', '#'))
            d = str(row.get('Анонс', '')).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            rss_items += f"<item><title>{t}</title><link>{l}</link><description>{d}</description><pubDate>{datetime.now().strftime('%a, %d %b %Y %H:%M:%S +0300')}</pubDate><guid>{l}</guid></item>"

        rss_content = f'<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0"><channel><title>{SITE_TITLE}</title><link>{SITE_URL}</link><description>{SITE_DESC}</description>{rss_items}</channel></rss>'
        with open("rss.xml", "w", encoding="utf-8") as f:
            f.write(rss_content)
            
        print("Сайт обновлен: шире 1024px, Метрика добавлена, углы исправлены.")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    build_site()
