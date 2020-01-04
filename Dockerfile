FROM ubuntu:18.04
LABEL maintainer="cal.loomis@gmail.com"

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3 python3-pip python3-opencv -qq && \
    apt-get install -y -qq --no-install-recommends usbutils git && \
    pip3 install requests flask && \
    apt-get clean && \
    pip3 install speech_recognition && \	
    rm -fr /var/lib/apt/lists
	
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

COPY . /root/speechtotext

CMD ["/root/speechtotext/app.py", "80", "640", "480", "4"]
