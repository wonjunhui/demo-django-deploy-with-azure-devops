FROM python:3.7-slim
MAINTAINER Chinseok Lee <me@askcompany.kr>

WORKDIR /dj
ADD . /dj

ENV PYTHONUNBUFFERED  1

RUN python3.7 -m pip install -r reqs/prod_docker.txt

EXPOSE 80

# ssh
# ADD sshd_config /etc/ssh/
# RUN echo "root:d0\$iskawk!" | chpasswd && \
#     echo "cd /home" >> /etc/bash.bashrc && \
#     apt-get install -y --no-install-recommends openssh-server vim curl wget tcptraceroute htop
# EXPOSE 2222

CMD ["/bin/sh", "/dj/entry.sh"]

