# Install ��װ

����μ�"��η�ǽ"������http proxy

�ٷ���װ�ű���https://get.docker.com/

��װ��� 

    curl -sSL https://get.docker.com/ | sh
    
�������һ����apt-get install docker-engine��ʱ�ϳ�������������������Ҫ���ĵȴ�

--------

# ���پ�������

##����ʹ��USTC��Դ��

���ԣ�https://lug.ustc.edu.cn/wiki/mirrors/help/docker

�޸� /etc/docker/daemon.json��Linux�� ������ Daemon��

���ڸ������ļ��м��루û�и��ļ��Ļ������Ƚ�һ������

    {
      "registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]
    }

##Ҳ��������ʹ��daocloud�ṩ��dao����

TODO:�о�dao�İ�װ������Ҫdaomonit