#VirtualBox

> �ο� https://www.howtoforge.com/tutorial/running-virtual-machines-with-virtualbox-5.1-on-a-headless-ubuntu-16.04-lts-server/

��linux�ն���ʹ��VBoxManage��VBoxHeadless����������������һ��Ubuntu14.04 64Bit�������

## ����

http://www.virtualbox.org/wiki/Downloads

�ӹ����ҵ���Ӧ��rpm��deb���ؼ���

> rpm�ļ��İ�װ��

>    rpm -ivh something.rpm

> deb�ļ��İ�װ

>    dpkg -i something.rpm

## һ��Ҫ��װ�����

```
cd /tmp
wget http://download.virtualbox.org/virtualbox/5.1.0/Oracle_VM_VirtualBox_Extension_Pack-5.1.0-108711.vbox-extpack
sudo VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-5.1.0-108711.vbox-extpack
```

## ��������������������ѡ��

```
mkdir -p /home/virtualbox
VBoxManage createvm --name ubuntu --ostype "Ubuntu_64" --register --basefolder /home/virtualbox/
VBoxManage createvdi  --filename ubuntu/ubuntu.vdi --size 102400 #100GB
VBoxManage storagectl ubuntu --name storage_controller_1 --add ide
VBoxManage storageattach ubuntu --storagectl storage_controller_1 \
    --type hdd --port 0 --device 0  --medium ubuntu/ubuntu.vdi
VBoxManage storageattach ubuntu --storagectl storage_controller_1 \
    --type dvddrive --port 1 --device 0 --medium ubuntu-14.04.4-server-amd64.iso
VBoxManage modifyvm ubuntu --cpus 4 --memory 2048 --acpi on --boot1 dvd --nic1 nat --cableconnected1 on --vrde on --vrdeport 3389
```

## ���������

```
nohup VBoxHeadless -startvm ubuntu --vrde on -e  TCP/Ports=63389 &
```

## ���������

Windows��ʹ��`mstsc`Զ�����Ӽ��ɻ��һ��ͼ�ν�����ն����ϵͳ��װ