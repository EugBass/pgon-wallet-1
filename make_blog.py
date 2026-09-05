import os
import json

articles = [
    {
        "slug": "kak-oplatit-chatgpt-plus-iz-rossii-2026",
        "title": "Как оплатить ChatGPT Plus и Claude Pro из России в 2026 году",
        "badge": "Гайды и сервисы",
        "date": "1 марта 2026",
        "read_time": "4 мин чтения",
        "hook": "Пошаговая инструкция по выпуску виртуальной карты PGON в Telegram и привязке её к OpenAI и Anthropic без посредников и риска блокировок аккаунта.",
        "icon": "🤖",
        "content_html": """
        <p class="lead">Оплата зарубежных нейросетей из России в 2026 году больше не требует переплат посредникам до 100% или покупки сомнительных чужих аккаунтов. С международной виртуальной картой <strong>PGON Virtual Card</strong> в Telegram вы можете безопасно оформить подписку на свой личный аккаунт OpenAI или Claude за 3 минуты.</p>

        <h2>Почему традиционные методы оплаты больше не работают</h2>
        <p>Пользователи сталкиваются со следующими сложностями:</p>
        <ul>
          <li><strong>Посредники и подарочные карты:</strong> берут комиссию от 30% до 80%, а код активации часто оказывается недействительным.</li>
          <li><strong>Покупка готовых чужих аккаунтов:</strong> через неделю продавец восстанавливает доступ, и вся история диалогов с ценными промптами безвозвратно теряется.</li>
          <li><strong>Блокировки OpenAI:</strong> биллинговая система Stripe моментально отклоняет карты банков РФ и большинства стран СНГ без европейского или американского BIN.</li>
        </ul>

        <div class="callout callout-info">
          <div class="callout-title">💡 Решение от PGON Wallet</div>
          <p>PGON Virtual Card выпускается с зарубежным BIN-кодом, полностью совместимым со Stripe, OpenAI, Anthropic, Midjourney и Apple Pay. Карта пополняется напрямую с баланса USDT (TRC-20, TON, BEP-20) без комиссий P2P-обменников.</p>
        </div>

        <h2>Пошаговый алгоритм оплаты ChatGPT Plus</h2>
        
        <h3>Шаг 1. Открытие PGON Wallet в Telegram</h3>
        <p>Запустите официального бота <a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener">@pgon_wallet_bot</a>. Вам не нужно проходить длительную верификацию документов для базовых тарифов — кошелек готов к работе сразу после запуска.</p>

        <h3>Шаг 2. Пополнение баланса криптовалютой</h3>
        <p>Перейдите в раздел <em>«Пополнить»</em> и отправьте USDT или TON на адрес вашего персонального депозита. Средства зачисляются автоматически после 1 подтверждения сети.</p>

        <h3>Шаг 3. Мгновенный выпуск виртуальной карты</h3>
        <p>В меню бота нажмите <em>«Выпустить карту»</em>. Карта моментально генерируется в защищенном интерфейсе Telegram: вы получаете полный номер карты (16 цифр), срок действия (EXP) и код безопасности (CVC).</p>

        <h3>Шаг 4. Оплата на сайте OpenAI</h3>
        <p>Включите надежное интернет-соединение соответствующего региона, откройте ChatGPT и выберите <strong>«Upgrade to Plus»</strong>. Введите реквизиты карты PGON и любой адрес (Billing Address) страны эмитента карты. Подтверждение платежа происходит моментально.</p>

        <div class="callout callout-warning">
          <div class="callout-title">⚠️ Важный совет по безопасности</div>
          <p>Не используйте перегруженные публичные VPN при вводе платежных данных на OpenAI. Используйте выделенный IP или надежный приватный сервер, чтобы защитные алгоритмы Stripe не пометили сессию как подозрительную.</p>
        </div>

        <h2>Какие еще сервисы принимает карта PGON?</h2>
        <p>Карта успешно протестирована и стабильно работает со следующими сервисами:</p>
        <ul>
          <li><strong>ИИ и разработка:</strong> OpenAI ChatGPT Plus, Claude Pro, Midjourney, Cursor AI, GitHub Copilot, Vercel, Supabase;</li>
          <li><strong>Магазины приложений:</strong> Apple App Store (смена региона), Google Play Console, Steam;</li>
          <li><strong>Медиа и стриминг:</strong> Netflix, Spotify Premium, YouTube Premium, Canva Pro, Figma.</li>
        </ul>
        """
    },
    {
        "slug": "kak-oplachivat-po-qr-sbp-kriptovalyutoy",
        "title": "Оплата по QR СБП с криптокошелька: как это устроено без P2P",
        "badge": "Технологии СБП",
        "date": "24 февраля 2026",
        "read_time": "3 мин чтения",
        "hook": "Разбираем технологию прямого криптоэквайринга: как расплачиваться в супермаркетах, кафе и на АЗС криптовалютой без банковских карт и блокировок 115-ФЗ.",
        "icon": "⚡",
        "content_html": """
        <p class="lead">Система быстрых платежей (СБП) Банка России установлена более чем на 90% кассовых терминалов по всей стране. PGON объединил инфраструктуру СБП с некастодиальным хранением криптовалюты, позволив оплачивать повседневные покупки напрямую с USDT-баланса.</p>

        <h2>Проблема классического P2P при покупках</h2>
        <p>До появления прямого крипто-СБП пользователям приходилось:</p>
        <ol>
          <li>Заходить на P2P-биржу за 15 минут до кассы;</li>
          <li>Создавать ордер на продажу 10-20 USDT;</li>
          <li>Ждать перевод на банковскую карту от случайного физлица;</li>
          <li>Рисковать получением «грязных» рублей и последующей блокировкой счета по 115-ФЗ.</li>
        </ol>

        <h2>Как работает шлюз PGON Pay</h2>
        <p>PGON исключает человека из цепочки расчетов. Процесс полностью автоматизирован:</p>
        
        <div class="callout callout-info">
          <div class="callout-title">⚡ Цикл транзакции за 3 секунды</div>
          <p>1. Вы сканируете QR-код на кассе (в супермаркете, автомойке, кафе или ресторане).<br>
          2. Бот PGON парсит платежные реквизиты НСПК/СБП и фиксирует точную сумму в рублях.<br>
          3. По прозрачному биржевому курсу рассчитывается эквивалент в USDT.<br>
          4. Автоматизированный банковский провайдер PGON выплачивает мерчанту рубли по СБП, а с вашего баланса списывается криптовалюта.</p>
        </div>

        <h2>Преимущества для покупателя</h2>
        <ul>
          <li><strong>Никаких дропов:</strong> платеж идет от аккредитованного платежного партнера со стандартным фискальным чеком.</li>
          <li><strong>Курс выгоднее обменников:</strong> отсутствие посредников снижает суммарные спреды до минимума.</li>
          <li><strong>Мгновенно:</strong> кассир слышит звуковой сигнал об успешной оплате через 2–3 секунды после подтверждения в Telegram.</li>
        </ul>
        """
    },
    {
        "slug": "kak-izbezhat-blokirovok-115-fz-pri-rabote-s-kriptoy",
        "title": "Безопасность криптовалютных расчетов и защита от 115-ФЗ",
        "badge": "Безопасность",
        "date": "18 февраля 2026",
        "read_time": "5 мин чтения",
        "hook": "Гид по финансовой гигиене: почему российские банки массово блокируют счета криптоэнтузиастов и как легально защитить свои средства при расчетах.",
        "icon": "🛡️",
        "content_html": """
        <p class="lead">Федеральный закон № 115-ФЗ стал главным барьером между криптоиндустрией и повседневными финансами. Ежедневно тысячи счетов замораживаются из-за переводов с бирж и P2P-сделок. В этой статье мы подробно объясняем критерии банковского комплаенса и методы защиты капитала.</p>

        <h2>Три главных триггера финмониторинга банков в 2026 году</h2>
        <p>Современные антифрод-системы ведущих банков используют алгоритмы машинного обучения, которые выявляют нетипичные паттерны за доли секунды:</p>

        <h3>1. Входящие переводы от сомнительных физлиц</h3>
        <p>Если на P2P-платформе контрагент отправил вам рубли с карты, которая фигурировала в цепочках нелегального обналичивания или мошенничества, ваш счет автоматически попадает в базу данных подозрительных операций ЦБ РФ.</p>

        <h3>2. Высокая транзакционная активность и «веерные» переводы</h3>
        <p>Более 15–20 входящих или исходящих переводов физлицам в сутки, особенно в ночное время или с круглыми суммами, вызывают мгновенный запрос подтверждающих документов.</p>

        <h3>3. Моментальное списание поступивших средств</h3>
        <p>Если деньги поступили на счет и в течение 10 минут переведены дальше или сняты в банкомате — это классический признак транзитного счета по методическим рекомендациям ЦБ № 16-МР.</p>

        <div class="callout callout-warning">
          <div class="callout-title">⚠️ Последствия блокировки по 115-ФЗ</div>
          <p>Присвоение «красного» уровня риска на платформе «Знай своего клиента» (ЗСК) ведет к блокировке дистанционного банковского обслуживания во всех банках РФ и запрету на выпуск новых карт.</p>
        </div>

        <h2>Как PGON Wallet решает проблему 115-ФЗ</h2>
        <p>Используя PGON, вы полностью устраняете рискованные межбанковские переводы между физическими лицами:</p>
        <ul>
          <li><strong>Оплата по СБП</strong> — это покупка в магазине (B2C транзакция). К таким операциям у банков нет претензий, так как отсутствует признак обналичивания.</li>
          <li><strong>Виртуальная карта</strong> эмитирована зарубежной организацией, не подпадает под внутренний мониторинг банков РФ и защищает ваше основное финансовое досье.</li>
          <li><strong>Криптовалютный баланс</strong> защищен некастодиальной архитектурой: ваши активы хранятся в блокчейне, а не на банковских серверах.</li>
        </ul>
        """
    },
    {
        "slug": "virtualnaya-karta-dlya-app-store-i-steam",
        "title": "Как пополнить баланс Steam и оплатить App Store без комиссии",
        "badge": "Игры и App Store",
        "date": "10 февраля 2026",
        "read_time": "3 мин чтения",
        "hook": "Покупаем игры, боевые пропуски и мобильные приложения по официальным ценам без 25% комиссии посредников и кошельков сторонних стран.",
        "icon": "🎮",
        "content_html": """
        <p class="lead">Геймеры и владельцы техники Apple в РФ вынуждены переплачивать сотни рублей за каждый платеж через сотовых операторов или турецкие виртуальные карты с ежемесячной абонплатой. С виртуальной картой PGON покупка игр и софта снова становится простой и выгодной.</p>

        <h2>Пополнение Steam напрямую</h2>
        <p>Большинство российских геймеров используют посреднические сервисы, где комиссия достигает 15-25% от суммы. Карта PGON решает этот вопрос:</p>
        <ul>
          <li>Поддерживает смену региона Steam на регион карты с региональными скидками;</li>
          <li>Позволяет оплачивать игры напрямую со счета USDT;</li>
          <li>Мгновенно активирует баланс кошелька Steam Wallet без задержек.</li>
        </ul>

        <h2>Оплата подписок в Apple App Store</h2>
        <p>Привязка виртуальной карты PGON к зарубежному Apple ID (например, США, Кипр или Казахстан) открывает доступ ко всем приложениям, удаленным из российского App Store:</p>
        <ul>
          <li>Официальный клиент <strong>ChatGPT</strong> с голосовым режимом;</li>
          <li>Банковские и финансовые приложения;</li>
          <li>Подписки на <strong>iCloud+, Apple Music и Apple Arcade</strong>.</li>
        </ul>

        <div class="callout callout-info">
          <div class="callout-title">🚀 Быстрый старт</div>
          <p>Выпуск виртуальной карты в боте <a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener">@pgon_wallet_bot</a> занимает менее 60 секунд. Пополняйте с баланса USDT и оплачивайте покупки сразу же.</p>
        </div>
        """
    }
]

