# Nginx

��¼�õ������ã�˵������Ҳ��������Щ����������~

## ��ͨ��Դ����POST

    error_page 405 =200 @405;


## ������׺���ļ�����phpִ��

�����˼·���÷������ķ�ʽ��ʵ��

    location /path/something {
        proxy_pass http://yourdomain/path/dosomething.php;
        proxy_method GET;
    }