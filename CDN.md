# UPYUN

## FTP

人家支持用ftp传输文件，而且用ftp似乎不对流量计费

ftp://v0.ftp.upyun.com 

用户名是"操作员名/服务名"（其中/字符是用户名的一部分）,密码为"操作员密码"

## UpyunManager

http://micyin.b0.upaiyun.com/manager-for-upyun/manager-for-upyun-0.0.6-win32.exe


## curlftpfs

http://curlftpfs.sourceforge.net/

注意命令中的 ftp://用户名:密码@v0.ftp.upyun.com 其中的用户名的/符号需要改为%2f

----

# Qiniu

## 使用qshell上传文件夹

    qshell qupload [<ThreadCount>] <LocalUploadConfig>

需要写一个config文件，具体参见官方文档

[http://developer.qiniu.com/code/v6/tool/qshell.html](http://developer.qiniu.com/code/v6/tool/qshell.html)

[https://github.com/qiniu/qshell/wiki/qupload](https://github.com/qiniu/qshell/wiki/qupload)