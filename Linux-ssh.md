#SSH

## ��ͬ������ʹ�ò�ͬ��id_rsa

�޸�`.ssh/config`:
```
Host myshortname realname.example.com
    HostName realname.example.com
    IdentityFile ~/.ssh/realname_rsa # private key for realname
    User remoteusername

Host myother realname2.example.org
    HostName realname2.example.org
    IdentityFile ~/.ssh/realname2_rsa
    User remoteusername
```

##�����˿ڿ���һ����ʱ��sshd��

```
which sshd
/usr/sbin/sshd -oPort=2333
```

## ssh�������

�μ���http://www.tuicool.com/articles/UVRNfi

��������22�˿�ת����������������2222�˿ڣ�

```
ssh -b 0.0.0.0 -L 2222:127.0.0.1:22 user@ip
```

ע��������ǰ��Ҫ�����������¼�Լ��޸�������������sshd_config������GatewayPorts  yes

----