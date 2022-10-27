import SimpleSockets as ss

s = ss.connection('127.0.0.1',5000,'server',logging=True)

def on_connect(cs,ip,port):
    lib.log('+',f'{ip}:{port} Connected!')
def on_disconnect(cs,ip,port):
    lib.log('-',f'{ip}:{port} Disconnected!')
def on_msg(msg,cs,address):
    lib.log('*',f'{ip}:{port}: {msg}')
    
s.on_connect = on_connect
s.on_disconnect = on_disconnect
s.on_msg = on_msg

