#create a dockerfile that will be used to build a python image

# Use an official Python runtime as a parent image

FROM ubuntu:latest

# Install Python and essential build tools
RUN apt-get update && \
    apt-get install -y python3 python3-pip
WORKDIR /app
COPY . /app

RUN apt -y install git
RUN git clone https://github.com/adrian154/masscan.git
WORKDIR /app/masscan
RUN make install
WORKDIR /app

RUN apt -y install python3.10-venv
RUN python3 -m venv .venv
RUN . .venv/bin/activate
RUN pip3 install pymongo


CMD ["python3", "main.py"]

