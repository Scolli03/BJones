FROM python:3.9
WORKDIR /bjones
ADD /src/requirements.txt /bjones/src/requirments.txt
RUN pip3 install -r /bjones/src/requirments.txt