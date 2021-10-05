FROM python:3.9
WORKDIR /bjones
ADD src/requirments.txt /bjones/src/requirments.txt
RUN pip3 install -r /src/requirments.txt
COPY . .