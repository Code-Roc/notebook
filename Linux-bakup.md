#���� ���� ���ݣ�

һ�����õı��ݼƻ�������Ҫ�����ݽű�Ӧ�õ������ݿ⡢ѹ����־�Ͷ�̬�����������ļ������ϴ���������������CDN

----

## Demo

����������漰��date��docker��tar��zip����ţqshell�����ʹ��

```bash
#!/bin/bash
pushd ����Ŀ¼
d=`date +%Y%m%d`
mkdir bakup$d
cd bakup$d
(docker exec �������� mysqldump -p���� ���ݿ�����) >database.sql
tar cvzf log.tar.gz ../log #ѹ��logĿ¼
cd ../
#ʹ��zip����ѹ����ѹ����ɾ��ԭ�ļ�
zip -r -P ѹ������ -m bakup$d.zip bakup$d/
#ʹ����ţ��qshell�ϴ������ļ�������ǰ��Ҫ�����˺�qshell account ���AK ���SK
#�������������ʾ��bakup$d.zip�ϴ���CDN�ϴ洢���ļ���Ϊ$d.zip
./qshell fput ���bucket������ $d.zip bakup$d.zip
#�������Ŀ��Ա��س���ɾ�������ļ���
#rm -r bakup$d.zip

```