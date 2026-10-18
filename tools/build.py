#!/usr/bin/env python3
"""Generates the static HTML pages of the ART COOK site.

Run from the repo root:  python3 tools/build.py
All content lives in the DATA section below; layout mirrors the Figma file
(pages 05 Desktop Screens and 06 Responsive Screens).
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
BASE_SCRIPT = """<script>(function(){var p=location.pathname.split('/');var b=(location.hostname.indexOf('github.io')>-1&&p[1])?'/'+p[1]+'/':'/';document.write('<base href="'+b+'">');})();</script>
"""
SITE_URL = "https://tanyaaisen07-uiux.github.io/art-cook/"

PHONE = "+7 701 000 00 00"
PHONE_TEL = "+77010000000"
WHATSAPP = "https://wa.me/77010000000"
ADDRESS = "г. Алматы, ул. Весновка 65"

# ------------------------------------------------------------------ DATA
COURSES = [
    dict(
        slug="basic", page="course-basic.html", group="beginner", kind="Для начинающих",
        title="Базовый кулинарный курс", weeks="4 недели", price="от 90 000 ₸",
        icon="course-basic", animated=True,
        photo="course-basic", card="card-basic",
        short="Техники нарезки, бульоны, соусы и блюда мировой кухни. Курс для тех, кто начинает с нуля.",
        catalog_text="Вы изучите все важнейшие моменты приготовления еды: от техник нарезки и бульонов до соусов, различных блюд и сложных гастрономических конструкций. Научитесь понимать правила разделки и сочетания продуктов и узнаете тонкости блюд мировой кухни. Курс подходит тем, у кого начальный уровень знаний или нет его совсем.",
        page_text="Вы изучите все важнейшие моменты приготовления еды: от техник нарезки и бульонов до соусов, различных блюд и сложных гастрономических конструкций. Научитесь понимать правила разделки и сочетания продуктов и узнаете тонкости блюд мировой кухни. Курс подходит тем, у кого начальный уровень знаний или нет его совсем.",
        sessions=["Овощи", "Рыба", "Курица", "Мясо"],
        for_whom=["Начинающим и тем, кто только учится готовить",
                  "Домашним поварам, которые хотят системных знаний",
                  "Тем, кто хочет понять технику, а не только рецепты"],
        reviews=[("Арсен", "Шеф объясняет просто и терпеливо, а всё готовим своими руками. После курса готовлю дома с удовольствием."),
                 ("Татьяна А.", "Очень атмосферные занятия. Теперь мои блюда получаются так, что семья просит добавки."),
                 ("Алия", "Тёплая атмосфера и понятная подача. Обязательно приду на следующий курс.")],
    ),
    dict(
        slug="mediterranean", page="course-mediterranean.html", group="thematic", kind="Тематический курс",
        title="Курс Средиземноморской кухни", weeks="4 недели", price="от 90 000 ₸",
        icon="course-mediterranean", animated=True,
        photo="photo-mediterranean", card="card-mediterranean",
        short="Традиционная средиземноморская кухня: секреты и особенности популярных блюд.",
        catalog_text="Вы приобретёте полезные теоретические знания и практические навыки приготовления популярных блюд. Освоите секреты и особенности традиционной средиземноморской кухни и научитесь готовить как настоящие профессионалы, легко и быстро.",
        page_text="Вы приобретёте полезные теоретические знания и практические навыки приготовления популярных блюд. Освоите секреты и особенности приготовления блюд традиционной Средиземноморской кухни. Научитесь готовить как настоящие профессионалы, легко и быстро использовать все кулинарные приёмы для выполнения блюд средиземноморской кухни.",
        sessions=["Овощи", "Рыба", "Курица", "Мясо"],
        for_whom=["Гурманам и поварам, желающим поднять кулинарные навыки на новый уровень"],
        reviews=None,
    ),
    dict(
        slug="eastern", page="course-eastern.html", group="thematic", kind="Тематический курс",
        title="Курс Восточной кухни", weeks="3 недели", price="от 70 000 ₸",
        icon="course-eastern", animated=True,
        photo="course-eastern", card="card-eastern",
        short="Основы азиатской кухни: приёмы, сочетания и здоровая, питательная еда.",
        catalog_text="Для тех, кто испытывает огромную любовь к Восточной кухне. Кулинары стран Азии достигли совершенства в искусстве сочетать, на первый взгляд, самые несочетаемые продукты. Мы научим вас этому искусству.",
        page_text="Для тех, кто испытывает огромную любовь к Восточной кухне. Кулинары стран Азии достигли совершенства в искусстве гармоничного комбинирования, на первый взгляд, самых несочетаемых продуктов. Мы научим вас этому искусству: благодаря курсу вы приобретёте навыки и знания в этом направлении кулинарии.",
        sessions=["Овощи", "Рыба", "Мясо"],
        for_whom=["Любителям экзотической кухни и тем, кто хочет освоить приёмы восточной кулинарии"],
        reviews=None,
    ),
    dict(
        slug="healthy", page="course-healthy.html", group="thematic", kind="Тематический курс",
        title="Курс Здорового питания", weeks="3 недели", price="от 90 000 ₸",
        icon="course-healthy", animated=True,
        photo="course-healthy", card="card-healthy",
        short="Принципы правильного питания: готовим вкусно, сохраняя свежесть и пользу.",
        catalog_text="Вы научитесь выбирать полезные продукты и готовить вкусные блюда. Расскажем о 4 законах правильного питания, планировании меню и балансе рациона.",
        page_text="Вы научитесь выбирать полезные продукты и готовить вкусные блюда. Расскажем о 4 законах правильного питания, планировании меню и балансе рациона.",
        sessions=["Овощи", "Фрукты", "Крупы", "Рыба, мясо, курица"],
        for_whom=["Тем, кто хочет готовить вкусно и полезно, сохраняя свежесть продуктов"],
        reviews=None,
    ),
]
NEW_COURSES = [
    dict(slug="italian", group="thematic", kind="Новый курс", title="Курс Итальянской кухни",
         icon="course-italian", photo="mc-italian",
         meta=["Продолжительность: сообщим при старте набора", "Стоимость: по запросу"],
         note="Предварительная запись уже открыта",
         text="Курс готовится к запуску. Оставьте заявку, и мы первыми пригласим вас в группу."),
    dict(slug="pastry", group="thematic", kind="Новый курс", title="Кондитерский курс",
         icon="course-pastry", photo="course-pastry",
         meta=["Продолжительность: сообщим при старте набора", "Стоимость: по запросу"],
         note="Предварительная запись уже открыта",
         text="Скоро откроем набор. Оставьте заявку, чтобы одним из первых узнать программу и даты."),
    dict(slug="pro", group="thematic", kind="Новый курс · продвинутый уровень", title="Курс для профессионалов",
         icon="course-pro", photo="course-pro",
         meta=["Продолжительность: сообщим при старте набора", "Стоимость: по запросу"],
         note="Предварительная запись уже открыта",
         text="Программу собираем вместе с шефом. Оставьте заявку, и мы расскажем, что в неё войдёт."),
    dict(slug="individual", group="individual", kind="Индивидуально", title="Индивидуальный курс",
         icon="course-individual", photo="photo-onsite",
         meta=["Продолжительность: под ваши цели", "Стоимость: зависит от программы"],
         note="Даты занятий выстраиваются индивидуально, с учётом ваших возможностей",
         text="Шеф составит программу под ваши цели, уровень подготовки и удобный график."),
]
ALL_TITLES = [(c["slug"], c["title"]) for c in COURSES] + [(c["slug"], c["title"]) for c in NEW_COURSES] + [
    ("masterclass", "Мастер-класс"), ("onsite", "Выездной мастер-класс")]

MASTERCLASSES = [
    dict(photo="mc-vietnam", sub="Вьетнамской кухни", seats="10 мест",
         text="Кулинарный класс для любителей экзотики: блюда Вьетнама, проводит шеф-повар."),
    dict(photo="mc-italian", sub="Итальянское свидание", seats="8 мест",
         text="Для тех, кто хочет совершить путешествие в солнечную Италию, не выезжая из города."),
]
HOME_REVIEWS = [
    ("Арсен", "Базовый кулинарный курс", "Пришёл почти с нуля, а через месяц уверенно готовлю бульоны и соусы. Шеф объясняет просто и терпеливо."),
    ("Татьяна А.", "Курс Средиземноморской кухни", "Очень атмосферные занятия. Теперь рыба и овощи у меня получаются так, что семья просит добавки."),
    ("Алия", "Мастер-класс «Итальянское свидание»", "Ходили на мастер-класс вдвоём и получили настоящий вечер-путешествие. Обязательно вернёмся на курс."),
]
NAV = [("about.html", "О школе"), ("courses.html", "Курсы"), ("master-classes.html", "Мастер-классы"),
       ("prices.html", "Цены"), ("gift.html", "Сертификаты"), ("contacts.html", "Контакты")]

# ------------------------------------------------------------------ HELPERS
def e(s):
    return escape(s, quote=True)

def icon(name, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="assets/svg/icons.svg#{name}"></use></svg>'

def img(name, alt="", cls="", w=None, h=None, eager=False, ext="jpg"):
    attrs = f' class="{cls}"' if cls else ""
    if w and h:
        attrs += f' width="{w}" height="{h}"'
    loading = "" if eager else ' loading="lazy" decoding="async"'
    return f'<img src="assets/img/{name}.{ext}" alt="{e(alt)}"{attrs}{loading}>'

def heading(title, eyebrow=None, subtitle=None, center=False, tag="h2", cls="h2"):
    out = f'<div class="sh{" sh--center" if center else ""}">'
    if eyebrow:
        out += f'<p class="overline">{e(eyebrow)}</p>'
    out += f'<{tag} class="{cls}">{title}</{tag}><span class="sh__divider" aria-hidden="true"></span>'
    if subtitle:
        out += f'<p class="sh__subtitle">{subtitle}</p>'
    return out + "</div>"

def crumbs(*items):
    parts = ['<a href="index.html">Главная</a>']
    for href, label in items[:-1]:
        parts.append(f'<a href="{href}">{e(label)}</a>')
    parts.append(f'<span aria-current="page">{e(items[-1][1])}</span>')
    return '<nav class="crumbs" aria-label="Хлебные крошки">' + '<span aria-hidden="true">/</span>'.join(parts) + "</nav>"

def btn(label, href=None, kind="primary", ico=None, attrs="", cls=""):
    inner = e(label) + (icon(ico) if ico else "")
    c = f"btn btn--{kind} {cls}".strip()
    if href:
        return f'<a class="{c}" href="{href}" {attrs}>{inner}</a>'
    return f'<button type="button" class="{c}" {attrs}>{inner}</button>'

def link(label, href=None, ico="arrow-right", attrs=""):
    inner = e(label) + icon(ico, "icon icon-20")
    if href:
        return f'<a class="link" href="{href}" {attrs}>{inner}</a>'
    return f'<button type="button" class="link" {attrs}>{inner}</button>'

CALLBACK = 'data-open="callback"'

def course_card(c):
    return f'''<div class="course-item">
  <a class="course-card" href="{c["page"]}">
    <div class="course-card__photo">{img(c["card"], c["title"], w=540, h=300)}</div>
    <div class="course-card__body">
      <div class="course-card__titles"><h3 class="h4">{e(c["title"])}</h3><p class="body course-card__meta">{c["weeks"]} · {c["price"]}</p></div>
      <p class="body-s">{e(c["short"])}</p>
    </div>
  </a>
  {btn("Записаться на курс", f'booking.html?course={c["slug"]}', cls="btn--block")}
</div>'''

def mc_card(m):
    return f'''<button type="button" class="mc-card" {CALLBACK} data-topic="Мастер-класс {e(m["sub"])}">
  <div class="mc-card__photo">{img(m["photo"], "Мастер-класс " + m["sub"], w=548, h=300)}</div>
  <div class="mc-card__body">
    <div class="mc-card__row"><div class="mc-card__titles"><p class="h4">Мастер-класс</p><p class="body text-highlight">{e(m["sub"])}</p></div><p class="mc-card__seats">{m["seats"]}</p></div>
    <p class="body-s">{e(m["text"])}</p>
  </div>
</button>'''

def stars():
    return '<div class="stars" role="img" aria-label="Оценка 5 из 5">' + icon("star-fill") * 5 + "</div>"

def review(name, course, text):
    return f'''<figure class="review">{stars()}<blockquote class="body">{e(text)}</blockquote><figcaption class="review__author"><span class="review__name">{e(name)}</span><span class="caption text-muted">{e(course)}</span></figcaption></figure>'''

def field(label, name, ph="", typ="text", req=False, helper="", extra=""):
    star = " *" if req else ""
    r = " required" if req else ""
    return f'''<div class="field" data-field="{name}">
  <label class="field__label" for="f-{name}{extra}">{e(label)}{star}</label>
  <div class="field__control"><input id="f-{name}{extra}" name="{name}" type="{typ}" placeholder="{e(ph)}"{r}{' inputmode="tel" autocomplete="tel"' if typ=="tel" else ''}{' autocomplete="name"' if name=="name" else ''}{' autocomplete="email"' if typ=="email" else ''}></div>
  <p class="field__helper">{e(helper)}</p>
</div>'''

def select(label, name, options, req=False, placeholder=None, selected=None, helper="", extra=""):
    star = " *" if req else ""
    opts = ""
    if placeholder:
        opts += f'<option value="" disabled{"" if selected else " selected"}>{e(placeholder)}</option>'
    for v, t in options:
        s = " selected" if selected == v else ""
        opts += f'<option value="{e(v)}"{s}>{e(t)}</option>'
    return f'''<div class="field" data-field="{name}">
  <label class="field__label" for="f-{name}{extra}">{e(label)}{star}</label>
  <div class="field__control"><select id="f-{name}{extra}" name="{name}"{' required' if req else ''}>{opts}</select>{icon("chevron-down", "icon field__chevron")}</div>
  <p class="field__helper">{e(helper)}</p>
</div>'''

def consent(extra=""):
    return f'''<label class="check" data-field="consent"><input type="checkbox" name="consent" required id="f-consent{extra}"><span>Согласен на обработку персональных данных. <a href="privacy.html">Политика конфиденциальности</a></span></label><p class="form-error">Подтвердите согласие на обработку данных</p>'''

# ------------------------------------------------------------------ LAYOUT
def header(active):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    mnav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}{icon("chevron-right")}</a>' for h, t in NAV)
    return f'''<a class="skip-link" href="#main">Перейти к содержанию</a>
<header class="header">
  <div class="header__bar">
    <a class="header__logo" href="index.html" aria-label="ART COOK, на главную"><img src="assets/svg/logo.svg" alt="ART COOK" width="100" height="100"></a>
    <nav class="nav" aria-label="Основное меню">{nav}</nav>
    <div class="header__contact"><a class="header__phone" href="tel:{PHONE_TEL}">{PHONE}</a><button type="button" class="header__callback" {CALLBACK}>Обратный звонок</button></div>
    {btn("Записаться", "booking.html", cls="header__cta")}
    <span class="header__spacer"></span>
    <a class="header__icon-btn" href="tel:{PHONE_TEL}" aria-label="Позвонить {PHONE}">{icon("phone")}</a>
    <button type="button" class="header__icon-btn" aria-label="Открыть меню" aria-expanded="false" aria-controls="menu" data-menu-open>{icon("menu")}</button>
  </div>
</header>
<div class="menu" id="menu" role="dialog" aria-modal="true" aria-label="Меню">
  <div class="menu__bar"><a href="index.html" aria-label="На главную"><img src="assets/svg/logo.svg" alt="ART COOK" width="56" height="56"></a><span class="header__spacer"></span><button type="button" class="header__icon-btn" aria-label="Закрыть меню" data-menu-close style="display:inline-flex">{icon("close")}</button></div>
  <nav class="menu__list" aria-label="Меню">{mnav}</nav>
  <div class="menu__actions">
    {btn("Записаться", "booking.html", cls="btn--block")}
    {btn("Обратный звонок", kind="secondary", attrs=CALLBACK, cls="btn--block")}
    <a class="menu__phone" href="tel:{PHONE_TEL}">{PHONE}</a>
    <p class="menu__addr">{ADDRESS}</p>
  </div>
</div>'''

def footer():
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<footer class="footer">
  <div class="container footer__inner">
    <div class="footer__logo-row"><a href="index.html" aria-label="ART COOK, на главную"><img src="assets/svg/logo-footer.svg" alt="ART COOK" width="110" height="110" loading="lazy"></a></div>
    <nav class="footer__nav" aria-label="Меню в подвале">{nav}</nav>
    <p class="footer__addr">{ADDRESS} · <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
    <div class="socials">
      <a class="social" href="https://www.instagram.com/" target="_blank" rel="noopener" aria-label="Instagram">{icon("instagram")}</a>
      <a class="social" href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="WhatsApp">{icon("whatsapp")}</a>
      <a class="social" href="https://t.me/" target="_blank" rel="noopener" aria-label="Telegram">{icon("telegram")}</a>
    </div>
    <div class="footer__bottom"><a href="contacts.html#partners">Партнёрам</a><a href="privacy.html">Политика конфиденциальности</a><span>© ART COOK, <span data-year>2026</span></span></div>
  </div>
</footer>'''

def callback_modal():
    times = [("Любое", "Любое"), ("10:00–13:00", "Утром, 10:00–13:00"), ("13:00–17:00", "Днём, 13:00–17:00"), ("17:00–20:00", "Вечером, 17:00–20:00")]
    return f'''<div class="modal" id="callback" aria-hidden="true">
  <div class="modal__scrim" data-close></div>
  <div class="modal__dialog" role="dialog" aria-modal="true" aria-labelledby="cb-title">
    <div data-state="form" class="stack gap-20">
      <div class="modal__top"><h2 class="h4" id="cb-title">Обратный звонок</h2><button type="button" class="modal__close" aria-label="Закрыть" data-close>{icon("close")}</button></div>
      <p class="body">Оставьте телефон, и мы перезвоним в рабочее время</p>
      <form class="form js-form" data-kind="callback" novalidate>
        <input type="hidden" name="topic" value="Обратный звонок">
        <p class="caption text-muted">* обязательные поля</p>
        {field("Имя", "name", "Введите имя", req=True, helper="Укажите имя", extra="-cb")}
        {field("Телефон", "phone", "+7 (___) ___-__-__", typ="tel", req=True, helper="Введите номер полностью: +7 (XXX) XXX-XX-XX", extra="-cb")}
        {select("Удобное время", "time", times, selected="Любое", extra="-cb")}
        {consent("-cb")}
        <button type="submit" class="btn btn--primary btn--block">Перезвоните мне{icon("phone")}</button>
      </form>
    </div>
    <div data-state="success" class="stack gap-20">
      <div class="modal__top"><h2 class="h4">Спасибо!</h2><button type="button" class="modal__close" aria-label="Закрыть" data-close>{icon("close")}</button></div>
      <p class="body">Мы перезвоним вам в рабочее время.</p>
      <button type="button" class="btn btn--secondary btn--block" data-close>Закрыть</button>
    </div>
  </div>
</div>'''

def page(fname, title, desc, active, body, extra_body_class="", noindex=False, head=""):
    full_title = title if title.startswith("ART COOK") else f"{title} | ART COOK"
    html = f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
{head}<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<meta property="og:type" content="website">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE_URL}assets/img/hero.jpg">
<meta property="og:locale" content="ru_RU">
<meta name="theme-color" content="#644336">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/svg/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/lora-cyrillic-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/fonts.css">
<link rel="stylesheet" href="assets/css/tokens.css">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body class="{extra_body_class}">
{header(active)}
<main id="main">
{body}
</main>
{footer()}
{callback_modal()}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''
    (ROOT / fname).write_text(html, encoding="utf-8")

# ------------------------------------------------------------------ PAGES
def home():
    tiles = [
        ("cat-courses", "Курсы", "Обучение для гурманов, начинающих и домашних поваров", "courses.html"),
        ("cat-masterclasses", "Мастер-классы", "Практические кулинарные классы и дегустации с шеф-поваром", "master-classes.html"),
        ("photo-mediterranean", "Индивидуальный курс", "Программа и даты под ваши цели", "courses.html?filter=individual"),
        ("photo-onsite", "Выездной мастер-класс", "Шеф приезжает к вам на праздник или корпоратив", "master-classes.html#onsite"),
    ]
    tiles_html = "".join(f'''<a class="tile" href="{h}"><div class="tile__photo">{img(p, "", w=263, h=180)}</div><h3 class="tile__title">{t}</h3><p class="tile__text">{d}</p><span class="link">Узнать больше{icon("arrow-right", "icon icon-20")}</span></a>''' for p, t, d, h in tiles)
    partners_one = f'''<div class="partner">{'<img src="assets/svg/partner-olivenna.svg" alt="" width="41" height="47">'}<span class="partner__olivenna">Olivenna</span></div>
<div class="partner"><img src="assets/svg/partner-tuzly-kitchen.svg" alt="" width="30" height="40"><span class="partner__wm"><b>TUZLY</b><small>KITCHEN</small></span></div>
<div class="partner"><img src="assets/svg/partner-green-plate-almaty.svg" alt="" width="40" height="40"><span class="partner__wm partner__wm--gp"><b>Green Plate</b><small>ALMATY</small></span></div>'''
    track = partners_one * 2
    body = f'''
<section class="hero" aria-labelledby="hero-title">
  {img("hero", "", cls="hero__bg", eager=True)}
  <div class="hero__content">
    <h1 class="hero__title" id="hero-title"><span class="t1">КУЛИНАРНАЯ ШКОЛА </span><span class="t2">ART COOK</span></h1>
    <p class="hero__sub">Курсы и мастер-классы для начинающих и домашних поваров</p>
    {btn("Выбрать курс", "courses.html", ico="edit")}
  </div>
</section>

<section class="section">
  <div class="container stack-60">
    {heading("Готовить это искусство", subtitle="Откройте для себя радость приготовления, используя лучшие ингредиенты, и узнайте секреты опытных поваров", center=True)}
    <div class="scroller"><div class="tiles scroller__track">{tiles_html}</div><button type="button" class="scroll-hint" aria-label="Листать дальше" data-scroll-next>{icon("chevron-right")}</button></div>
  </div>
</section>

<section class="section section--flush-top">
  <div class="container stack-60" style="align-items:center">
    {heading("Выберите свой курс", eyebrow="Ближайшие курсы", center=True)}
    <div class="scroller w-100"><div class="cards-2 scroller__track">{"".join(course_card(c) for c in COURSES)}</div><button type="button" class="scroll-hint" aria-label="Листать дальше" data-scroll-next>{icon("chevron-right")}</button></div>
    {link("Все курсы", "courses.html")}
  </div>
</section>

<section class="section section--cream">
  <div class="container stack-60" style="align-items:center">
    {heading("Предстоящие мастер-классы", center=True)}
    <div class="mc-cards mc-cards--home w-100">{"".join(mc_card(m) for m in MASTERCLASSES)}</div>
    {link("Все мастер-классы", "master-classes.html")}
  </div>
</section>

<section class="section">
  <div class="container founder">
    <div class="founder__text">
      {heading("О создателе школы", subtitle="Бренд-шеф кулинарной школы ART COOK Абитов Тамир", center=True)}
      <div class="body">
        <p>В сфере кулинарии более 10 лет. Музыкальное и экономическое образование помогли раскрыть творческий подход, а обучение у профессионалов в Испании (школа BellArt) убедило: еда это прежде всего культура. Любовь к профессии выражается в творчестве, поиске совершенства и во «вкусном» общении с людьми через еду.</p>
        <p style="margin-top:30px">Главное приобретение на наших кулинарных курсах: гастрономическая гармония, навыки и знания, позволяющие готовить с удовольствием и вкусно!</p>
      </div>
    </div>
    <div class="photo-frame">{img("chef", "Абитов Тамир, бренд-шеф ART COOK", w=400, h=400)}</div>
  </div>
</section>

<section class="section section--cream">
  <div class="container stack-60">
    {heading("Что говорят ученики", eyebrow="Отзывы", center=True)}
    <div class="cards-3">{"".join(review(n, c, t) for n, c, t in HOME_REVIEWS)}</div>
  </div>
</section>

<section class="section section--cream">
  <div class="container gift-split">
    <div class="gift-card">
      {heading("Подарочный сертификат", eyebrow="Подарок")}
      <p class="body">Закажите подарочную карту ART COOK и удивите знакомых и родных на день рождения или по особому случаю. Это уместный подарок для того, у кого есть всё.</p>
      {btn("Заказать сертификат", "gift.html", ico="edit")}
    </div>
    <div class="gift-split__photo">{img("gift-box", "Подарочная карта ART COOK", w=520, h=464)}</div>
  </div>
</section>

<section class="section">
  <div class="container stack" style="align-items:center;gap:40px">
    {heading("Наши партнёры", center=True)}
    <div class="marquee" aria-label="Партнёры: Olivenna, Tuzly Kitchen, Green Plate Almaty"><div class="marquee__track" aria-hidden="true">{track}</div></div>
    {btn("Стать партнёром", "contacts.html#partners", kind="secondary", cls="btn--m-block")}
  </div>
</section>

<section class="lead" aria-labelledby="lead-title">
  <div class="lead__form">
    {heading('<span id="lead-title">Оставить заявку на курс</span>')}
    <form class="form js-form" data-kind="lead" novalidate>
      <p class="caption text-muted">* обязательные поля</p>
      {field("Имя", "name", "Введите имя", req=True, helper="Укажите имя", extra="-lead")}
      {field("Телефон", "phone", "+7 (___) ___-__-__", typ="tel", req=True, helper="Введите номер полностью: +7 (XXX) XXX-XX-XX", extra="-lead")}
      {field("Email (необязательно)", "email", "name@mail.kz", typ="email", helper="Проверьте адрес почты", extra="-lead")}
      {select("Курс", "course", ALL_TITLES, req=True, placeholder="Выберите курс", helper="Выберите курс", extra="-lead")}
      {consent("-lead")}
      <div><button type="submit" class="btn btn--primary btn--m-block">Отправить заявку{icon("edit")}</button></div>
      <p class="body js-form-success" hidden role="status">Спасибо! Заявка принята, менеджер свяжется с вами в рабочее время.</p>
    </form>
  </div>
  <div class="lead__photo">{img("photo-onsite", "Ученики готовят на кухне ART COOK")}</div>
</section>
'''
    page("index.html", "ART COOK: кулинарная школа в Алматы",
         "Курсы и мастер-классы для начинающих и домашних поваров в Алматы. Базовый курс, средиземноморская, восточная кухня, здоровое питание, подарочные сертификаты.",
         "index.html", body)

def courses():
    chips = [("all", "Все"), ("beginner", "Для начинающих"), ("thematic", "Тематические"), ("individual", "Индивидуальный")]
    chips_html = "".join(f'<button type="button" class="chip" data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{t}</button>' for k, t in chips)
    blocks = []
    i = 0
    for c in COURSES:
        rev = " block--rev" if i % 2 else ""
        sess = "".join(f"<li>Сессия {n}: {s}</li>" for n, s in enumerate(c["sessions"], 1))
        blocks.append(f'''<article class="block{rev}" id="{c["slug"]}" data-group="{c["group"]}">
  <a class="block__photo" href="{c["page"]}" tabindex="-1" aria-hidden="true">{img(c["photo"], "", w=500, h=760)}</a>
  <div class="block__info">
    <div class="block__head"><span class="course-icon" data-gif="assets/icons/{c["icon"]}.gif"><img src="assets/icons/{c["icon"]}.png" alt="" width="80" height="80"></span><p class="overline">{c["kind"]}</p><h2 class="h3">{e(c["title"])}</h2></div>
    <div class="block__meta"><p>Продолжительность: {c["weeks"]}</p><p>Стоимость: {c["price"]}</p><p class="body-s">Даты занятий выстраиваются индивидуально, с учётом ваших возможностей</p></div>
    <p class="body">{e(c["catalog_text"])}</p>
    <ul class="sessions">{sess}</ul>
    <div class="actions">{btn("Забронировать место", f'booking.html?course={c["slug"]}')}{link("Подробнее о курсе", c["page"])}</div>
  </div>
</article>''')
        i += 1
    for c in NEW_COURSES:
        rev = " block--rev" if i % 2 else ""
        meta = "".join(f"<p>{m}</p>" for m in c["meta"])
        blocks.append(f'''<article class="block{rev}" id="{c["slug"]}" data-group="{c["group"]}">
  <div class="block__photo">{img(c["photo"], c["title"], w=500, h=560)}</div>
  <div class="block__info">
    <div class="block__head"><span class="course-icon course-icon--static"><img src="assets/icons/{c["icon"]}.png" alt="" width="50" height="50"></span><p class="overline">{c["kind"]}</p><h2 class="h3">{e(c["title"])}</h2></div>
    <div class="block__meta">{meta}<p class="body-s">{c["note"]}</p></div>
    <p class="body">{e(c["text"])}</p>
    <div class="actions">{btn("Оставить заявку", f'booking.html?course={c["slug"]}')}{link("Задать вопрос", attrs=CALLBACK + f' data-topic="Вопрос: {e(c["title"])}"')}</div>
  </div>
</article>''')
        i += 1
    body = f'''
<section class="section section--intro">
  <div class="container stack-60">
    {crumbs(("courses.html", "Курсы"))}
    {heading("Курсы ART COOK", subtitle="Кулинарные курсы для начинающих и домашних поваров.<br>Даты занятий подбираются индивидуально.", tag="h1")}
    <div class="stack gap-20">
      <div class="chips" role="group" aria-label="Фильтр курсов">{chips_html}</div>
      <p class="body-s text-muted" id="filter-info" aria-live="polite">Показаны все курсы: 8</p>
    </div>
  </div>
</section>
<section class="section section--flush-top">
  <div class="container blocks">{"".join(blocks)}</div>
</section>
<section class="section section--cream">
  <div class="container stack" style="align-items:center;gap:30px">
    {heading("Не знаете, какой курс выбрать?", subtitle="Оставьте телефон, и мы поможем подобрать программу", center=True)}
    <div class="actions actions--center actions--m-stack">{btn("Обратный звонок", ico="phone", attrs=CALLBACK)}{btn("Сравнить цены", "prices.html", kind="secondary")}</div>
  </div>
</section>'''
    page("courses.html", "Курсы", "Кулинарные курсы ART COOK в Алматы: для начинающих, тематические и индивидуальные. Даты занятий подбираются индивидуально.", "courses.html", body)

def course_page(c):
    others = [o for o in COURSES if o is not c][:3]
    facts = f'''<div class="facts"><div class="fact"><p class="overline">Продолжительность</p><p class="h5">{c["weeks"]}</p></div><div class="fact"><p class="overline">Стоимость</p><p class="h5">{c["price"]}</p></div><div class="fact"><p class="overline">Даты</p><p class="h5">индивидуально</p></div></div>'''
    steps = "".join(f'<li class="step"><div class="step__marker"><span class="step__num">{n}</span></div><div class="step__text"><p class="overline">Сессия {n}</p><p class="h4">{s}</p></div></li>' for n, s in enumerate(c["sessions"], 1))
    revs = c["reviews"] or COURSES[0]["reviews"]
    reviews = "".join(review(n, c["title"], t) for n, t in revs)
    bullets = "".join(f"<li>{b}</li>" for b in c["for_whom"])
    body = f'''
<section class="section section--intro">
  <div class="container stack-60">
    {crumbs(("courses.html", "Курсы"), (c["page"], c["title"]))}
    <div class="course-hero">
      <div class="course-hero__photo">{img(c["photo"], c["title"], w=480, h=718, eager=True)}</div>
      <div class="course-hero__info">
        <span class="course-icon" data-gif="assets/icons/{c["icon"]}.gif"><img src="assets/icons/{c["icon"]}.png" alt="" width="80" height="80"></span>
        <h1 class="h1">{e(c["title"])}</h1>
        {facts}
        <p class="body">{e(c["page_text"])}</p>
        <div class="actions actions--m-stack">{btn("Записаться на курс", f'booking.html?course={c["slug"]}')}{link("Задать вопрос", attrs=CALLBACK + f' data-topic="Вопрос: {e(c["title"])}"')}</div>
      </div>
    </div>
  </div>
</section>
<section class="section section--cream">
  <div class="container stack-60">
    {heading("Программа курса", eyebrow=f'{c["weeks"]} · {len(c["sessions"])} сессии')}
    <ol class="timeline" style="--steps:{len(c["sessions"])};padding:0;margin:0;list-style:none">{steps}</ol>
  </div>
</section>
<section class="section">
  <div class="container split-2">
    <div class="panel panel--border"><h2 class="h4">Для кого этот курс</h2><ul class="bullets body stack gap-20">{bullets}</ul></div>
    <div class="panel panel--beige"><h2 class="h4">Ведёт курс</h2><div class="chef-row">{img("chef", "Абитов Тамир", w=88, h=88)}<div><p class="h5">Абитов Тамир, бренд-шеф ART COOK</p><p class="body-s">10+ лет в кулинарии · школа BellArt, Испания</p></div></div><div>{link("Команда школы", "about.html")}</div></div>
  </div>
</section>
<section class="section section--cream">
  <div class="container stack-60">
    {heading("Что говорят ученики курса", eyebrow="Отзывы", center=True)}
    <div class="cards-3">{reviews}</div>
  </div>
</section>
<section class="section">
  <div class="container stack-60">
    {heading("Другие курсы ART COOK", center=True)}
    <div class="scroller"><div class="cards-3 scroller__track">{"".join(course_card(o) for o in others)}</div><button type="button" class="scroll-hint" aria-label="Листать дальше" data-scroll-next>{icon("chevron-right")}</button></div>
  </div>
</section>
<div class="sticky-cta"><div class="sticky-cta__price"><span>Стоимость</span><b>{c["price"]}</b></div>{btn("Записаться", f'booking.html?course={c["slug"]}')}</div>
'''
    page(c["page"], c["title"], f'{c["title"]} в кулинарной школе ART COOK, Алматы: {c["weeks"]}, {c["price"]}. {c["short"]}', "courses.html", body, "has-sticky-cta")

def masterclasses():
    body = f'''
<section class="section section--intro">
  <div class="container stack-60">
    {crumbs(("master-classes.html", "Мастер-классы"))}
    {heading("Мастер-классы", subtitle="Мастер-класс проходит в школе ART COOK под руководством профессионального шеф-повара. За несколько часов в непринуждённой обстановке вы приготовите оригинальный обед или тематический ужин.", tag="h1")}
  </div>
</section>
<section class="section section--cream" style="padding-top:80px">
  <div class="container stack-60">
    {heading("Предстоящие мастер-классы").replace('<span class="sh__divider" aria-hidden="true"></span>', '')}
    <div class="mc-cards">{"".join(mc_card(m) for m in MASTERCLASSES)}</div>
  </div>
</section>
<section class="section section--cream" id="onsite">
  <div class="container split">
    <div class="split__text">
      {heading("Выездной мастер-класс", eyebrow="Для праздников и компаний")}
      <p class="body">Шеф приезжает к вам: день рождения, корпоратив или семейный ужин. Программу и меню подбираем под повод и количество гостей.</p>
      {btn("Заказать выездной", "booking.html?course=onsite")}
    </div>
    <div class="split__photo">{img("photo-onsite", "Выездной мастер-класс", w=520, h=420)}</div>
  </div>
</section>
<section class="section">
  <div class="container stack" style="align-items:center;gap:30px">
    {heading("Подарите мастер-класс", subtitle="Сертификат на мастер-класс: приятный подарок для тех, кто любит готовить", center=True)}
    {btn("Подарочный сертификат", "gift.html", kind="secondary", ico="gift", cls="btn--m-block")}
  </div>
</section>'''
    page("master-classes.html", "Мастер-классы", "Кулинарные мастер-классы с шеф-поваром ART COOK в Алматы и выездные мастер-классы для праздников и компаний.", "master-classes.html", body)

def prices():
    rows = [(c["title"], c["weeks"], ", ".join(s.lower() if i else s for i, s in enumerate(c["sessions"])), c["price"], "Записаться", f'booking.html?course={c["slug"]}') for c in COURSES]
    rows[0] = (rows[0][0], rows[0][1], "Овощи, рыба, курица, мясо", rows[0][3], rows[0][4], rows[0][5])
    rows += [
        ("Индивидуальный курс", "по запросу", "по программе", "по запросу", "Оставить заявку", "booking.html?course=individual"),
        ("Мастер-класс", "несколько часов", "одно занятие", "по запросу", "Оставить заявку", "booking.html?course=masterclass"),
        ("Выездной мастер-класс", "по запросу", "по программе", "по запросу", "Оставить заявку", "booking.html?course=onsite"),
        ("Подарочный сертификат", "", "", "от 15 000 ₸", "Оставить заявку", "gift.html"),
    ]
    tr = "".join(f'<tr><td>{a}</td><td data-label="Длительность">{b}</td><td data-label="Сессии">{s}</td><td class="price">{p}</td><td>{link(l, h)}</td></tr>' for a, b, s, p, l, h in rows)
    tr = tr.replace('<td data-label="Длительность"></td>', '<td></td>').replace('<td data-label="Сессии"></td>', '<td></td>')
    body = f'''
<section class="section section--intro">
  <div class="container stack-60">
    {crumbs(("prices.html", "Цены"))}
    {heading("Цены на обучение", subtitle="Даты занятий подбираются индивидуально.<br>Точную стоимость подтвердит менеджер.", tag="h1")}
  </div>
</section>
<section class="section section--flush-top">
  <div class="container">
    <table class="price-table">
      <thead><tr><th scope="col" style="width:30%">Программа</th><th scope="col" style="width:16%">Длительность</th><th scope="col" style="width:24%">Сессии</th><th scope="col" style="width:14%">Стоимость</th><th scope="col"><span class="sr-only">Действие</span></th></tr></thead>
      <tbody>{tr}</tbody>
    </table>
  </div>
</section>
<section class="section section--cream">
  <div class="container stack" style="align-items:center;gap:30px">
    {heading("Нужна консультация?", subtitle="Перезвоним и поможем выбрать программу", center=True)}
    <div class="actions actions--center actions--m-stack">{btn("Обратный звонок", ico="phone", attrs=CALLBACK)}{btn("Все курсы", "courses.html", kind="secondary")}</div>
  </div>
</section>'''
    page("prices.html", "Цены", "Цены на кулинарные курсы и мастер-классы ART COOK в Алматы. Подарочные сертификаты от 15 000 ₸.", "prices.html", body)

def about():
    body = f'''
<section class="section section--intro">
  <div class="container stack-60">
    {crumbs(("about.html", "О школе"))}
    <div class="split">
      <div class="split__text">
        {heading("ART COOK кулинарная школа в Алматы", eyebrow="О школе", tag="h1")}
        <p class="body-l">Обучаем кулинарному искусству в доступном формате: для начинающих, домашних и профессиональных поваров. Курсы, мастер-классы и подарочные сертификаты.</p>
      </div>
      <div class="split__photo">{img("cat-masterclasses", "Кухня кулинарной школы ART COOK", w=540, h=380, eager=True)}</div>
    </div>
  </div>
</section>
<section class="section section--cream">
  <div class="container split split--400">
    <div class="split__photo">{img("chef", "Абитов Тамир, бренд-шеф ART COOK", w=400, h=460)}</div>
    <div class="split__text">
      {heading("Абитов Тамир, бренд-шеф ART COOK", eyebrow="О создателе школы")}
      <ul class="checks">
        <li>{icon("check")}<span>Более 10 лет в кулинарии</span></li>
        <li>{icon("check")}<span>Музыкальное и экономическое образование помогли раскрыть творческий подход</span></li>
        <li>{icon("check")}<span>Обучение у профессионалов в Испании, школа BellArt</span></li>
      </ul>
      <p class="quote h5">Еда это прежде всего культура</p>
      <p class="body-s">Любовь к профессии выражается в творчестве, поиске совершенства и «вкусном» общении с людьми через еду.</p>
    </div>
  </div>
</section>
<section class="section section--beige">
  <div class="container stack" style="align-items:center;gap:30px">
    {heading("Приходите учиться", center=True)}
    {btn("Выбрать курс", "courses.html", cls="btn--m-block")}
  </div>
</section>'''
    page("about.html", "О школе", "ART COOK: кулинарная школа в Алматы. Бренд-шеф Абитов Тамир, более 10 лет в кулинарии, обучение в Испании (школа BellArt).", "about.html", body)

def gift():
    types = [("gift-course", "На курс", "Любой курс школы"), ("gift-box", "На мастер-класс", "Один мастер-класс с шефом"), ("gift-amount", "На сумму", "от 15 000 ₸, номинал на выбор")]
    cards = "".join(f'<div class="gift-type">{img(p, "Сертификат " + t.lower(), w=298, h=220)}<h3 class="h5">{t}</h3><p class="body-s">{d}</p>{btn("Заказать сертификат", kind="secondary", attrs=CALLBACK + f' data-topic="Сертификат {t.lower()}"', cls="btn--block")}</div>' for p, t, d in types)
    body = f'''
<section class="section section--intro">
  <div class="container stack-60">
    {crumbs(("gift.html", "Подарочные сертификаты"))}
    <div class="split split--r520">
      <div class="split__text">
        {heading("Подарочные сертификаты от ART COOK", tag="h1")}
        <p class="body">Мастер-класс проходит в школе ART COOK под руководством профессионального шеф-повара, который с огромным удовольствием поделится с гостями секретами кулинарии и поможет вам разнообразить будничный рацион. За несколько часов в непринуждённой обстановке вы приготовите оригинальный обед или тематический ужин.</p>
        {btn("Заказать сертификат", ico="gift", attrs=CALLBACK + ' data-topic="Подарочный сертификат"')}
      </div>
      <div class="split__photo">{img("gift-intro", "Подарок от ART COOK", w=520, h=460, eager=True)}</div>
    </div>
  </div>
</section>
<section class="section section--cream">
  <div class="container stack-60">
    {heading("Выберите сертификат", subtitle="Номиналы и условия подтвердит менеджер", center=True)}
    <div class="cards-3">{cards}</div>
  </div>
</section>
<section class="section">
  <div class="container stack" style="align-items:center;gap:30px;text-align:center">
    <p class="h4" style="max-width:900px">Хотите подарить что-то необычное? Свяжитесь с нами, и мы соберём подарок специально для вас.</p>
    {link("Обратный звонок", ico="phone", attrs=CALLBACK)}
  </div>
</section>'''
    page("gift.html", "Подарочные сертификаты", "Подарочные сертификаты ART COOK на курс, мастер-класс или сумму от 15 000 ₸.", "gift.html", body)

def contacts():
    map_q = "Алматы, улица Весновка 65"
    body = f'''
<section class="section section--intro">
  <div class="container stack-60">
    {crumbs(("contacts.html", "Контакты"))}
    <div class="split split--520 split--top">
      <div class="split__text">
        {heading("Контакты", tag="h1")}
        <div class="info-item">{icon("map-pin")}<div><p class="overline">Адрес</p><p class="body-l text-heading">{ADDRESS}</p></div></div>
        <div class="info-item">{icon("phone")}<div><p class="overline">Телефон</p><a class="body-l text-heading" href="tel:{PHONE_TEL}">{PHONE}</a></div></div>
        <div class="stack gap-20" style="gap:10px"><p class="overline">Соцсети</p>
          <div class="socials" style="gap:10px">
            <a class="social social--light" href="https://www.instagram.com/" target="_blank" rel="noopener" aria-label="Instagram">{icon("instagram")}</a>
            <a class="social social--light" href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="WhatsApp">{icon("whatsapp")}</a>
            <a class="social social--light" href="https://t.me/" target="_blank" rel="noopener" aria-label="Telegram">{icon("telegram")}</a>
          </div>
        </div>
        <div class="actions actions--m-stack" style="gap:20px">{btn("Обратный звонок", ico="phone", attrs=CALLBACK)}{btn("Написать в WhatsApp", WHATSAPP, kind="secondary", ico="whatsapp", attrs='target="_blank" rel="noopener"')}</div>
      </div>
      <iframe class="map" title="Карта: {ADDRESS}" src="https://www.google.com/maps?q={map_q.replace(' ', '+')}&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</section>
<section class="section section--cream" id="partners">
  <div class="container split__text">
    {heading("Станьте партнёром ART COOK", eyebrow="Партнёрам")}
    <p class="body">Совместные мастер-классы, поставки продуктов и оборудования, корпоративные программы.</p>
    {btn("Стать партнёром", ico="arrow-right", attrs=CALLBACK + ' data-topic="Партнёрство"')}
  </div>
</section>'''
    page("contacts.html", "Контакты", f"Кулинарная школа ART COOK: {ADDRESS}, телефон {PHONE}, WhatsApp.", "contacts.html", body)

def booking():
    opts = ALL_TITLES
    summary_data = {c["slug"]: dict(title=c["title"], meta=f'{c["weeks"]} · {c["price"]}', photo=c["photo"]) for c in COURSES}
    for c in NEW_COURSES:
        summary_data[c["slug"]] = dict(title=c["title"], meta="Стоимость: по запросу", photo=c["photo"])
    summary_data["masterclass"] = dict(title="Мастер-класс", meta="несколько часов · по запросу", photo="mc-vietnam")
    summary_data["onsite"] = dict(title="Выездной мастер-класс", meta="по запросу", photo="photo-onsite")
    import json
    body = f'''
<section class="section section--intro">
  <div class="container stack-60">
    {crumbs(("courses.html", "Курсы"), ("booking.html", "Запись"))}
    {heading("Записаться на курс", tag="h1")}
    <div class="booking">
      <form class="form form--loose js-form" data-kind="booking" novalidate>
        <p class="caption text-muted">* обязательные поля</p>
        {select("Курс", "course", opts, req=True, placeholder="Выберите курс", selected="basic", helper="Выберите курс")}
        <div class="form-row">
          {field("Имя", "name", "Введите имя", req=True, helper="Укажите имя")}
          {field("Телефон", "phone", "+7 (___) ___-__-__", typ="tel", req=True, helper="Введите номер полностью: +7 (XXX) XXX-XX-XX")}
        </div>
        {field("Email (необязательно)", "email", "name@mail.kz", typ="email", helper="Проверьте адрес почты")}
        <div class="field"><label class="field__label" for="f-comment">Комментарий</label><div class="field__control"><textarea id="f-comment" name="comment" placeholder="Например, хочу записаться на несколько курсов"></textarea></div></div>
        {consent()}
        <div><button type="submit" class="btn btn--primary btn--m-block">Отправить заявку{icon("arrow-right")}</button></div>
      </form>
      <aside class="summary" aria-live="polite">
        <p class="overline">Вы выбрали</p>
        <img id="sum-photo" src="assets/img/course-basic.jpg" alt="" width="360" height="220">
        <p class="h5" id="sum-title">Базовый кулинарный курс</p>
        <p class="body text-accent" id="sum-meta">4 недели · от 90 000 ₸</p>
        <p class="body-s">Даты подбираются индивидуально. Менеджер свяжется с вами после заявки.</p>
        <div>{link("Изменить курс", "courses.html")}</div>
      </aside>
    </div>
    <p class="help-line body">Нужна консультация? Позвоните: <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
  </div>
</section>
<script>window.AC_COURSES = {json.dumps(summary_data, ensure_ascii=False)};</script>'''
    page("booking.html", "Запись на курс", "Запишитесь на кулинарный курс или мастер-класс ART COOK. Менеджер перезвонит и подберёт даты.", "", body)

    body2 = f'''
<section class="section section--intro">
  <div class="container success">
    <div class="success__icon">{icon("check")}</div>
    {heading("Заявка принята", center=True, tag="h1")}
    <p class="h4 text-accent" id="ok-course"></p>
    <p class="body-l">Менеджер свяжется с вами в рабочее время, чтобы подобрать даты</p>
    <div class="actions actions--center actions--m-stack" style="gap:20px">{btn("Смотреть другие курсы", "courses.html", ico="arrow-right")}{btn("Позвонить", f"tel:{PHONE_TEL}", kind="secondary", ico="phone")}</div>
  </div>
</section>
<section class="section section--cream">
  <div class="container stack" style="align-items:center;gap:30px">
    {heading("Подарите курс близким", center=True)}
    {link("Подарочные сертификаты", "gift.html", ico="gift")}
  </div>
</section>
<script>window.AC_COURSES = {json.dumps(summary_data, ensure_ascii=False)};</script>'''
    page("booking-success.html", "Заявка принята", "Заявка на курс ART COOK принята.", "", body2, noindex=True)

def privacy():
    body = f'''
<section class="section section--intro">
  <div class="container stack-60" style="max-width:900px">
    {crumbs(("privacy.html", "Политика конфиденциальности"))}
    {heading("Политика конфиденциальности", tag="h1")}
    <div class="body stack gap-20">
      <p>Кулинарная школа ART COOK обрабатывает имя, телефон и email, которые вы оставляете в формах на сайте, только чтобы связаться с вами по заявке: подобрать курс, даты или сертификат.</p>
      <p>Мы не передаём данные третьим лицам и не используем их для рассылок без вашего согласия. Чтобы удалить свои данные, напишите или позвоните нам: <a class="text-accent" href="tel:{PHONE_TEL}">{PHONE}</a>.</p>
      <p>Сайт может использовать сервисы аналитики для обезличенной статистики посещений.</p>
    </div>
  </div>
</section>'''
    page("privacy.html", "Политика конфиденциальности", "Как ART COOK обрабатывает данные из форм на сайте.", "", body)

def notfound():
    body = f'''
<section class="container notfound">
  <img src="assets/img/404-bowl.png" alt="Перевёрнутая миска и рассыпанные овощи" width="300" height="300">
  <h1 class="h1">Упс! Мы не нашли эту страницу</h1>
  <p class="body-l text-muted">Возможно, страница переехала или больше не существует</p>
  <p class="notfound__code" aria-hidden="true">404</p>
  <p class="body text-heading">Нужна помощь? Позвоните нам: <a href="tel:{PHONE_TEL}">{PHONE}</a></p>
  <div class="actions actions--center actions--m-stack" style="padding-top:16px">{btn("Выбрать курс", "courses.html")}{btn("На главную", "index.html", kind="secondary")}</div>
</section>'''
    page("404.html", "Страница не найдена", "Страница не найдена.", "", body, noindex=True,
         head=BASE_SCRIPT)

if __name__ == "__main__":
    home(); courses()
    for c in COURSES:
        course_page(c)
    masterclasses(); prices(); about(); gift(); contacts(); booking(); privacy(); notfound()
    print("built")
