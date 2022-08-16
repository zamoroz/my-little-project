FROM python:3.8
ENV PYTHONPATH=.

WORKDIR /code
COPY ./req.txt ./
RUN pip install -r req.txt
RUN pip freeze -r req.txt
COPY ./ /code

EXPOSE 50051

CMD ["python", "main.py"]