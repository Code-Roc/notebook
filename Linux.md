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
    
----

#�������߾�̬IP
```bash
vim /etc/network/interfaces
#д���������ݣ��������滻xx����
iface eth0 inet static
 address 10.xx.xx.13
 netmask 255.255.255.0
 network 10.xx.xx.0
 broadcast 10.xx.xx.255
 gateway 10.xx.xx.254
 dns-nameservers 10.10.0.21
#��Esc, :wq�˳�����
service networking restart
ifconfig eth0 10.xx.xx.13 netmask 255.255.255.0 up
route add default eth0
```

#��������ö��IP
ifconfig eth0:233 10.xx.xx.233 netmask 255.255.255.0 up
