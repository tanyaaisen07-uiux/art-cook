# ART COOK · сайт кулинарной школы

Статичный сайт кулинарной школы ART COOK (Алматы): UX/UI-дизайн в Figma и вёрстка для GitHub Pages.
Static website for ART COOK culinary school, designed in Figma and hand-coded for GitHub Pages.

**Автор:** Tania Aisen, UI/UX Designer · [Портфолио](https://tania-aisen.framer.website/) · [LinkedIn](https://www.linkedin.com/in/tania-aisen) · [Behance](https://www.behance.net/tanyaaisen)

## Что внутри

| Страница | Файл |
|---|---|
| Главная | `index.html` |
| Каталог курсов с фильтром | `courses.html` |
| Страницы курсов | `course-basic.html`, `course-mediterranean.html`, `course-eastern.html`, `course-healthy.html` |
| Мастер-классы | `master-classes.html` |
| Цены | `prices.html` |
| О школе | `about.html` |
| Подарочные сертификаты | `gift.html` |
| Контакты и партнёрам | `contacts.html` |
| Запись и успешная заявка | `booking.html`, `booking-success.html` |
| Политика конфиденциальности | `privacy.html` |
| 404 | `404.html` |

Окно «Обратный звонок» и мобильное меню есть на каждой странице.

## Стек

- HTML, CSS, немного vanilla JS, без сборщика и зависимостей.
- Дизайн-токены из Figma Variables: `assets/css/tokens.css`.
- Шрифт Lora (SIL OFL 1.1) лежит в репозитории: `assets/fonts`, без запросов к Google Fonts.
- Иконки: SVG-спрайт `assets/svg/icons.svg`. Иконки курсов: статичный PNG, анимированный GIF при наведении (на телефоне, когда карточка в зоне видимости).
- Адаптив: десктоп 1440, планшет 768, телефон 375. На телефоне курсы листаются горизонтально, на страницах курсов есть закреплённая кнопка записи.
- Доступность: семантические заголовки, skip-link, фокус-обводка, `aria-*` у фильтра, меню и модального окна, `prefers-reduced-motion`.

## Как править

Тексты и данные курсов собраны в `tools/build.py`. После правок:

```bash
python3 tools/build.py
```

Скрипт пересобирает все HTML-страницы. Стили: `assets/css/styles.css`, поведение: `assets/js/main.js`.

## Заявки с форм

Сейчас формы работают в демо-режиме: проверяют поля и показывают успешное состояние.
Чтобы заявки приходили на почту, вставьте адрес обработчика (Formspree, Getform или вебхук Make) в `FORM_ENDPOINT` в начале `assets/js/main.js`.

## Публикация

1. Settings → Pages → Source: `Deploy from a branch`, ветка `main`, папка `/ (root)`.
2. Для своего домена: Settings → Pages → Custom domain, затем добавьте у регистратора CNAME-запись на `tanyaaisen07-uiux.github.io`.
   При переходе на домен замените адрес в `robots.txt`, `sitemap.xml` и `SITE_URL` в `tools/build.py`.

## Контент

Номер телефона и партнёры (Olivenna, Tuzly Kitchen, Green Plate Almaty) условные и использованы для демонстрации дизайна.
Фотографии и тексты принадлежат проекту ART COOK и используются с согласия владельца. Код открыт для просмотра как часть портфолио.
