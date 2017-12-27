FROM sshd:ubuntu1404

MAINTAINER from suen.cn by suen (sunzh95@hotmail.com)

RUN apt-get update
RUN apt-get install -y python git
COPY get-pip.py /get-pip.py
RUN python /get-pip.py
RUN git config --global credential.helper store

COPY flasks /root/flasks
RUN mkdir /root/flasks/logs

COPY pip.conf /root/.pip/pip.conf
RUN pip install -r /root/flasks/deploy_conf/requirements.txt

RUN mkdir -p /etc/supervisor/supervisor.d
COPY supervisord.conf /etc/supervisor/supervisord.conf
RUN ln -s /root/flasks/deploy_conf/supervisord.conf /etc/supervisor/supervisor.d/wx_api.conf

RUN echo "Asia/Shanghai" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

COPY start.sh /start.sh
COPY update.sh /update.sh
RUN chmod 755 /*.sh
VOLUME ["/etc/supervisor/supervisor.d", "/root/flasks/logs"]
WORKDIR /root/flasks
EXPOSE 10011

CMD ["/start.sh"]