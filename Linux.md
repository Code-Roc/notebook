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

----
#���ٰ�װ

���ԣ�https://github.com/91yun/serverspeeder

��װ֮ǰ��Ҫ�޸��ں˰汾��������

    apt-get install linux-image-3.16.0-43-generic
    reboot

��װ���#�˰�װ�ű������ӿ����ߵķ�������rootȨ��ִ��Զ��ָ������Ը�

    wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh
    
�鿴״̬/�رշ���

    service serverSpeeder stauts
    service serverSpeeder stop