#Git��ѧϰ�ʼǿ�

> �ο� http://igit.linuxtoy.org/

----

#��������

����ҳ���ȴ�����repo�����ú�.gitignore

```bash
git clone  github�ṩ�ĵ�ַ(��ssh��)
#Ȼ�󶪴����ȥ��
git add .
git commit -a -m "��θ���Щɶ��"
git push
```

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

#�ٴ����

ͨ���޸�~/.profile�����ñ�������

```
alias gs='git status '
alias ga='git add '
alias gb='git branch '
alias gc='git commit'
alias gd='git diff'
alias go='git checkout '
alias gl="git log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short"
```

Ҫ������Ч������ִ��source ~/.profile

#git status

�鿴״̬��~

#git reset

�Ѿ�`git add`�ˣ���ȡ����һ������`git reset`

#git checkout

������������㻵����Ҫ�ع����ϴ�commit����`git checkout -- �ļ���`

----

#��ѧ

* ΪɶҪ**git add**��?

��Ϊ��Щʱ�������ļ������ǲ���ص��޸ģ�Ӧ�÷ֱ��ύ����

> ͨ���ֿ��ݴ���ύ�����ܹ��������׵ص���ÿһ���ύ��