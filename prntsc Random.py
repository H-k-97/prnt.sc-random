import webbrowser
import string
import random
import time
from datetime import datetime



def id_generator(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

hash = input('Enter Hash to Start only 2 :')


def total(num):
    return len(num)



while True:
    if total(hash) != 2:
        hash = input('Enter only 2 Hash !! :')
    else:
        now = datetime.now()
        link = 'https://prnt.sc/' + hash + id_generator()
        webbrowser.open(link)
        with open('log.txt', mode='a') as text:
            log_link = f'{link} at {now} \n'
            writee = text.write(log_link)
            print('Script by Hk')
            print(log_link)
        time.sleep(3)
