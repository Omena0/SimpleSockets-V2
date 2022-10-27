# SimpleSockets V2
 SimpleSockets V1 but more simple?? Yea, i guess! ¯\\_(ツ)_/¯

```
import SimpleSockets as ss
```

## How to get started
#### (a how to and a getting started guide combined im so smart)

### Making a server

- First import SimpleSockets 
```python
import SimpleSockets as ss
```

- Define a server or client object:
##### Define a new connection with logging enabled on localhost port 5000 as s:
```python
s = ss.connection('127.0.0.1',5000,'server',logging=True)
```

- Define what to do on a new connection, disconnection or message:
```python
def on_connect(cs,ip,port):
    lib.log('+',f'{ip}:{port} Connected!')
def on_disconnect(cs,ip,port):
    lib.log('-',f'{ip}:{port} Disconnected!')
def on_msg(msg,cs,address):
    lib.log('*',f'{ip}:{port}: {msg}')
s.on_connect = on_connect
s.on_disconnect = on_disconnect
s.on_msg = on_msg
```
### Making the client

- Import SimpleSockets and sandals and define connection:
#### See sandals [here] (https://github.com/georgewalton/Sandals)
```python
import SimpleSockets as ss
import sandals

s = ss.connection('127.0.0.1',5000,'client',logging=True)
```







