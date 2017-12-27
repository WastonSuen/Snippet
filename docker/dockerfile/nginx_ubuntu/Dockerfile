FROM sshd:docker

MAINTAINER from suen.cn by suen (sunzh95@hotmail.com)

RUN \
    apt-get install -y nginx && \
    rm -rf /var/lib/apt/lists/* && \
    echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \
    chown -R www-data:www-data /var/lib/nginx

RUN echo "Asia/Shanghai" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

ADD run.sh /run.sh
RUN chmod 755 /*.sh
VOLUME ["/etc/nginx/sites_enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx"]
WORKDIR /etc/nginx
CMD ["/run.sh"]

EXPOSE 80
EXPOSE 443
