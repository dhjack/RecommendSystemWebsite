# 电影推荐系统 -- 前端部分
实际的运行，需要依赖[推荐引擎](https://github.com/dhjack/RecommendSystemEngines)。
页面提供两种反馈方式：
1. 直接点击页面上面的“喜欢”和“不喜欢”按钮
2. 通过语音方式交互

# 安装
```
git clone https://github.com/dhjack/RecommendSystemWebsite.git
cd RecommendSystemWebsite
pip install -r requirements.txt
```

# 配置文件
可以直接修改文件*web/default_settings.py*。也可以添加并修改文件*instance/settings.cfg*。后面的会覆盖前面的内容。
主要需要处理的是数据库相关配置。

# Flask直接运行
```
pyhon run.py
```

# 部署到apache中

1. 安装 wsgi
sudo apt-get install libapache2-mod-wsgi
2. 修改相关文件目录
    * chrome只能在https协议下才能访问麦克风，所以如果需要支持chrome，需要部署为https模式

    ```
    sudo vim default-ssl.conf
    #文件内容如下
    <IfModule mod_ssl.c>
        <VirtualHost _default_:443>
            ServerAdmin webmaster@localhost

            DocumentRoot /var/www/RecommendSystemWebsite

            WSGIScriptAlias / /var/www/RecommendSystemWebsite/web.wsgi

            SSLEngine on
            SSLCertificateFile	/etc/apache2/ssl/server.crt
            SSLCertificateKeyFile /etc/apache2/ssl/server.key

            <FilesMatch "\.(cgi|shtml|phtml|php)$">
                    SSLOptions +StdEnvVars
            </FilesMatch>
            <Directory /usr/lib/cgi-bin>
                    SSLOptions +StdEnvVars
            </Directory>
        </VirtualHost>
    </IfModule>
    # 需要这一步生效
    sudo a2ensite
    ```
    * 如果部署http模式
    ```
    sudo vim 000-default.conf
    # 文件内容如下
    <VirtualHost *:80>

            ServerAdmin webmaster@localhost

            DocumentRoot /var/www/RecommendSystemWebsite

            WSGIScriptAlias / /var/www/RecommendSystemWebsite/web.wsgi

            ErrorLog ${APACHE_LOG_DIR}/error.log
            CustomLog ${APACHE_LOG_DIR}/access.log combined

    </VirtualHost> 
    ```
3. 最后都需要重启
```
sudo /etc/init.d/apache2 restart   
```
