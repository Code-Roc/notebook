#д��ǰ��

��û�нӴ���C��Python֮ǰ����Ҳ����BAT��һ�ѵ�������exe������

������֪������ѽ~

----
#��һ����ѭ���� for

> ���ڽ������̣�����DNS��ѯ�����˸�����tmdզ������û��

    for /l %i in (1,1,9999999) do ...

----
#�������� taskkill

> woc��զ�ҿ�����ô��cmd��һ��������̫���ˣ�����taskkillһ��

    taskkill /f /im cmd.exe
    
----
#�ڴ����� free

> ΢���Լ�����һ���ڴ������ߣ���Ҫ����ԱȨ�ޣ�ԭ����û�㶮

> exe��download/empty.exe

    empty *

----
#˯һ�� SleepX

> ������Ҫ�ȴ�һ��ʱ���ټ������оͿ���sleepx��

> exe��download/SleepX.exe������Bill Stewart (bstewart@iname.com)

    SleepX 10
    
    REM�ȴ�5s������û��Ȳ������԰�������ʱ not "%errorlevel%" == "0"
    SleepX -k 5
    
----
#�����е����� curl

![cURL](https://curl.haxx.se/logo/curl-logo.svg)

> ����������cURL�����ض��ԣ�ֻ�����������е����з�ʽ��libcurl����������ܴ���Ƚ�php��curl�÷���

> �ٷ���https://curl.haxx.se/

> �����ţ�http://www.bathome.net/thread-1761-1-1.html

> **��curlתΪpython requests** http://curl.trillworks.com/

[����7.51 x64�汾](download/curl.exe)

```
REM ��bat��REM�����ʾע����

REM �򵥵�getһ��
curl http://ip.cn

REM ���浽�ļ����ϵ����������Բ�ָ���ļ���-O��
curl -o iplist.txt -c  http://f.ip.cn/rt/chnroutes.txt

REM POST��������Referer����ʹ�ô���
curl http://httpbin.org/post --data "something=somedata" -H "Referer: http://github.com/zjuchenyuan/" --proxy socks5://127.0.0.1:1080

REM �ļ��ϴ� @�ļ���
REM POSTģʽ�µ��ļ��ϵ��ļ��ϴ�������
REM <form method="POST" enctype="multipart/form-data" action="http://cgi2.tky.3web.ne.jp/~zzh/up_file.cgi">
REM <input type=file name=upload>
REM <input type=submit name=nick value="go">
REM </form>
REM ����һ��HTTP��������Ҫ��curl����ģ�⣬�͸����������﷨��
curl -F upload=@localfile -F nick=go http://cgi2.tky.3web.ne.jp/~zzh/up_file.cgi

REM ��¼·����
curl http://192.168.1.1 -u admin:admin

REM ����Set-Cookie
curl -D cookie0001.txt http://www.yahoo.com

REM ʹ�ô洢��Cookie
curl -b cookie0001.txt http://www.yahoo.com

REM dictЭ����ֵ䣬��ʾ��ϸ��������Ϣ
curl dict://www.dict.org/d:computer -v
```

----

# BAT��������

##�ж��ļ��д���

```
if exist DIRNAME\nul echo Yes!
```

## ����Ӳ����

Win7�����ϣ�
```
mklink /H Link Target
```

Ŀ¼����Ҫ/J
```
mklink /H /J Link Target
```

WinXPֻ���ã�
```
fsutil hardlink create <new filename> <existing filename>
```

----