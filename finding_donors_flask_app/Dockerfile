FROM continuumio/miniconda3:4.5.11

RUN apt-get update -y; apt-get upgrade -y
RUN apt-get install -y vim-tiny vim-athena ssh

RUN adduser --home /home/flask flask

USER flask
WORKDIR /home/flask

RUN mkdir -p finding_donors_flask_app

WORKDIR /home/flask/finding_donors_flask_app

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

#EXPOSE 5000
COPY . ./

CMD ["/bin/bash", "-c", "/home/flask/finding_donors_flask_app/start_flask_app.sh"]
