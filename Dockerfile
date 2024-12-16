FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    openjdk-11-jdk curl python3 python3-pip && \
    apt-get clean

RUN pip install antlr4-python3-runtime==4.13.2

ENV ANTLR_VERSION=4.13.2
ENV ANTLR_LOCAL_JAR_PATH=/usr/local/lib/antlr-${ANTLR_VERSION}-complete.jar

RUN curl -o ${ANTLR_LOCAL_JAR_PATH} https://www.antlr.org/download/antlr-4.13.2-complete.jar

RUN echo 'alias antlr4="java -jar /usr/local/lib/antlr-4.13.2-complete.jar"' >> ~/.bashrc

SHELL ["/bin/bash", "-c"]
RUN echo "source ~/.bashrc" >> ~/.bash_profile && source ~/.bashrc

WORKDIR /dir

CMD ["/bin/bash"]