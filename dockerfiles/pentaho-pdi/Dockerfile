FROM java:7
# Init ENV
ENV PENTAHO_VERSION 6.1
ENV PENTAHO_TAG 6.1.0.1-196

ENV PENTAHO_HOME /opt/pentaho

# Apply JAVA_HOME
RUN . /etc/environment
ENV PENTAHO_JAVA_HOME $JAVA_HOME
ENV PENTAHO_JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64

RUN apt-get update -y \
    && apt-get -y install wget unzip libswt-gtk-3-java libwebkitgtk-1.0-0 libswt-gtk-3-java xz-utils \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# nao ta extraindo, com problema no formato do xf ou o xz-utils nao instalado
RUN cd /tmp \
    && wget http://http.debian.net/debian/pool/main/s/swt4-gtk/swt4-gtk_4.6.0-2.debian.tar.xz \
    && tar xf swt4-gtk_4.6.0-2.debian.tar.xz -C /tmp \
    && make -C debian \
    && make -C debian install \
    && rm -rf /tmp/*

RUN groupadd -r pentaho && useradd -r -g pentaho pentaho \
    && mkdir $PENTAHO_HOME && chown -R pentaho:pentaho $PENTAHO_HOME
USER pentaho 

# Download Pentaho BI Server
RUN /usr/bin/wget --progress=dot:giga http://downloads.sourceforge.net/project/pentaho/Data%20Integration/${PENTAHO_VERSION}/pdi-ce-${PENTAHO_TAG}.zip -O /tmp/pdi-ce-${PENTAHO_TAG}.zip; \
    /usr/bin/unzip -q /tmp/pdi-ce-${PENTAHO_TAG}.zip -d  $PENTAHO_HOME; \
     rm /tmp/pdi-ce-${PENTAHO_TAG}.zip

# /usr/lib/jni/libswt-gtk-3836.so
# install libswt-gtk-4-java
# libswt-gtk-4-java no in apt => compile
ENV LIBPATH $LIBPATH:/usr/lib/jni

COPY scripts/ /opt/pentaho/data-integration/
COPY slave_dyn.xml /opt/pentaho/data-integration/

WORKDIR /opt/pentaho/data-integration

EXPOSE 8181

CMD ["./run.sh"]
