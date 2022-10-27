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
import SimpleSockets as ss

s = ss.connection('127.0.0.1',5000,'client',logging=True)

with window('Test'):
    label('')
    a = editBox('Message')
    
    @button('Send')
    def send():
        s.send(a.text)
```







