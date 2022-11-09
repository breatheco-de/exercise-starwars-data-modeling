FROM gitpod/workspace-full
# Install image generator
USER root

RUN apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config python3-dev

RUN pyenv install 3.6.4

ENV IP=0.0.0.0
ENV PORT=3000
