FROM python:3.9-alpine

WORKDIR /cfs

COPY install-packages.sh .
RUN ./install-packages.sh

COPY . .
RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0