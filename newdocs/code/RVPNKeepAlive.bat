REM ���ڱ�֤Windows�������ϵ�rvpn�����Ͽ��󾡿�����
REM ���ű������������߼�������Ҫдһ��Loader.batÿ���1min(���Զ���)����һ�α��ű�
REM �߼�������������˳���¼�ĵ������Զ����������curl��ȡ��������ʧ���Զ�����
REM ����rvpn���Զ���������������ܵ��´����ڴ�ռ�ã������������Զ��������������Chrome.exe

taskkill /f /im LogoutTimeOut.exe
if "%errorlevel%"=="0" taskkill /f /im SangforCSClient.exe&ping www.baidu.com&start "" "C:\Program Files\Sangfor\SSL\SangforCSClient\SangforCSClient.exe" /ShortCutAutoLogin&& taskkill /f /im Chrome.exe &ping www.baidu.com
curl 10.71.45.100 >nul
if "%errorlevel%"=="0" exit 0
curl www.cc98.org >nul
if "%errorlevel%"=="0" exit 0
taskkill /f /im SangforCSClient.exe
ping -n 2 ip.cn
start "" "C:\Program Files\Sangfor\SSL\SangforCSClient\SangforCSClient.exe" /ShortCutAutoLogin
taskkill /f /im Chrome.exe