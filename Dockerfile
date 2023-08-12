FROM python:3.9
COPY requirements.txt .

RUN pip install --user -r requiments.txt
CMD [ "python", "main.py" ]