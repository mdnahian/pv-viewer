FROM centos:7

RUN mkdir -p /opt/pvviewer/lib/web/app
ADD ./app /opt/pvviewer/lib/web/app

RUN yum -y update && \
    yum -y install \
    python3 \
    python3-devel \
    python3-setuptools \
    gcc \
    nginx \
    net-tools \
    less && \
    pip3 install -r /opt/pvviewer/lib/web/app/requirements.txt

ADD uwsgi.ini /etc/uwsgi/
ADD nginx.conf /etc/nginx/
ADD supervisor.conf /etc/supervisor/

EXPOSE 8080

USER nobody

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]