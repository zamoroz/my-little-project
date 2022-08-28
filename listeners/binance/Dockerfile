FROM python:3.8
ENV PYTHONPATH=.

WORKDIR /code
COPY ./req.txt ./
RUN pip install -r req.txt

COPY ./ /code

CMD ["python", "main.py"]