from telegram.ext import ApplicationBuilder
import requests
from telegram import (Update)
from telegram.ext import ApplicationBuilder
from telegram.ext import (CommandHandler, ContextTypes)


async def holiday(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    request = requests.get(
        f"https://calendarific.com/api/v2/holidays?&api_key=nP5EjQWi9KDHNzVOySuULjOKLdgn6oWW&country=UZ&year=2024")
    res = request.json()
    bayram = res["response"]["holidays"][0]['name']
    date = res["response"]["holidays"][0]['date']['iso']
    bayram1 = res["response"]["holidays"][1]['name']
    date1 = res["response"]["holidays"][1]['date']['iso']
    bayram2 = res["response"]["holidays"][2]['name']
    date2 = res["response"]["holidays"][2]['date']['iso']
    bayram3 = res["response"]["holidays"][3]['name']
    date3 = res["response"]["holidays"][3]['date']['iso']
    text = f"Holidays \n{bayram} {date}\n{bayram1} {date1}\n{bayram2} {date2}\n{bayram3} {date3}"
    await update.message.reply_text(text)


app = ApplicationBuilder().token("7079580951:AAE5IPnI0HlFsMGouUCgvCH9p2h19OX493A").build()
app.add_handler(CommandHandler("holiday", holiday))

app.run_polling()
