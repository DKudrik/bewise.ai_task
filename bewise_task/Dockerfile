FROM python:3.10-slim
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
CMD ["gunicorn", "bewise_task.wsgi:application", "--bind", "0:8000"]