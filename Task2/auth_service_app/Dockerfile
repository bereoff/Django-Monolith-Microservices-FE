# pull official base image
FROM python:3.12.0-bullseye AS app

# set work directory
WORKDIR /app

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev pkg-config -y\
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && mkdir /static 


ENV PYTHONDONTWRITEBYTECODE="true" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="/app" \
    PATH="${PATH}:/home/python/.local/bin" \
    DJANGO_SETTINGS_MODULE="core.settings" 
 
# copy project
COPY . .

# install dependencies
RUN pip install -r requirements.txt \
    && pip install --upgrade pip 


#entrypoynt
# COPY ./docker/entrypoint.sh .
RUN sed -i 's/\r$//g' /app/docker/entrypoint.sh
RUN chmod +x /app/docker/entrypoint.sh


ENTRYPOINT ["/app/docker/entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "-c", "python:core.gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
