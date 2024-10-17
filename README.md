# Chatbot

Ce projet est un chatbot de cybersécurité construit avec Flask. Il utilise une base de connaissances et l'API Mistral pour générer des réponses.

## Project Overview

> Requirements
> - [Python > 3.0](https://www.python.org/downloads)


> Create virtual environment
> ```bash
> python -m venv venv
> ```

> Source virtual env
> ```bash
> source venv/bin/activate
> ```

> Install python dependencies
> ```bash
> pip install -r requirements.txt
> ```

## Project Architecture
```
.
├── src/                # project source files
│   ├── controllers/    # http responses handlers
│   ├── models/         # mysql models
│   ├── static/         # http static files
│   │   ├── images/         # static images
│   │   ├── scripts/        # static js scripts
│   │   └── style/          # static stylesheets (scss, fonts..)
│   │       └── build/      # static generated css stylesheets
│   ├── templates/      # http html templates
│   ├── utils/          # project utils
│   └── main.py         # project entry
├── docker-compose.yaml # docker compose entry
├── Dockerfile          # docker image
├── README.md
└── requirements.txt    # python dependencies
```

## Installation

> Clone the repository
> ```bash
> git clone git@github.com:toto31810/chatbot.git chatbot
> cd chatbot
> ```

> create the `.env` file
> ```
> MISTRAL_APIKEY='<mistral api_key>'
> 
> MYSQL_HOST='localhost'
> MYSQL_PORT=3306
> MYSQL_USER='server'
> MYSQL_DATABASE='chatbot'
> MYSQL_PASSWORD='<mysql password>'
> MYSQL_ROOT_PASSWORD='<mysql root password>'
> ```

> Build Docker Image
> ```bash
> docker compose build
> ```

> Run Docker Compose
> ```bash
> docker compose up -d
> ```

## Integration
```html
<style>
    #chatbot {
        position: fixed;
        bottom: 0;
        right: 0;
    }
</style>
<div id="chatbot">
    <iframe width="400" height="600" src="<chatbot endpoint>" frameborder="0"></iframe>
</div>
```