# Write articles to disk
os.makedirs('blog', exist_ok=True)

# Generate single article pages
for a in articles:
    filename = f"blog/{a['slug']}.html"
    other_articles = [o for o in articles if o['slug'] != a['slug']][:3]
    
    other_cards_html = ""
    for o in other_articles:
        other_cards_html += f"""
        <a href="/blog/{o['slug']}.html" class="related-card">
          <span class="related-badge">{o['badge']}</span>
          <h4 class="related-title">{o['title']}</h4>
          <p class="related-hook">{o['hook']}</p>
          <div class="related-meta">
            <span>{o['date']}</span>
            <span>•</span>
            <span>{o['read_time']}</span>
          </div>
        </a>
        """

    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{a['title']} | Блог PGON Wallet</title>
  <meta name="title" content="{a['title']} | Блог PGON Wallet">
  <meta name="description" content="{a['hook']}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://pgon.pro/blog/{a['slug']}.html">
  
  <link rel="icon" type="image/png" href="/assets/pgon-icon.png">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="apple-touch-icon" href="/assets/pgon-icon.png">

  <meta property="og:type" content="article">
  <meta property="og:url" content="https://pgon.pro/blog/{a['slug']}.html">
  <meta property="og:title" content="{a['title']} | Блог PGON Wallet">
  <meta property="og:description" content="{a['hook']}">
  <meta property="og:image" content="https://pgon.pro/hero-bg.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&family=Unbounded:wght@500;600;700;800;900&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg-dark: #070310;
      --bg-surface: #100620;
      --bg-surface-elevated: #1a0b33;
      --bg-card: rgba(26, 11, 51, 0.65);
      --border-glass: rgba(157, 78, 221, 0.22);
      --border-glow: #A855F7;
      --primary-purple: #8A14F7;
      --light-purple: #E0AAFF;
      --accent-orange: #FF9E00;
      --text-main: #F3EEF9;
      --text-muted: #B8A9CC;
      --text-dim: #7A6990;
      --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(138, 20, 247, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 85% 65%, rgba(255, 158, 0, 0.08) 0%, transparent 45%);
      background-attachment: fixed;
    }}

    .container {{
      width: 100%;
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }}

    /* Header */
    .site-header {{
      background: rgba(7, 3, 16, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-glass);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 0.85rem 0;
    }}

    .header-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
    }}

    .brand-logo {{
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.3rem 1.15rem 0.3rem 0.35rem;
      border-radius: 9999px;
      background: linear-gradient(135deg, rgba(34, 12, 68, 0.75) 0%, rgba(18, 6, 38, 0.85) 100%);
      border: 2px solid #8A14F7;
      box-shadow: 0 0 16px rgba(138, 20, 247, 0.45), inset 0 0 12px rgba(138, 20, 247, 0.25);
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
      white-space: nowrap;
      flex-shrink: 0;
      text-decoration: none;
    }}
    .brand-logo:hover {{
      border-color: #A855F7;
      box-shadow: 0 0 24px rgba(168, 85, 247, 0.75), inset 0 0 16px rgba(168, 85, 247, 0.35);
      transform: translateY(-1px) scale(1.02);
    }}
    .brand-logo-img {{
      width: 36px;
      height: 36px;
      background: transparent;
      border: none;
      object-fit: contain;
      filter: drop-shadow(0 0 8px rgba(192, 132, 252, 0.6));
      transition: transform 0.3s ease;
      flex-shrink: 0;
    }}
    .brand-logo:hover .brand-logo-img {{
      transform: rotate(-3deg) scale(1.05);
    }}
    .brand-logo-text {{
      font-family: 'Unbounded', sans-serif;
      font-size: 1.4rem;
      font-weight: 900;
      letter-spacing: 0.04em;
      background: linear-gradient(180deg, #A855F7 0%, #7E22CE 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
      line-height: 1;
      filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.5));
    }}

    .header-nav {{
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }}

    .header-nav a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      transition: var(--transition);
    }}

    .header-nav a:hover,
    .header-nav a.active {{
      color: #fff;
    }}

    .btn-header-cta {{
      background: linear-gradient(135deg, #FF9E00, #FF6000);
      color: #fff;
      font-weight: 700;
      font-size: 0.88rem;
      padding: 0.55rem 1.25rem;
      border-radius: 9999px;
      text-decoration: none;
      box-shadow: 0 0 20px rgba(255, 158, 0, 0.35);
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      white-space: nowrap;
    }}

    .btn-header-cta:hover {{
      transform: translateY(-1px);
      box-shadow: 0 0 28px rgba(255, 158, 0, 0.55);
    }}

    /* Article layout */
    .article-main {{
      flex: 1;
      padding: 2.5rem 0 5rem;
    }}

    .article-wrap {{
      max-width: 820px;
      margin: 0 auto;
    }}

    .breadcrumbs {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.88rem;
      color: var(--text-dim);
      margin-bottom: 2rem;
    }}

    .breadcrumbs a {{
      color: var(--text-muted);
      text-decoration: none;
      transition: var(--transition);
    }}

    .breadcrumbs a:hover {{
      color: #fff;
    }}

    .article-header {{
      margin-bottom: 2.5rem;
    }}

    .article-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.35rem 0.85rem;
      border-radius: 9999px;
      background: rgba(138, 20, 247, 0.15);
      border: 1px solid rgba(168, 85, 247, 0.35);
      color: var(--light-purple);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      margin-bottom: 1.25rem;
    }}

    .article-title {{
      font-family: 'Unbounded', sans-serif;
      font-size: clamp(1.8rem, 3.8vw, 2.5rem);
      font-weight: 800;
      line-height: 1.25;
      color: #FFFFFF;
      margin-bottom: 1.25rem;
      letter-spacing: -0.02em;
    }}

    .article-meta {{
      display: flex;
      align-items: center;
      gap: 1.25rem;
      font-size: 0.9rem;
      color: var(--text-dim);
      padding-bottom: 1.75rem;
      border-bottom: 1px solid var(--border-glass);
    }}

    .article-content {{
      font-size: 1.05rem;
      line-height: 1.75;
      color: #DFD7EC;
    }}

    .article-content p {{
      margin-bottom: 1.5rem;
    }}

    .article-content p.lead {{
      font-size: 1.2rem;
      line-height: 1.7;
      color: #FFFFFF;
      font-weight: 500;
    }}

    .article-content h2 {{
      font-family: 'Unbounded', sans-serif;
      font-size: 1.5rem;
      font-weight: 800;
      color: #FFFFFF;
      margin: 2.5rem 0 1rem;
      letter-spacing: -0.01em;
    }}

    .article-content h3 {{
      font-family: 'Unbounded', sans-serif;
      font-size: 1.18rem;
      font-weight: 700;
      color: var(--light-purple);
      margin: 2rem 0 0.85rem;
    }}

    .article-content ul, .article-content ol {{
      margin: 1.25rem 0 1.75rem 1.5rem;
    }}

    .article-content li {{
      margin-bottom: 0.65rem;
      color: #DFD7EC;
    }}

    .article-content strong {{
      color: #FFFFFF;
    }}

    .article-content a {{
      color: var(--light-purple);
      text-decoration: underline;
      text-underline-offset: 3px;
    }}

    .article-content a:hover {{
      color: #fff;
    }}

    .callout {{
      border-radius: 14px;
      padding: 1.5rem;
      margin: 2rem 0;
      background: rgba(26, 11, 51, 0.7);
      border: 1px solid rgba(138, 20, 247, 0.3);
      position: relative;
    }}

    .callout-title {{
      font-family: 'Unbounded', sans-serif;
      font-size: 1.02rem;
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 0.65rem;
    }}

    .callout-info {{
      border-left: 4px solid var(--primary-purple);
      background: linear-gradient(135deg, rgba(138, 20, 247, 0.12), rgba(26, 11, 51, 0.7));
    }}

    .callout-warning {{
      border-left: 4px solid var(--accent-orange);
      background: linear-gradient(135deg, rgba(255, 158, 0, 0.12), rgba(26, 11, 51, 0.7));
    }}

    .article-cta-box {{
      margin: 3.5rem 0 2rem;
      padding: 2.25rem;
      border-radius: 18px;
      background: linear-gradient(135deg, rgba(34, 12, 68, 0.95), rgba(18, 6, 38, 0.98));
      border: 2px solid #8A14F7;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5), 0 0 24px rgba(138, 20, 247, 0.35);
      text-align: center;
    }}

    .article-cta-box h3 {{
      font-family: 'Unbounded', sans-serif;
      font-size: 1.45rem;
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 0.75rem;
    }}

    .article-cta-box p {{
      color: var(--text-muted);
      font-size: 0.98rem;
      margin-bottom: 1.5rem;
      max-width: 540px;
      margin-left: auto;
      margin-right: auto;
    }}

    .btn-cta-big {{
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      background: linear-gradient(135deg, #FF9E00, #FF6000);
      color: #FFFFFF;
      font-weight: 800;
      font-size: 1.05rem;
      padding: 0.85rem 2rem;
      border-radius: 9999px;
      text-decoration: none;
      box-shadow: 0 0 24px rgba(255, 158, 0, 0.4);
      transition: var(--transition);
    }}

    .btn-cta-big:hover {{
      transform: translateY(-2px);
      box-shadow: 0 0 32px rgba(255, 158, 0, 0.65);
    }}

    /* Related articles */
    .related-section {{
      margin-top: 4rem;
      padding-top: 3rem;
      border-top: 1px solid var(--border-glass);
    }}

    .related-section h3 {{
      font-family: 'Unbounded', sans-serif;
      font-size: 1.35rem;
      font-weight: 800;
      color: #FFFFFF;
      margin-bottom: 1.5rem;
    }}

    .related-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 1.25rem;
    }}

    .related-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 14px;
      padding: 1.35rem;
      text-decoration: none;
      transition: var(--transition);
      display: flex;
      flex-direction: column;
    }}

    .related-card:hover {{
      transform: translateY(-3px);
      border-color: var(--border-glow);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5), 0 0 16px rgba(138, 20, 247, 0.25);
    }}

    .related-badge {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--light-purple);
      margin-bottom: 0.6rem;
    }}

    .related-title {{
      font-family: 'Unbounded', sans-serif;
      font-size: 0.98rem;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 0.65rem;
      line-height: 1.35;
    }}

    .related-hook {{
      font-size: 0.84rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 1rem;
      flex: 1;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .related-meta {{
      display: flex;
      gap: 0.4rem;
      font-size: 0.76rem;
      color: var(--text-dim);
    }}

    /* Footer */
    .site-footer {{
      background: #070310;
      border-top: 1px solid var(--border-glass);
      padding: 3.5rem 0 2rem;
      margin-top: auto;
    }}

    .footer-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 2.5rem;
      margin-bottom: 2.5rem;
    }}

    .footer-brand p {{
      color: var(--text-muted);
      font-size: 0.88rem;
      margin-top: 0.85rem;
      max-width: 320px;
      line-height: 1.6;
    }}

    .footer-col h4 {{
      font-family: 'Unbounded', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 1rem;
      letter-spacing: -0.01em;
    }}

    .footer-col ul {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
    }}

    .footer-col a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.86rem;
      transition: var(--transition);
    }}

    .footer-col a:hover {{
      color: #FFFFFF;
      padding-left: 2px;
    }}

    .footer-bottom {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 2rem;
      padding-top: 1.75rem;
      border-top: 1px solid rgba(157, 78, 221, 0.12);
      font-size: 0.82rem;
      color: var(--text-dim);
      line-height: 1.6;
    }}

    .footer-bottom-left {{
      text-align: left;
    }}

    .footer-bottom-right {{
      text-align: right;
    }}

    @media (max-width: 860px) {{
      .footer-grid {{
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
      }}
    }}

    @media (max-width: 580px) {{
      .footer-grid {{
        grid-template-columns: 1fr;
      }}
      .footer-bottom {{
        flex-direction: column;
        gap: 0.75rem;
        text-align: center;
      }}
      .footer-bottom-left,
      .footer-bottom-right {{
        text-align: center;
      }}
      .header-nav {{
        display: none;
      }}
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="container">
      <div class="header-inner">
        <a href="/#hero" class="brand-logo" aria-label="PGON Wallet Главная">
          <img src="/assets/pgon-icon.png" alt="PGON Wallet" class="brand-logo-img" width="36" height="36" />
          <span class="brand-logo-text">PGON</span>
        </a>
        <nav class="header-nav">
          <a href="/#pipeline">Как работает</a>
          <a href="/#benefits">Преимущества</a>
          <a href="/#card">Виртуальная карта</a>
          <a href="/#tariffs">Тарифы</a>
          <a href="/#faq">FAQ</a>
          <a href="/blog.html" class="active">Блог</a>
        </nav>
        <a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer" class="btn-header-cta">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="m20.665 3.717-17.73 6.837c-1.21.486-1.203 1.161-.222 1.462l4.552 1.42 10.532-6.645c.498-.303.953-.14.579.192l-8.533 7.701h-.002l-.313 4.674c.459 0 .661-.211.918-.46l2.206-2.145 4.588 3.389c.845.466 1.455.226 1.666-.783l3.007-14.166c.309-1.238-.474-1.8-1.282-1.439z"/></svg>
          Открыть в Telegram
        </a>
      </div>
    </div>
  </header>

  <main class="article-main">
    <div class="container">
      <div class="article-wrap">
        <div class="breadcrumbs">
          <a href="/#hero">Главная</a>
          <span>/</span>
          <a href="/blog.html">Блог</a>
          <span>/</span>
          <span>{a['badge']}</span>
        </div>

        <article class="article-header">
          <span class="article-badge">{a['icon']} {a['badge']}</span>
          <h1 class="article-title">{a['title']}</h1>
          <div class="article-meta">
            <span>📅 {a['date']}</span>
            <span>⏱️ {a['read_time']}</span>
            <span>✍️ PGON Media</span>
          </div>
        </article>

        <div class="article-content">
          {a['content_html']}

          <div class="article-cta-box">
            <h3>Оформите карту и оплатите за 2 минуты</h3>
            <p>Запустите PGON Wallet в Telegram — без бумажной волокиты, P2P-рисков и посредников.</p>
            <a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer" class="btn-cta-big">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="m20.665 3.717-17.73 6.837c-1.21.486-1.203 1.161-.222 1.462l4.552 1.42 10.532-6.645c.498-.303.953-.14.579.192l-8.533 7.701h-.002l-.313 4.674c.459 0 .661-.211.918-.46l2.206-2.145 4.588 3.389c.845.466 1.455.226 1.666-.783l3.007-14.166c.309-1.238-.474-1.8-1.282-1.439z"/></svg>
              Запустить PGON в Telegram
            </a>
          </div>
        </div>

        <section class="related-section">
          <h3>Читайте также в блоге</h3>
          <div class="related-grid">
            {other_cards_html}
          </div>
        </section>

      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/#hero" class="brand-logo">
            <img src="/assets/pgon-icon.png" alt="PGON Wallet" class="brand-logo-img" width="36" height="36" />
            <span class="brand-logo-text">PGON</span>
          </a>
          <p>Инновационный платежный Web3-шлюз нового поколения. Мгновенные расчеты по СБП напрямую с баланса USDT и TON по всей России</p>
        </div>
        <div class="footer-col">
          <h4>Навигация</h4>
          <ul>
            <li><a href="/#hero">Главная</a></li>
            <li><a href="/#pipeline">Как это работает</a></li>
            <li><a href="/#benefits">Преимущества</a></li>
            <li><a href="/#card">Виртуальная карта</a></li>
            <li><a href="/#cases">Сценарии использования</a></li>
            <li><a href="/#tariffs">Тарифная сетка</a></li>
            <li><a href="/#faq">База знаний FAQ</a></li>
            <li><a href="/blog.html">Блог и гайды</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Продукты</h4>
          <ul>
            <li><a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer">PGON Virtual Card (Visa/MC)</a></li>
            <li><a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer">Telegram Mini App</a></li>
            <li><a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer">PGON Pay для бизнеса</a></li>
            <li><a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer">Реферальная программа</a></li>
            <li><a href="https://t.me/pgon_support_bot" target="_blank" rel="noopener noreferrer">API документация</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Юридическая информация</h4>
          <ul>
            <li><a href="/terms.html">Пользовательское соглашение</a></li>
            <li><a href="/privacy.html">Политика конфиденциальности</a></li>
            <li><a href="/aml-cft.html">Политика AML & KYC</a></li>
            <li><a href="/cookies.html">Политика файлов Cookie</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-bottom-left">
          <p>© 2026 PGON Technologies Ltd. InterSpin LLC.<br>Все права защищены</p>
        </div>
        <div class="footer-bottom-right">
          <p>Криптоактивы сопряжены с рыночной волатильностью.<br>Сервис не предоставляет финансовых консультаций</p>
        </div>
      </div>
    </div>
  </footer>

</body>
</html>
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {filename}")

# Generate catalog page: blog.html
catalog_cards_html = ""
for idx, a in enumerate(articles):
    featured_class = "blog-card-featured" if idx == 0 else ""
    catalog_cards_html += f"""
    <article class="blog-card {featured_class}">
      <div class="blog-card-body">
        <div class="blog-card-top">
          <span class="blog-card-badge">{a['icon']} {a['badge']}</span>
          <span class="blog-card-date">{a['date']} • {a['read_time']}</span>
        </div>
        <h2 class="blog-card-title">
          <a href="/blog/{a['slug']}.html">{a['title']}</a>
        </h2>
        <p class="blog-card-hook">{a['hook']}</p>
        <div class="blog-card-bottom">
          <a href="/blog/{a['slug']}.html" class="blog-card-link">
            <span>Читать статью</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </a>
        </div>
      </div>
    </article>
    """

blog_index_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Блог PGON Wallet — Инструкции, безопасность и оплата криптовалютой</title>
  <meta name="title" content="Блог PGON Wallet — Инструкции, безопасность и оплата криптовалютой">
  <meta name="description" content="Официальный блог PGON Wallet: пошаговые гайды по оплате ChatGPT, Claude, App Store, Steam, инструкции по СБП и разборы защиты от 115-ФЗ.">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://pgon.pro/blog.html">

  <link rel="icon" type="image/png" href="./assets/pgon-icon.png">
  <link rel="icon" type="image/svg+xml" href="./favicon.svg">
  <link rel="apple-touch-icon" href="./assets/pgon-icon.png">

  <meta property="og:type" content="website">
  <meta property="og:url" content="https://pgon.pro/blog.html">
  <meta property="og:title" content="Блог PGON Wallet — Инструкции, безопасность и оплата криптовалютой">
  <meta property="og:description" content="Официальный блог PGON Wallet: пошаговые гайды по оплате ChatGPT, Claude, App Store, Steam, инструкции по СБП и разборы защиты от 115-ФЗ.">
  <meta property="og:image" content="https://pgon.pro/hero-bg.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&family=Unbounded:wght@500;600;700;800;900&display=swap" rel="stylesheet">

  <style>
    :root {{
      --bg-dark: #070310;
      --bg-surface: #100620;
      --bg-card: rgba(26, 11, 51, 0.65);
      --border-glass: rgba(157, 78, 221, 0.22);
      --border-glow: #A855F7;
      --primary-purple: #8A14F7;
      --light-purple: #E0AAFF;
      --accent-orange: #FF9E00;
      --text-main: #F3EEF9;
      --text-muted: #B8A9CC;
      --text-dim: #7A6990;
      --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      background-image: 
        radial-gradient(circle at 10% 20%, rgba(138, 20, 247, 0.15) 0%, transparent 50%),
        radial-gradient(circle at 90% 80%, rgba(255, 158, 0, 0.08) 0%, transparent 50%);
      background-attachment: fixed;
    }}

    .container {{
      width: 100%;
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 1.5rem;
    }}

    .site-header {{
      background: rgba(7, 3, 16, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-glass);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 0.85rem 0;
    }}

    .header-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
    }}

    .brand-logo {{
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      padding: 0.3rem 1.15rem 0.3rem 0.35rem;
      border-radius: 9999px;
      background: linear-gradient(135deg, rgba(34, 12, 68, 0.75) 0%, rgba(18, 6, 38, 0.85) 100%);
      border: 2px solid #8A14F7;
      box-shadow: 0 0 16px rgba(138, 20, 247, 0.45), inset 0 0 12px rgba(138, 20, 247, 0.25);
      transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
      white-space: nowrap;
      flex-shrink: 0;
      text-decoration: none;
    }}
    .brand-logo:hover {{
      border-color: #A855F7;
      box-shadow: 0 0 24px rgba(168, 85, 247, 0.75), inset 0 0 16px rgba(168, 85, 247, 0.35);
      transform: translateY(-1px) scale(1.02);
    }}
    .brand-logo-img {{
      width: 36px;
      height: 36px;
      background: transparent;
      border: none;
      object-fit: contain;
      filter: drop-shadow(0 0 8px rgba(192, 132, 252, 0.6));
      transition: transform 0.3s ease;
      flex-shrink: 0;
    }}
    .brand-logo:hover .brand-logo-img {{
      transform: rotate(-3deg) scale(1.05);
    }}
    .brand-logo-text {{
      font-family: 'Unbounded', sans-serif;
      font-size: 1.4rem;
      font-weight: 900;
      letter-spacing: 0.04em;
      background: linear-gradient(180deg, #A855F7 0%, #7E22CE 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
      line-height: 1;
      filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.5));
    }}

    .header-nav {{
      display: flex;
      align-items: center;
      gap: 1.5rem;
    }}

    .header-nav a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.9rem;
      font-weight: 600;
      transition: var(--transition);
    }}

    .header-nav a:hover,
    .header-nav a.active {{
      color: #fff;
    }}

    .btn-header-cta {{
      background: linear-gradient(135deg, #FF9E00, #FF6000);
      color: #fff;
      font-weight: 700;
      font-size: 0.88rem;
      padding: 0.55rem 1.25rem;
      border-radius: 9999px;
      text-decoration: none;
      box-shadow: 0 0 20px rgba(255, 158, 0, 0.35);
      transition: var(--transition);
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      white-space: nowrap;
    }}

    .btn-header-cta:hover {{
      transform: translateY(-1px);
      box-shadow: 0 0 28px rgba(255, 158, 0, 0.55);
    }}

    /* Hero */
    .blog-hero {{
      padding: 4rem 0 3rem;
      text-align: center;
      max-width: 860px;
      margin: 0 auto;
    }}

    .blog-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.35rem 0.95rem;
      border-radius: 9999px;
      background: rgba(138, 20, 247, 0.15);
      border: 1px solid rgba(168, 85, 247, 0.35);
      color: var(--light-purple);
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 1.25rem;
    }}

    .blog-hero h1 {{
      font-family: 'Unbounded', sans-serif;
      font-size: clamp(2rem, 4.5vw, 3rem);
      font-weight: 800;
      line-height: 1.2;
      color: #FFFFFF;
      margin-bottom: 1.25rem;
      letter-spacing: -0.02em;
    }}

    .gradient-text {{
      background: linear-gradient(135deg, #FF9E00 0%, #E0AAFF 50%, #C084FC 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .blog-hero p {{
      color: var(--text-muted);
      font-size: 1.08rem;
      max-width: 640px;
      margin: 0 auto;
      line-height: 1.65;
    }}

    /* Grid */
    .blog-section {{
      flex: 1;
      padding-bottom: 5rem;
    }}

    .blog-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
      gap: 1.75rem;
    }}

    .blog-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: 18px;
      padding: 1.85rem;
      transition: var(--transition);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }}

    .blog-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, transparent, #8A14F7, transparent);
      opacity: 0;
      transition: opacity 0.3s ease;
    }}

    .blog-card:hover {{
      transform: translateY(-4px);
      border-color: var(--border-glow);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(138, 20, 247, 0.3);
    }}

    .blog-card:hover::before {{
      opacity: 1;
    }}

    .blog-card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      margin-bottom: 1rem;
    }}

    .blog-card-badge {{
      font-size: 0.76rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--light-purple);
      background: rgba(138, 20, 247, 0.2);
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
    }}

    .blog-card-date {{
      font-size: 0.8rem;
      color: var(--text-dim);
    }}

    .blog-card-title {{
      font-family: 'Unbounded', sans-serif;
      font-size: 1.25rem;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 0.85rem;
      line-height: 1.35;
    }}

    .blog-card-title a {{
      color: #FFFFFF;
      text-decoration: none;
      transition: var(--transition);
    }}

    .blog-card-title a:hover {{
      color: var(--light-purple);
    }}

    .blog-card-hook {{
      font-size: 0.94rem;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 1.5rem;
      flex: 1;
    }}

    .blog-card-bottom {{
      padding-top: 1.25rem;
      border-top: 1px solid rgba(157, 78, 221, 0.12);
    }}

    .blog-card-link {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--light-purple);
      font-weight: 700;
      font-size: 0.92rem;
      text-decoration: none;
      transition: var(--transition);
    }}

    .blog-card-link:hover {{
      color: #FFFFFF;
      gap: 0.75rem;
    }}

    /* Footer */
    .site-footer {{
      background: #070310;
      border-top: 1px solid var(--border-glass);
      padding: 3.5rem 0 2rem;
      margin-top: auto;
    }}

    .footer-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 2.5rem;
      margin-bottom: 2.5rem;
    }}

    .footer-brand p {{
      color: var(--text-muted);
      font-size: 0.88rem;
      margin-top: 0.85rem;
      max-width: 320px;
      line-height: 1.6;
    }}

    .footer-col h4 {{
      font-family: 'Unbounded', sans-serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 1rem;
      letter-spacing: -0.01em;
    }}

    .footer-col ul {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
    }}

    .footer-col a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.86rem;
      transition: var(--transition);
    }}

    .footer-col a:hover {{
      color: #FFFFFF;
      padding-left: 2px;
    }}

    .footer-bottom {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 2rem;
      padding-top: 1.75rem;
      border-top: 1px solid rgba(157, 78, 221, 0.12);
      font-size: 0.82rem;
      color: var(--text-dim);
      line-height: 1.6;
    }}

    .footer-bottom-left {{
      text-align: left;
    }}

    .footer-bottom-right {{
      text-align: right;
    }}

    @media (max-width: 860px) {{
      .footer-grid {{
        grid-template-columns: 1fr 1fr;
        gap: 2rem;
      }}
    }}

    @media (max-width: 580px) {{
      .blog-grid {{
        grid-template-columns: 1fr;
      }}
      .footer-grid {{
        grid-template-columns: 1fr;
      }}
      .footer-bottom {{
        flex-direction: column;
        gap: 0.75rem;
        text-align: center;
      }}
      .footer-bottom-left,
      .footer-bottom-right {{
        text-align: center;
      }}
      .header-nav {{
        display: none;
      }}
    }}
  </style>
