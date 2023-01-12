from controller import parseable_data, solution_equation
from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from log import get_id_user, get_input_data, get_result, save_log

TOKEN = '5909180299:AAF3qzGZSzPM1ZYjeNwVDhsxFZVP5sG8-4g'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

start_calc = 0

# ДАЛЕЕ = ТРИ ОСНОВНЫЕ ФУНКЦИИ

def start(update, context):
    '''Начало работы с калькулятором. Получение id пользователя'''
    context.bot.send_message(update.effective_chat.id, 'Вас приветствует калькулятор "Mapoduma T-800"')
    context.bot.send_message(update.effective_chat.id, 'Производим деление, сложение, умножение и вычитание с положительными числами')
    context.bot.send_message(update.effective_chat.id, 'Приоритет действий и работа со скобками учтены')
    context.bot.send_message(update.effective_chat.id, 'Для завершения работы введите /end')
    get_id_user(update.effective_chat.id)
    return start_calc

def receiving_data(update, context):
    '''Логика бота'''
    data = update.message.text            # введенный текст - это и есть уравнение
    get_input_data(data)                  # передача данных для записи в log
    list_data = parseable_data(data)      # обработка полученных данных для использования в дальнейшем
    result = solution_equation(list_data) # получение результата (находится в controller)
    get_result(result)                    # передача результата для записи в log
    save_log()                            # запуск функции записи в log
    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')

def cancel(update, context):
    '''Закрытие бота'''
    context.bot.send_message(update.effective_chat.id, 'Adios Amigo!')
    return ConversationHandler.END       #   To end the conversation, the callback function must return END or -1

start_handler = CommandHandler('start', start)
receiving_data_handler = MessageHandler(Filters.text & (~Filters.command), receiving_data) # текст и ~команда, запуск функции
mes_data_handler = CommandHandler('end', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler], # точка входа
                                   states={start_calc: [receiving_data_handler]},
                                   fallbacks=[mes_data_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()