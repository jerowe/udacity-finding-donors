FROM continuumio/miniconda3:4.5.11

RUN apt-get update -y; apt-get upgrade -y
RUN apt-get install -y vim-tiny vim-athena ssh

RUN adduser --home /home/flask flask

USER flask
WORKDIR /home/flask

COPY environment.yml environment.yml

RUN conda env create -f environment.yml
RUN echo "alias l='ls -lah'" >> ~/.bashrc
RUN echo "source activate finding-donors" >> ~/.bashrc

ENV CONDA_EXE /opt/conda/bin/conda
ENV CONDA_PREFIX /home/flask/.conda/envs/finding-donors
ENV CONDA_PYTHON_EXE /opt/conda/bin/python
ENV CONDA_PROMPT_MODIFIER (finding-donors)
ENV CONDA_DEFAULT_ENV finding-donors
ENV PATH /home/flask/.conda/envs/finding-donors/bin:/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

ENV DONOR_DATA '/home/flask/data/census.csv'

RUN mkdir -p data
RUN mkdir -p scripts/flask_app

WORKDIR /home/flask/scripts

COPY . flask_app/

WORKDIR /home/flask/scripts
EXPOSE 5000

CMD ["/bin/bash", "-c", "/home/flask/scripts/start_flask_app.sh"]
#CMD ["/bin/bash", "-c", "tail -f /dev/null"]
