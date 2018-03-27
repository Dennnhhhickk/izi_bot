# -*- coding: utf8 -*-

import time
import vk_api
import requests

url = "https://api.telegram.org/bot570381481:AAEsHbgPniY6aIJ43enZCprco2qQhB8PUjA/"

def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def get_msg():
    main_hero = 264476226
    values = {'out': 0, 'count': 200, 'time_offset': 60}
    while True:
        response = vk.method('messages.get', values)
        if response['items']:
            values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:
            # write_msg(item[u'user_id'],u'Hi, Habr!')
            # print(item[u'body'])
            s = str(item[u'body']) + '\n' + str(item[u'id']) + ' ' + 'https://vk.com/id' + str(item[u'user_id']);
            send_mess(main_hero, s)
        time.sleep(1)


vk = vk_api.VkApi(token="7502db93ef7bb27c36d19de968ebbc65b293fa5ef4427edf79ddd763bea9714fbb46c60eafdccd2bbcfca")
vk._auth_token()
send_mess(264476226, 'Statr')
get_msg()
'''

Школа #2
7502db93ef7bb27c36d19de968ebbc65b293fa5ef4427edf79ddd763bea9714fbb46c60eafdccd2bbcfca

378291306
250399634
'''