# SimpleSockets V2
 SimpleSockets V1 but more simple?? Yea, i guess! ¯\\_(ツ)_/¯

```python
import SimpleSockets as ss
```

## Examples:

### Client:
```python
from sandals import *
import lib
import socket
import SimpleSockets as ss
s = ss.connection('127.0.0.1',5000,'client',logging=True)
with window('MSG APP V4 GUI CLIENT VERY VERY VERY EARLY BETA'):
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
```

### Server
```python
import SimpleSockets as ss
import socket
import lib

s = ss.connection('127.0.0.1',5000,'server',logging=True)

def on_connect(cs,ip,port):
    lib.log('+',f'{ip}:{port} Connected!')
def on_disconnect(cs,ip,port):
    lib.log('-',f'{ip}:{port} Disconnected!')
def on_msg(msg,cs,address):
    ip = address[0]
    port = address[1]
    lib.log('*',f'{ip}:{port}: {msg}')
    for cs in s.clients:
        cs.send(f'[JOIN] {ip}:{port}'.encode())
    
s.on_connect = on_connect
s.on_disconnect = on_disconnect
s.on_msg = on_msg

ss.stop()

```






