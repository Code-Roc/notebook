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