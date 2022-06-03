FROM openjdk:11

ENV SBT_VERSION 1.3.13

RUN \
  curl -L -o sbt-$SBT_VERSION.deb https://scala.jfrog.io/artifactory/debian/sbt-$SBT_VERSION.deb && \
  dpkg -i sbt-$SBT_VERSION.deb && \
  rm sbt-$SBT_VERSION.deb && \
  apt-get update && \
  apt-get install sbt && \
  sbt sbtVersion

# (sbt sbtVersion will force the fetching of the right sbt jar needed)

WORKDIR /root/project
