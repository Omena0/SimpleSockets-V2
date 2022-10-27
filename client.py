from sandals import *
import lib
import socket
import SimpleSockets as ss

s = ss.connection('127.0.0.1',5000,'client',logging=True)


with window('MSG APP V4 GUI CLIENT VERY EARLY BETA'):
    a = label('')
    label('Enter message: ')
    b = editBox('Message')

    def on_msg(msg,cs,address):
        a.text = a.text + f'\n{msg}'
    s.on_msg = on_msg
    
    @button('Send')
    def send():
        s.send(b.text)
        b.text = ''



ss.stop()
