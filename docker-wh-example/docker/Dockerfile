FROM debian:jessie

MAINTAINER Daniel Keler <danielk@jfrog.com>

RUN apt-get update && apt-get install -y unzip

ADD demo-application-1.0.zip /demo-application-1.0.zip

WORKDIR /tmp

RUN unzip /demo-application-1.0.zip && rm -rf /demo-application-1.0.zip demo-application-1.0.deb

