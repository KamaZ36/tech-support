FROM python:3.11

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR ./app

COPY ./requirements.txt .

RUN pip3 install --user package-name
RUN pip3 install pip --upgrade
RUN pip3 install --no-cache-dir -r ./requirements.txt

COPY . .

CMD ["python3", "main.py"]
