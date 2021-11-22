FROM continuumio/miniconda3
WORKDIR /app

COPY freeze.yml .

RUN conda config --set restore_free_channel true && conda env create -n py39 -f freeze.yml && echo "conda activate py39" > ~/.bashrc

COPY . .

CMD ["python","manage.py","runserver","0.0.0.0:8000"]