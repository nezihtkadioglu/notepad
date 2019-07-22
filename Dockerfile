FROM python:3.6.9-slim

ENV INSTALL_PATH /home/notepad

RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

COPY ./source/ $INSTALL_PATH

RUN apt-get update -yq --fix-missing
RUN apt-get install -yq python3-tk
RUN python -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
