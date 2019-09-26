cat << ! >> /usr/local/apache2/conf/httpd.conf
Alias '/home' /var/www/html/index.html
<Directory "/var/www/html/">
    Require all granted
</Directory>
!

