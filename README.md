<p align="center">
<img src="https://raw.githubusercontent.com/leonardomathon/sqleyes-api/develop/design/logo-combined.svg" alt="SQLEyes - API" title="SQLEyes API logo" style="max-width:100%; width:60%">
</p>

---

## About SQLEyes-api

SQLEyes-api is the official REST API for SQLEyes. Using this api allows you to analyzing simple, raw SQL queries for common sql anti-patterns by leveraging the logic of SQLEyes.

## Usage

This package can be run containerized using Docker or manually. The Dockerfile is intended to use in production whilst the manual method is intended to be used during development.

### Usage during development

Using `pip install -r requirements.txt`. After installation, open a terminal in the root directory and run `python -m api/app.py`. This starts a development server on `localhost:5000`.

### Usage in production

Build the container using `Docker build -t [imagename] .` and run it using `docker run -p 5000:5000 --rm --name [containername] [image]`.

## Acknowledgements

> This project was developed as a master's graduation project at Eindhoven University of Technology. It is part of a series of packages and tools, namely related to the [SQLEyes](https://github.com/leonardomathon/sqleyes) Python package and the [QuerySandbox](https://querysandbox.com) web app that uses this API.
