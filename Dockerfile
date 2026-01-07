FROM python:3.10.19 

COPY . /main

WORKDIR /main

# Upgrade pip 
RUN pip install --upgrade pip

RUN    pip install --no-cache-dir -r requirements.txt

EXPOSE  8000



CMD ["gunicorn", "api.main:app", "-k", "uvicorn.workers.UvicornWorker", "--workers", "1", "--bind", "0.0.0.0:8000"]