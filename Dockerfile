FROM python:3

ADD libconfig.py /

CMD [ "python", "./libconfig.py" ]
