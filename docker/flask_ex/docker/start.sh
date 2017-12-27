#!/bin/bash
/usr/sbin/sshd &
/usr/local/bin/supervisord -c /etc/supervisor/supervisord.conf