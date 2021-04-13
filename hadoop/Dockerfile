FROM debian:buster

RUN set -ex; \
    apt-get update; \
    apt-get -y install sudo; \
    sudo apt -y update; \
    sudo apt -y install

RUN sudo apt-get install default-jre -y
RUN sudo apt install curl -y
RUN sudo apt-get install git wget vim ssh -y
RUN wget https://archive.apache.org/dist/hadoop/core/hadoop-3.3.0/hadoop-3.3.0.tar.gz
RUN tar zxvf hadoop-3.3.0.tar.gz

RUN mv hadoop-3.3.0 /usr/local/hadoop && \
    mkdir /usr/local/hadoop/logs

RUN echo "export HADOOP_HOME=/usr/local/hadoop \
nexport HADOOP_INSTALL=/usr/local/hadoop \
nexport HADOOP_MAPRED_HOME=/usr/local/hadoop \
nexport HADOOP_COMMON_HOME=/usr/local/hadoop \
nexport HADOOP_HDFS_HOME=/usr/local/hadoop \
nexport YARN_HOME=/usr/local/hadoop \
nexport HADOOP_COMMON_LIB_NATIVE_DIR=/usr/local/hadoop/lib/native \
nexport PATH=$PATH:/usr/local/hadoop/sbin:/usr/local/hadoop/bin \
nexport HADOOP_OPTS=\"-Djava.library.path=/usr/local/hadoop/lib/native\"\
nexport HDFS_NAMENODE_USER=root\
nexport HDFS_DATANODE_USER=root\nexport YARN_RESOURCEMANAGER_USER=root\nexport YARN_NODEMANAGER_USER=root\nexport HDFS_SECONDARYNAMENODE_USER=root\n" >> /root/.bashrc

RUN echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64 " >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh

RUN echo "export HADOOP_CLASSPATH+=\" /usr/local/hadoop/lib/*.jar\"" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh


# Install git, supervisor, VNC, & X11 packages
RUN set -ex; \
    apt-get update; \
    apt-get install -y \
      bash \
      fluxbox \
      net-tools \
      novnc \
      supervisor \
      x11vnc \
      xterm \
      xvfb

# Setup demo environment variables
ENV HOME=/root \
    DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=C.UTF-8 \
    DISPLAY=:0.0 \
    DISPLAY_WIDTH=1024 \
    DISPLAY_HEIGHT=768 \
    RUN_XTERM=yes \
    RUN_FLUXBOX=yes
    
COPY . /app
CMD ["./app/entrypoint.sh"]
EXPOSE 8080