FROM python:3-alpine

EXPOSE 80
WORKDIR /app
CMD ["/app/entrypoint.sh"]

RUN set -ex \
	&& apk add --no-cache --virtual .build-deps \
		gcc \
		make \
		libc-dev \
		musl-dev \
		libffi-dev \
	&& PIP_NO_CACHE_DIR=true \
	&& pip install pipenv \
	&& mkdir -p /db

COPY Pipfile.lock Pipfile /app/
RUN set -ex \
	&& pipenv install --system \
	&& pip uninstall -y pipenv \
	&& apk del .build-deps

COPY . /app/

