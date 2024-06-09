from telegram.ext import ApplicationBuilder
import requests
from telegram import (Update)
from telegram.ext import ApplicationBuilder
from telegram.ext import (CommandHandler, ContextTypes)


async def holiday(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    request = requests.get(
        f"https://calendarific.com/api/v2/holidays?&api_key=nP5EjQWi9KDHNzVOySuULjOKLdgn6oWW&country=UZ&year=2024")
    resulst = request.json()
    holiday = resulst["response"]["holidays"][0]['name']
    date = resulst["response"]["holidays"][0]['date']['iso']
    holiday1 = resulst["response"]["holidays"][1]['name']
    date1 = resulst["response"]["holidays"][1]['date']['iso']
    holiday2 = resulst["response"]["holidays"][2]['name']
    date2 = resulst["response"]["holidays"][2]['date']['iso']
    holiday3 = resulst["response"]["holidays"][3]['name']
    date3 = resulst["response"]["holidays"][3]['date']['iso']
    text = f"Holidays \n{holiday} {date}\n{holiday1} {date1}\n{holiday2} {date2}\n{holiday3} {date3}"
    await update.message.reply_text(text)


app = ApplicationBuilder().token("7274654492:AAHSnRxc65rIdd3D1tWwafucEB5aAAlW0fw").build()
app.add_handler(CommandHandler("holiday", holiday))

app.run_polling()
