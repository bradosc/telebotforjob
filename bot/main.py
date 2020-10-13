import telebot
from telebot import types



token = '955839116:AAEo5mNeBqxZ9HJrj8DTHUAf8YPVu21H2FM' #Изменить на свой токен. Взять и создать можно через @BotFather

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_towns(message):
    photo = open('../img/national.png', 'rb')
    markup = types.InlineKeyboardMarkup()
    info = types.InlineKeyboardButton(text='Інформація', callback_data="info")
    target = types.InlineKeyboardButton(text='Ціль', callback_data="target")
    education = types.InlineKeyboardButton(text='Освіта', callback_data="education")
    Experience = types.InlineKeyboardButton(text='Досвід роботи', callback_data="Experience")
    More_information = types.InlineKeyboardButton(text='Додаткові відомості', callback_data="More_information")
    Experience_Virus = types.InlineKeyboardButton(text='Знання Вірусологія', callback_data="Experience_Virus")
    Send_Doc_File = types.InlineKeyboardButton(text='Резюме в форматі Word', callback_data="Send_Doc_File")
    Send_Document_File = types.InlineKeyboardButton(text='Документи в форматі PDF', callback_data="Send_Document_File")
    markup.add(info,target,education,Experience,More_information,Experience_Virus,Send_Doc_File,Send_Document_File)
    bot.send_photo(message.from_user.id, photo)
    bot.send_message(message.from_user.id, 'Резюме Балибердіна Дениса''\n'
                                           '\n'
                     'На заняття вакантної посади інспектор (з функціями спецагента)''\n'
                     'Категорії «цивільний персонал» 3-го відділу 3-го управління(інформаційних технологій та програмування)''\n'
                     'Департаменту кіберполіції(міжрегіональний територіальний орган Національної поліції України''\n', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "info":
        bot.send_message(chat_id=call.message.chat.id, text="Балибердін Денис Володимирович"'\n'
                                                            "▪Тел. +38 (093) 228-2108"'\n'
                                                            "▪E-mail: denbaliberdin@gmail.com"'\n'
                                                            "▪Telegram @denbelya"'\n'
                                                            "▪Д.н. 21 серпня 1999 р"'\n'
                                                            "▪Судимість в 2020р"'\n'
                                                            " •ч.1 ст. 361 КК України"'\n'
                                                            " •ч.1 ст. 361-2 КК України"'\n'
                                                            "▪Дата створення бота 09.10.2020-12.10.2020"'\n'
                         )
    elif call.data == "target":
        bot.send_message(chat_id=call.message.chat.id, text="Отримання роботи в області IT сфері. Поліпшити і набути навичок в області IT сфери, роботи з інформацією в будь-якій її формі, отримання високо рівня знань в даній сфері. Здобуття нових вершин. Тільки в верх тільки в перед."
                         )

    elif call.data == "education":
        bot.send_message(chat_id=call.message.chat.id, text="▪Закінчив Смілянський Технологічний Фаховий Коледж Національного Університету Харчових Технологій" '\n'
                                                            "▪Отримано диплом про вищу освіту з Добре" '\n'
                                                            "▪Спеціальність: «Обслуговування програмних систем та комплексів»"'\n'
                                                            "▪Тема дипломної роботи: «Розрахунок та нарахування депозитних вкладів ПАТ Приват Банк»" '\n'
                                                            '\n'
                                                            "▪Зарахований в Черкаський Державний Технічний Університет."'\n'
                                                            "▪Факультет: Факультет електронних технологій і робототехніки."'\n'
                                                            "▪Спеціальність: Кібербезпека (Безпека інформаційних і комунікаційних систем, Системи технічного захисту інформації"
                         )
    elif call.data == "Experience":
        bot.send_message(chat_id=call.message.chat.id, text="▪Три роки працював фрілансом на платформі https://freelance.ua/ в категорія "'\n'
                         "▪ Відео монтаж:"'\n'
                         "    • Рекламні відео"'\n'
                         "    •	Сюжети"'\n'
                         "    •	Промо"'\n'
                         "▪ Розробка лендінг сторінок."'\n'
                         "▪ Розробка сайтів на OpenCard"'\n'
                         "▪ Робота з другими CMS платформами"'\n'
                         "▪ Робота з системой VPS\VDS"'\n'
                         "▪ Розробка Telegram ботів на мові (Python\MySQL):"'\n'
                         "    • Магазини "'\n'
                         "    • Інформативні блоги"'\n'
                         "    • Парсери"'\n'                         
                         "▪ Робота за Базами даних"'\n'
                         "▪ Розробка презентацій PowerPoint\Word\Ecxel"'\n'
                         "▪ SMM\SEO проекти такі як:"'\n'
                         "    •Leongram (https://leongram.com) Онлайн консультант в відділі технічна підтримка"'\n'
                         "    •Lolzteam (https://lolz.guru/) Адміністратор проекта 2014-2016р "'\n'
                         "    •Ps-hack (https://pshack.org/) Адміністратор проекта 2015-2017р "'\n'                           
                         "▪ Робота в комерційних проектах "'\n'
                         )
    elif call.data == "More_information":
        bot.send_message(chat_id=call.message.chat.id, text="▪ Знання спеціалізованих програм для автоматизованої системи (Пакет програм MS Office (Word, Excel, Access), графічний редактор Adobe Photoshop (на базовому рівні)."'\n'
                                                            "▪ Знання ін. мов: англійська - рівеньсередній."'\n'
                                                            "▪ Брав активну участь у студентських заходах."'\n'
                                                            "▪ Хобі: програмування, автомобілі, активний відпочинок, подорожі в країни третього рівня."'\n'
                                                            "▪ Комунікабельність"'\n'
                                                            "▪ Креативне мислення"'\n'
                                                            "▪ Наполегливість в досягненні мети"'\n'
                         "▪ На даний момент навчаюся на курсах Пентестингу з метою отримати великий теоретичний досвід роботи в даному напрямку."'\n'
                         "▪ Досвід роботи в зборі інформації любого типу."'\n'
                         "	Користна інформація:"'\n'
                         " •Про конкретну людину\фірму\сферу"'\n'
                         " •Аудит і аналіз сайтів."'\n'
                         " •Перехват людей(клієнтів) в конкурентних фірмах"'\n'
                         " •Робота з фальсифікацієй результатів."'\n'
                         "▪Ремонт техніки Apple:"'\n'
                         " •Обход блокувань Lost\Icloud"'\n'
                         " •Технічний ремонт"'\n'
                         "▪Робота в системах:"'\n'
                         " •Windows (Професійна)"'\n'
                         " •Android (Професійна)"'\n'
                         " •Mac OS (Добре)"'\n'
                         " •Linux(Debian\KaliLinux) здобуваю технічні знання"'\n'
                         "▪Продвинуті знання в системі Wordpress"'\n'
                                                            "▪Пcихологія"'\n'
                                                            " •СІ(соціальна інженерія)"'\n'
                                                            " •Седення переговорів на різни теми"'\n'
                         "*Тримав особистий проект статистика за один місяць була 10.000-30.000 тис користувачів*"'\n'
                                                            '\n'
                         "НАВЧАЮСЬ ПІД ЧАС ВИКОНАННЯ ПРОЕКТІВ, ЛЕГКО ОТРИМУЮ НАВИКИ"
                         )
    elif call.data == "Experience_Virus":
        bot.send_message(chat_id=call.message.chat.id, text="▪ Знання і практичне володіння:"'\n'
                                                            "•BotNet"'\n'
                                                            " •RMS"'\n'
                         " •DDos"'\n'
                         " •Keyloger"'\n'
                         " •Stilling"'\n'
                         " •Miner"'\n'
                         " •Crypting"'\n'
                         "▪Підміна файлів"'\n'
                         "▪Поглибленні знаня в системі Carding(ТІЛЬКИ ТЕОРИТИЧНІ ЗНАННЯ)"'\n'
                         "▪Особисто знайомий з АМС всих СНГ проектами\форумами"'\n'
                         "▪Доповнити інформацію можли при особисті зустрічі або через онлайн спілкування"'\n'
                         )
    elif call.data == "Send_Doc_File":
        bot.send_document(chat_id=call.message.chat.id, data=open("../file/rezume.doc", "rb")
                          )
        bot.send_message(chat_id=call.message.chat.id, text="Готове резюме для друку:"
                         )
    elif call.data == "Send_Document_File":
        bot.send_document(chat_id=call.message.chat.id, data=open("../file/document/Document.rar","rb"
                                                                  )
                          )

bot.polling()