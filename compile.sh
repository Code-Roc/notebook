#! /bin/bash
rm *.html
bundle exec jekyll build -d docs --no-watch -I
cp docs/*.html ./
echo "<hr><small>Last updated: `date --iso-8601=seconds`&nbsp;&nbsp;&nbsp;<a href=http://www.miitbeian.gov.cn/>浙ICP备15043819号-2</a>&nbsp;&nbsp;<a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602007826"><img src="beian.png" height="14px">浙公网安备 33010602007826号</p></a></small>" >> index.html
cp code/randomstring.html ./p.html
cp doc/python/quickstart.html ./
python3 << PYTHON
import os
import re
replace_css=re.compile(r'/assets/css/style.css\?v=.*"')
for filename in os.listdir("."):
    if filename.endswith(".html"):
        if filename in ("p.html","quickstart.html"):
            continue
        data = open(filename,encoding='utf-8').read()
        data = replace_css.sub('assets/css/style.css"',data)
        if filename != "index.html":
            data = data.replace("View on GitHub</a>","""View on GitHub</a>&nbsp;<a href="https://py3.io" class="btn btn-back"><span class="icon"></span>Back to Index</a>""")
        if filename == "Python.html":
            data = data.replace('<span class="err">','<span class="s">')
        data = data.replace("</html>","""<script src="https://py3.io/assets/instantclick.min.js"></script><script data-no-instant>InstantClick.init();</script></html>""")
        open(filename,"w",encoding='utf-8').write(data)
PYTHON
#刷新又拍云缓存，代码在https://github.com/zjuchenyuan/EasyLogin/tree/master/examples/upyun
pushd /mnt/d/Seafile/Developer/EasyLogin/examples/upyun/
python3 upyun.py https://py3.io/*.html 
popd
python3 code/upyun_purge.py
