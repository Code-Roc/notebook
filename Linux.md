#��η�ǽ

##����shadowsocks�ͻ��ˣ�������Privoxy�ṩhttp proxy

> * ����μ�code/ssprivoxy.txt

##Ҳ��ʹ��iodineҲ�Ǹ��������

TODO: ����iodine�ıʼ�

----

#�����ı���grep����stderr�ض���stdout

������2>&1�������ض���

    ssh-keygen --help 2>&1|grep bit

----

#git push������

����http://blog.csdn.net/chfe007/article/details/43388041

���������Լ���ssh��Կ

    ssh-keygen -t rsa -b 4096

Ȼ���id_rsa.pub���������õ�github�У���ҳ�˲���������˳������������֤

����git�Լ���˭��

    git config --global user.email "����"
    git config --global user.name "�û���"

�����ǰ�ֿ���https�ģ���Ϊgit��ʽ��

    git remote set-url origin git@github.com:�û���/�ֿ�����.git