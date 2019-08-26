FROM python:3.7

RUN pip install -U pip

ADD requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

RUN pip uninstall MarkupSafe==1.1.1 -y