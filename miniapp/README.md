# Sticker Forge – Mini App (visual editor)

یک صفحه‌ی ساده (`index.html`) که داخل تلگرام باز می‌شود و پیش‌نمایش زنده‌ی استیکر را نشان می‌دهد:
افکت‌ها (تا ۳ تا)، سرعت، شدت، حاشیه/سایه، متن (اندازه، رنگ، فونت، **کشیدن متن با انگشت**)، حذف پس‌زمینه،
تنظیمات تصویر و فرمت خروجی. با دکمه‌ی «ارسال به ربات» تنظیمات به ربات می‌رسد و ربات همان‌ها را اجرا می‌کند.

بک‌اند ندارد: فقط یک فایل HTML استاتیک است و داده را با `Telegram.WebApp.sendData` به ربات برمی‌گرداند.

## میزبانی رایگان با GitHub Pages (فقط با گوشی)

1. در GitHub یک مخزن بساز (مثلاً `sticker-forge-app`) و **Public** باشد.
2. در مخزن: **Add file → Upload files** و فایل `index.html` را آپلود کن (Commit).
3. **Settings → Pages**: بخش *Build and deployment* را روی *Deploy from a branch* بگذار، شاخه‌ی `main` و پوشه‌ی `/ (root)` را انتخاب و Save کن.
4. بعد از یک دقیقه آدرس می‌آید، مثلاً `https://USERNAME.github.io/sticker-forge-app/` (حتماً `https`).
5. در Termux در فایل `.env` بنویس: `WEBAPP_URL=https://USERNAME.github.io/sticker-forge-app/`
6. ربات را ریستارت کن و در تلگرام `/menu` بزن. دکمه‌ی «🎨 ویرایشگر تصویری» بالای منو می‌آید.

## نحوه‌ی کار
* تصویر را قبل یا بعد از ویرایشگر به ربات بفرست. اگر در ویرایشگر قالب (WEBM/TGS) انتخاب شده باشد، ربات بلافاصله می‌سازد.
* پیش‌نمایش با فونت خود گوشی کشیده می‌شود؛ فونت واقعی را ربات رندر می‌کند، پس فاصله‌ی حروف کمی فرق دارد.
* دکمه‌ی ویرایشگر فقط وقتی داده را برمی‌گرداند که از **منوی پایین چت** (کیبورد) باز شده باشد، نه از دکمه‌ی داخل پیام.

## پیش‌نمایش فونت‌ها
قبل از آپلود در GitHub یک بار این را در Termux اجرا کن تا فونت‌های ربات کنار صفحه کپی شوند:

```bash
cd ~/sticker_forge && python miniapp/make_fonts.py
```

سپس **`index.html`، `fonts.json` و پوشه‌ی `fonts/`** را در مخزن Pages آپلود کن (با git: `cp -r miniapp/index.html miniapp/fonts.json miniapp/fonts ~/sticker-forge-app/ && cd ~/sticker-forge-app && git add -A && git commit -m fonts && git push`).
بدون `fonts.json` هم صفحه کار می‌کند؛ فقط فونت‌ها بدون نمونه نشان داده می‌شوند.
