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

#��ǰĿ¼�ļ�ȫ������

����Ҫ������ǰĿ¼�������еİ���"MultiTeam"��php�ļ�

    find| grep .php| xargs cat|grep MultiTeam -r .

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

## ����aptԴ

    curl http://mirrors.163.com/.help/sources.list.trusty>/etc/apt/sources.list

���ֻ���ִ�vim����һ�е�����Ϊyy��ճ��Ϊp

```
deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse
```

## ��������ö��IP
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
    
----
#���apt��������

����������������Ϊubuntu14.04�汾��ĳЩ�����������޷���`apt-get`��װ�κζ���

```bash
> apt-get -f install
Reading package lists... Done
Building dependency tree
Reading state information... Done
Correcting dependencies... failed.
The following packages have unmet dependencies:
 libatk1.0-0 : Depends: libglib2.0-0 (>= 2.41.1) but 2.40.0-2 is installed
 libglib2.0-bin : Depends: libglib2.0-0 (= 2.44.0-1ubuntu3) but 2.40.0-2 is installed
 libglib2.0-dev : Depends: libglib2.0-0 (= 2.44.0-1ubuntu3) but 2.40.0-2 is installed
 libgtk2.0-0 : Depends: libglib2.0-0 (>= 2.41.1) but 2.40.0-2 is installed
E: Error, pkgProblemResolver::Resolve generated breaks, this may be caused by held packages.
E: Unable to correct dependencies
```

��ϸ������˵����libglib2.0-bin��������Ҫ��libglib2.0-0�İ汾=2.44�������еİ�װ�汾Ϊ2.40

��ubuntu�������������������https://launchpad.net/ubuntu/

����2.44�汾����vivid���ṩ�ģ�����ϵͳ�汾��trusty����Ȼapt-getװ����

���������

�ҵ�������Ϣ��Ҫ�ľ�ȷƥ����Ǹ�deb�ļ����ؿ������������Ҫ��������汾�ģ�

https://launchpad.net/ubuntu/vivid/amd64/libglib2.0-0/2.44.0-1ubuntu3

�õ�deb�ļ���`dpkg -i �ļ���`

## Note

һ��apt������ͻ���ⶼ������ϵͳ�汾����Ҫ�İ��İ汾��һ�µ��µģ����һ��/etc/apt/sources.list�����Ƿ�ƥ��ϵͳ�汾��

��apt-getǰ���һ��sources.list����ݮ���ǰ汾8����jessie����wheezy!

----

# UnixBench

VPS���ܲ��Թ��ߣ���ʱ�ϳ������ĵȴ�

```bash
curl https://codeload.github.com/kdlucas/byte-unixbench/zip/v5.1.3>UnixBench.zip
unzip UnixBench.zip
cd byte-unixbench-5.1.3/UnixBench
#apt-get install build-essential
make
screen -S ub
./Run
```

## Ӳ��IO���ܲ���

```
dd if=/dev/zero of=test bs=64k count=4k oflag=dsync
dd if=/dev/zero of=test bs=8k count=256k conv=fdatasync
```

## �ο����ݣ���Ϊ�������

������1590.5��������1470.4����Ѷ��1156.0

----

## ����ڴ滺��

```
sync
echo 3 > /proc/sys/vm/drop_caches
```

----

#ʹ��iptables��ip

###���ε���IP

    iptables -I INPUT -s 123.45.6.7 -j DROP

###��C��

    iptables -I INPUT -s 123.45.6.0/24 -j DROP

####��B��

     iptables -I INPUT -s 123.45.0.0/16 -j DROP

###��A��

    iptables -I INPUT -s 123.0.0.0/8 -j DROP

�ǵ�**����**��

    service iptables save

## ɾ��һ������

ֻҪ��дһ�Ρ���-I��Ϊ-D����

    iptables -D INPUT -s IP��ַ -j DROP

----

## ��rootȨ��ʹ��screen

> https://www.gnu.org/software/screen/

������ͬ����ϵͳ�µ�screen�������ļ�������ǰָ����������

    mkdir -p $HOME/.screen
    export SCREENDIR=$HOME/.screen
    
----

## screen���÷�

�г����ڵ�screen��

    screen -ls
    
����һ����Ϊname��screen��

    screen -S name

��screen���룺

    ��Ctrl+A��d

������������Ϊname��screen��

    screen -r name

----

# ͳ�Ƶ�ǰ�ļ��д�������

find ָ���ļ���׺������סҪ���ű���bash����*

    find -name "*.py" -o -name "*.md"|xargs cat|wc

----

# ˫�����˿�ת������¶�����˿�

> ���ԣ� https://yq.aliyun.com/wenzhang/show_25824

����̨����������һ̨A ��������������Bֻ��������

Ŀ�꣺ ����������A������2121�˿ڣ����൱��������B������ftp(21)

##������ 

A��������IPΪ 123.234.12.22(eth1) ����IPΪ 192.168.1.20 (eth0)

B��������Ϊ 192.168.1.21

## ʵ�ַ�����

1. ��A�����ϴ򿪶˿�ת������

    echo 1 > /proc/sys/net/ipv4/ip_forward
    echo -e "\nnet.ipv4.ip_forward = 1">>/etc/sysctl.conf
    sysctl -p

2. ��A�����ϴ���iptables����

    #�ѷ�������2121�˿ڵİ�ת��������ftp������
    iptables -t nat -I PREROUTING -d 123.234.12.22 -p tcp --dport 2121 -j DNAT --to 192.168.1.21:21 
    #�ѵ�����ftp�������İ���Դ�����������ϣ���Ȼ��ֻ��ת��ftp�������������صİ����ܵ���ͻ���
    iptables -t nat -I POSTROUTING -d 192.168.1.21 -p tcp --dport 21 -j SNAT --to 192.168.1.20 
    #����һ�¹���
    service iptables save

## ȡ������

iptables�а�-I��Ϊ-D���о���ɾ����������