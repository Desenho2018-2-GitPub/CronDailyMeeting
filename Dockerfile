FROM ubuntu:latest

ADD requirements.txt requirements.txt

ADD crontab /etc/cron.d/issue-cron

ADD create_issue.py /root/create_issue.py

ADD issue_body.md /root/issue_body.md

ADD env.json /root/env.json

ADD secret.json /root/secret.json

RUN apt-get update && apt-get -y install \
  cron \
  python3 \
  python3-pip

RUN pip3 install -r requirements.txt

RUN chmod 0644 /etc/cron.d/issue-cron

RUN crontab /etc/cron.d/issue-cron

RUN touch /var/log/cron_create.log && touch /var/log/cron_close.log

CMD ["cron", "-f"]
