import vk_api
import botT
import fille
import threading
import time
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
vk_session = vk_api.VkApi(token = 'fad3d76abe4c195a54916d631fc453b0ddf8005caa387269585af7c9fc522b22588b7f075a36114e61b69')
#vk_session = vk_api.VkApi(token = 'aeb7a7e62e220a95cf2c76702cf1b9c50735ab93b688a95a203c98c678e3d60d48ec521967c551a9c7b40') 11а
#vk_session = vk_api.VkApi(token = '973e44f4661ce7e6f56115203bdf7cffe2904eb0e6e29936ded6ee3a5055545e1e3dc2c4f834d19c7a881') записки
vk = vk_session.get_api()
ero_links=['photo-121679067_456239349','photo-121679067_456240260','photo-121679067_456240079','photo-121679067_456240079','photo-121679067_456240078','photo-121679067_456240077','photo-121679067_456240075','photo-121679067_456240074','photo-121679067_456240071','photo-121679067_456240063','photo-121679067_456240060','photo-121679067_456240057','photo-121679067_456239221','photo-121679067_456239345','photo-121679067_456239349']
keyboard = VkKeyboard()
keyboard.add_button('11а', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('11б', color=VkKeyboardColor.POSITIVE)
keyboard.add_button('11в', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()  # Переход на вторую строку
keyboard.add_button('10а', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('10б', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('10в', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('9а', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('9б', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('9в', color=VkKeyboardColor.DEFAULT)
keyboard.add_line()
keyboard.add_button('9г', color=VkKeyboardColor.DEFAULT)
keyboard.add_button('9д', color=VkKeyboardColor.DEFAULT)
keyboard.add_line()
keyboard.add_button('Инф0рмация', color=VkKeyboardColor.NEGATIVE)
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
                text = event.text
                if text=='':
                    text='1'
                if event.text=='11а':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    alfa = botT.get_book('11а')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='11б':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('11б')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='11в':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('11в')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='10а':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    alfa = botT.get_book('10а')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='10б':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('10б')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='10в':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('10в')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='9а':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('9а')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='9б':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('9б')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='9в':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('9в')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='9г':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('9г')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='9д':
                    res = botT.get_timetable2()
                    beta = res[1]+'\n==========================\n'
                    botT.get_timetable2()
                    alfa = botT.get_book('9д')
                    alfa = beta + alfa
                    vk.messages.send(user_id=event.user_id,message=alfa,keyboard=keyboard.get_keyboard())
                elif event.text=='!SpecFor10A':
                    i = random.randint(0,len(ero_links)-1) 
                    vk.messages.send(user_id=event.user_id,keyboard=keyboard.get_keyboard(),attachment=ero_links[i])
                elif text.split()[0]=='!AppendEro':
                    text = event.text
                    text = text.split()
                    text[0] = ''
                    ero_links.append(text[1])
                    vk.messages.send(user_id=event.user_id,message='Готово!',keyboard=keyboard.get_keyboard())
                elif event.text=='Инф0рмация':
                    vk.messages.send(user_id=event.user_id,message='v2.2 VK_REBORN(A contrario)\nВсе права принадлежат тому, кому принадлежат.\n_______________________________________________\nНичего не изменилось. Мне просто захотелось обновление\n_______________________________________________\nКонсультант по проблемам с ботом:\nhttps://vk.com/id_gwynbleidd',keyboard=keyboard.get_keyboard())
                elif event.text=='Как подключить уведомления?':
                    vk.messages.send(user_id=event.user_id,message='Подключить уведомления можно только в беседу. Позже я возможно переделаю эту систему. А пока пишите мне чтобы подключить эту функцию.\nhttps://vk.com/id_gwynbleidd',keyboard=keyboard.get_keyboard())    
                elif event.text=='Начать' or event.text=='Start':
                    vk.messages.send(user_id=event.user_id,message='Все претензии к тем кто выкладывает расписание на сайт.',keyboard=keyboard.get_keyboard())
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
