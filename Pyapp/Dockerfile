#create a dockerfile that will be used to build a python image

# Use an official Python runtime as a parent image

FROM ubuntu:20.04
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
RUN apt-get install libpcap0.8 libpcap0.8-dev libpcap-dev

RUN apt -y install python3-venv
RUN python3 -m venv .venv
RUN . .venv/bin/activate


CMD ["python3", "main.py"]

