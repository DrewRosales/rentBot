import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import rentScraper as sc

token = "1145110613:AAFuDGcl_KXOEF_k4eYwjxIKXUzAvG25EEc"
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    message = 'Gathering rent information...'
    update.message.reply_text(message)

def rentData():
    amount, date = sc.scrap()
    
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    #Create an updater based on the bot's token
    updater = Updater(token, use_context = True)

    #Dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start"), start)
    dp.add_handler(CommandHandler("paid"), paid)

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle();

if __name__ == '__main__':
    main()