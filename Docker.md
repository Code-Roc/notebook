# Install ��װ

����μ�[��η�ǽ](https://github.com/zjuchenyuan/notebook/blob/master/code/ssprivoxy.txt)������http proxy

��װ֮ǰ�������޸�aptԴ

��װ��� 

    curl -sSL https://get.docker.com/ | sh
    
�������һ����apt-get install docker-engine��ʱ�ϳ�������������������Ҫ���ĵȴ�

��װ��ִ��docker version��û�б�����

--------

# ���پ�������

> ��ִ�����²���֮ǰ������docker�İ汾��`docker -v`

> ������docker�汾Ϊ1.6.2,��ο�ж��docker

##����ʹ��USTC��Դ��

���ԣ�https://lug.ustc.edu.cn/wiki/mirrors/help/docker

�޸� /etc/docker/daemon.json ���루û�и��ļ��Ļ������Ƚ�һ������

    {
      "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
    }

##Ҳ��������ʹ��daocloud�ṩ��dao����

TODO:�о�dao�İ�װ������Ҫdaomonit

-------

#Docker�ɰ汾ж��

������docker��ʹ��apt-get install docker.io��װ�ģ�����ִ����������ж�أ�

    apt-get remove docker.io
    apt-get autoremove
    rm -rf /var/lib/docker

Ȼ��Ϳ���ִ�а�װ������