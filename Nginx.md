# Nginx

��¼�õ������ã�˵������Ҳ��������Щ����������~

## ��ͨ��Դ����POST

    error_page 405 =200 @405;


## ������׺���ļ�����phpִ��

�����˼·���÷������ķ�ʽ��ʵ��

    location /path/something {
        proxy_pass http://yourdomain/path/something.php;
        proxy_method GET;
    }

˳���ܾ�����php��׺�Ĳ²⣺

    location = /path/something.php {
        if ($remote_addr != '����������IP') {
            return 404;
        }
        include fastcgi.conf;
    }

## http��ת��https

    location /{
        rewrite ^ https://$host$request_uri? permanent;
    }

## ���Let's encrypt���https֤��

Ϊ�򻯲�������д��һ�����ӷ����[getcert.py](code/getcert.py)

###ʹ�÷�����

####��һ����

������Ӧ��վ��nginx conf�е�server���棬���������

```
    location /.well-known/acme-challenge {
        alias ������Կ��Ŀ¼;
        try_files $uri =404;
    }
```

�ǵ����к� `nginx -s reload`

####�ڶ����������ҵ�getcert.py������˽Կ���ύ���룩��

````
pushd ����������Կ��Ŀ¼
wget https://raw.githubusercontent.com/zjuchenyuan/notebook/master/code/getcert.py
./getcert.py �ļ����� ��֤������������б�
````

�����������ܻ��һ�ź���zjusec.com������������֤�飺`./getcert.py zjusec zjusec.com,www.zjusec.com,web.zjusec.com`

������˵������ű����Զ�������Ҫ��acme_tiny.py��Let's Encrypt���м�֤�飬����openssl�����˺�˽Կ��վ��˽Կ�����ղ��� **����.crt** **����.key**��

![https.jpg](download/img/https.jpg)

####������������https�����ã�

```
server {
    listen 443;
    server_name ����1 ����2;
    access_log /tmp/access.log;
    error_log /tmp/error.log;
    ssl on;
    ssl_certificate ��ԿĿ¼/����.crt;
    ssl_certificate_key ��ԿĿ¼/����.key;
    ssl_session_cache    shared:SSL:1m;
    ssl_session_timeout  5m;
    ssl_ciphers 'AES128+EECDH:AES128+EDH';
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers  on;
    �������á�����
}
```