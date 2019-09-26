FROM httpd

COPY res/ /var/www/html/
COPY setup.sh /tmp/
# Add AliasMatche for each page

RUN bash /tmp/setup.sh
