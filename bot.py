import vk_api
import botT
import fille
import threading
import time
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
vk_session = vk_api.VkApi(token = 'fad3d76abe4c195a54916d631fc453b0ddf8005caa387269585af7c9fc522b22588b7f075a36114e61b69')
#vk_session = vk_api.VkApi(token = 'aeb7a7e62e220a95cf2c76702cf1b9c50735ab93b688a95a203c98c678e3d60d48ec521967c551a9c7b40') 11а
#vk_session = vk_api.VkApi(token = '973e44f4661ce7e6f56115203bdf7cffe2904eb0e6e29936ded6ee3a5055545e1e3dc2c4f834d19c7a881') записки
vk = vk_session.get_api()
keyboard = VkKeyboard()
keyboard.add_button('11а', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('11б', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('11в', color=VkKeyboardColor.DEFAULT)
keyboard.add_line()  # Переход на вторую строку
keyboard.add_button('10а', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('10б', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('10в', color=VkKeyboardColor.DEFAULT)
keyboard.add_line()
keyboard.add_button('Инфо, так сказать', color=VkKeyboardColor.NEGATIVE)
keyboard.add_line()
keyboard.add_button('Как подключить уведомления?', color=VkKeyboardColor.POSITIVE)
longpoll = VkLongPoll(vk_session)
last_date = ''
last_xd = ''
def checker():
    while(True):
        global last_xd
        xd = botT.get_hook()
        if last_xd != xd:
            vk.messages.send(user_id='75772038',message=xd,keyboard=keyboard.get_keyboard())
            last_xd = xd    
        print(1)        
        time.sleep(20)  
"""      
def getter():
    while(True):
        global last_date
        result = botT.get_timetable2()
        if result[1]==0:
            print(1)
            time.sleep(360)
            continue            
        if last_date != result[1]:
            last_date = result[1]
            beta = 'Уведомление!\n'+result[1]+'\n__________________________\n'
            alfa = botT.get_book('11а')
            alfa = beta + alfa
            vk.messages.send(user_id='75772038',message=alfa,keyboard=keyboard.get_keyboard())
            vk.messages.send(chat_id='2',message=alfa)
#            vk.messages.send(user_id='86658739',message=alfa,keyboard=keyboard.get_keyboard())        
        print(1)        
        time.sleep(360)
"""
def main():
        for event in longpoll.listen():

            if event.type == VkEventType.MESSAGE_NEW:
                print('Новое сообщение:')
                print('Текст: ', event.text)
                if event.text=='11а':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    alfa = botT.get_book('11а')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                if event.text=='11б':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('11б')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                if event.text=='11в':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('11в')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                if event.text=='10а':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    alfa = botT.get_book('10а')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                if event.text=='10б':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('10б')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                if event.text=='10в':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('10в')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                if event.text=='Инфо, так сказать':
                    vk.messages.send(user_id=event.user_id,message='v2.0 VK_REBORN(MagnumOpus)\nВсе права принадлежат тому, кому принадлежат.\n_______________________________________________\nПочему у римлян не было проблем с алгеброй? Потому что X всегда 10.\n_______________________________________________\nКонсультант по проблемам с ботом:\nhttps://vk.com/id_gwynbleidd',keyboard=keyboard.get_keyboard())
                if event.text=='Как подключить уведомления?':
                    vk.messages.send(user_id=event.user_id,message='Подключить уведомления можно только в беседу. Позже я возможно переделаю эту систему. А пока пишите мне чтобы подключить эту функцию.\nhttps://vk.com/id_gwynbleidd',keyboard=keyboard.get_keyboard())    
                if event.text=='Начать':
                    vk.messages.send(user_id=event.user_id,message='Бот был разработан для 11А.Вопросы пишите нашему консультанту(Мы не несем ответственности за последствия).',keyboard=keyboard.get_keyboard())
                print()
"""
def main():



    thread1 = threading.Thread(target=worker)
    thread2 = threading.Thread(target=getter)
    thread1.start()
    thread2.start()
"""

if __name__ == '__main__':
    main()
