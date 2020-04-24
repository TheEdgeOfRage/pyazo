# THIS PROJECT HAS BEEN REWRITTEN AND MOVED TO [pyazo-screenshot](https://github.com/pyazo-screenshot)

# Pyazo

Pyazo is a self-hosted screenshot upload utility. It allows you to take a screenshot of part of your screen and automatically upload it to your own server.

It is comprised by a cross-platform client in Python which defers the actual taking of screenshot to OS built-in tools (macOS and Windows) or common utilities (Linux distributions). The server is written as a RESTful Flask app with support for basic user accounts.

## Compatibility

### Server

* Python >= 3.5 (check with `python --version`)

## Installation

The only official supported way to run the server is through docker-compose. First make a copy of the `.env-example` file, name it `.env` and change the settings inside accordingly.

| Key        | Default                    | Description                                                  |
|------------|----------------------------|--------------------------------------------------------------|
| SECRET_KEY | test-key                   | API endpoint to send the image file in a POST request        |
| FLASK_APP  | app                        | Name of the flask app variable inside run.py (leave default) |
| FLASK_ENV  | production                 | Flask environment. Set to development to enable debugging    |
| WEB_PORT   | 80                         | Internal port inside the container (leave default)           |
| HOST       | https://pyazo.example.com/ | Protocol and FQDN of your server                             |

Build the container using:

```shell
docker-compose build
```

Then run it using:

```shell
docker-compose up -d
```

## License and Credits

BSD 3-Clause

[Python]: <https://www.python.org/downloads/>
[Docker]: <https://docs.docker.com/>
[Docker Compose]: <https://docs.docker.com/compose/>

