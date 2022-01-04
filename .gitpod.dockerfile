FROM gitpod/workspace-full
# Install image generator
USER root

RUN apt-get update && apt-get install -y -y build-essential python3.6 python3-pip python3.6-venv graphviz libgraphviz-dev pkg-config

ENV IP=0.0.0.0
ENV PORT=3000
