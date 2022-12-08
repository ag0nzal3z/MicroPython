import urequests


def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = urequests.post(send_text)
    return response


#mensaje = 'Test'
#mensaje_enviar = telegram_bot_sendtext(mensaje)
