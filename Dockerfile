FROM apache/spark-py

USER root

RUN apt update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y ant && \
    apt-get clean;

USER 185

WORKDIR /opt/applications
RUN chmod -R 777 /opt/applications

COPY app/src/scripts/* /opt/applications/

