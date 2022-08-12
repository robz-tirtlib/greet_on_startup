import pyttsx3

import time

from datetime import datetime

from pygame import mixer


months = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря'
}


def greeting(hour: int) -> str:
    if hour < 10:
        message = 'Доброе утро'
    elif hour < 17:
        message = 'Добрый день'
    else:
        message = 'Добрый вечер'
    return message


# Check if played today already
with open("flag.txt", "r+") as f:
    date = f.readline()
    today = datetime.strftime(datetime.today(), '%y %m %d')

    if date and date == today:
        exit()

    f.write(today)

today = datetime.today()
month, day, hour = months[today.month], today.day, today.hour

text = f'{greeting(hour)}, кожаный мешок. Сегодня {day} {month}.'

ngn = pyttsx3.init()
rate = ngn.getProperty('rate')
ngn.setProperty('rate', rate-10)

volume = ngn.getProperty('volume')
ngn.setProperty('volume', volume+0.9)

voices = ngn.getProperty('voices')
ngn.setProperty('voice', 'ru')
ngn.setProperty('voice', voices[0].id)


ngn.say(text)
ngn.startLoop(False)
ngn.iterate()
ngn.endLoop()

mixer.init()
mixer.music.load("track.mp3")
mixer.music.play()
mixer.music.set_volume(0.3)
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