</head>
<body>

  <header class="site-header">
    <div class="container">
      <div class="header-inner">
        <a href="/#hero" class="brand-logo" aria-label="PGON Wallet Главная">
          <img src="/assets/pgon-icon.png" alt="PGON Wallet" class="brand-logo-img" width="36" height="36" />
          <span class="brand-logo-text">PGON</span>
        </a>
        <nav class="header-nav">
          <a href="/#pipeline">Как работает</a>
          <a href="/#benefits">Преимущества</a>
          <a href="/#card">Виртуальная карта</a>
          <a href="/#tariffs">Тарифы</a>
          <a href="/#faq">FAQ</a>
          <a href="/blog.html" class="active">Блог</a>
        </nav>
        <a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer" class="btn-header-cta">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="m20.665 3.717-17.73 6.837c-1.21.486-1.203 1.161-.222 1.462l4.552 1.42 10.532-6.645c.498-.303.953-.14.579.192l-8.533 7.701h-.002l-.313 4.674c.459 0 .661-.211.918-.46l2.206-2.145 4.588 3.389c.845.466 1.455.226 1.666-.783l3.007-14.166c.309-1.238-.474-1.8-1.282-1.439z"/></svg>
          Открыть в Telegram
        </a>
      </div>
    </div>
  </header>

  <main class="blog-section">
    <div class="container">
      <div class="blog-hero">
        <span class="blog-badge">База знаний и статьи</span>
        <h1>Блог и аналитика <span class="gradient-text">PGON Wallet</span></h1>
        <p>Практические руководства по международным расчетам, оплате ИИ-сервисов, работе с СБП и юридической защите криптоактивов.</p>
      </div>

      <div class="blog-grid">
        {catalog_cards_html}
      </div>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/#hero" class="brand-logo">
            <img src="/assets/pgon-icon.png" alt="PGON Wallet" class="brand-logo-img" width="36" height="36" />
            <span class="brand-logo-text">PGON</span>
          </a>
          <p>Инновационный платежный Web3-шлюз нового поколения. Мгновенные расчеты по СБП напрямую с баланса USDT и TON по всей России</p>
        </div>
        <div class="footer-col">
          <h4>Навигация</h4>
          <ul>
            <li><a href="/#hero">Главная</a></li>
            <li><a href="/#pipeline">Как это работает</a></li>
            <li><a href="/#benefits">Преимущества</a></li>
            <li><a href="/#card">Виртуальная карта</a></li>
            <li><a href="/#cases">Сценарии использования</a></li>
            <li><a href="/#tariffs">Тарифная сетка</a></li>
            <li><a href="/#faq">База знаний FAQ</a></li>
            <li><a href="/blog.html">Блог и гайды</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Продукты</h4>
          <ul>
            <li><a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer">PGON Virtual Card (Visa/MC)</a></li>
            <li><a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer">Telegram Mini App</a></li>
            <li><a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer">PGON Pay для бизнеса</a></li>
            <li><a href="https://t.me/pgon_wallet_bot" target="_blank" rel="noopener noreferrer">Реферальная программа</a></li>
            <li><a href="https://t.me/pgon_support_bot" target="_blank" rel="noopener noreferrer">API документация</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Юридическая информация</h4>
          <ul>
            <li><a href="/terms.html">Пользовательское соглашение</a></li>
            <li><a href="/privacy.html">Политика конфиденциальности</a></li>
            <li><a href="/aml-cft.html">Политика AML & KYC</a></li>
            <li><a href="/cookies.html">Политика файлов Cookie</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <div class="footer-bottom-left">
          <p>© 2026 PGON Technologies Ltd. InterSpin LLC.<br>Все права защищены</p>
        </div>
        <div class="footer-bottom-right">
          <p>Криптоактивы сопряжены с рыночной волатильностью.<br>Сервис не предоставляет финансовых консультаций</p>
        </div>
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog_index_html)
print("Generated blog.html")
