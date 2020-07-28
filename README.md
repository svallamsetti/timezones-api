# Running timezones API

This repo contains a flask app which provides timezones API.

# Requirements
   * [Docker](https://docs.docker.com/get-docker/)
   * [Docker Compose](https://docs.docker.com/compose/install/)

# Installation
Once docker and docker compose are installed follow the below steps to spin this app.

#### Steps:
1. clone this repo 
`git clone https://github.com/svallamsetti/timezones-api.git`
2. `cd timezones-api`
3. `docker-compose up`
> This step will take some time to download the image used in Dockerfile. The Dockerfile will take care of installing all the required dependencies.
4. The app can be accessed on   `http://127.0.0.1:5001`
> If the above port is occupied you can change the port by creating `.env` file in the project root directory and by setting the port to the variable `HOST_PORT`. You can refer to `.env-example`. A `docker-compose restart` is required for the changes to be affected.
5. This app provides Swagger-UI documentation. You can access the Swagger-UI at `http://127.0.0.1:5001/swagger`. **Note:** If you changed the port in previous step this might not work. You would need to change the URL in the `static/swagger.json`. This swagger list all the API'S produced by this application. You can call the API'S using Swagger-UI.

# Running tests

`docker-compose exec apis pytest`

# List of API'S

1. /timezones `http://127.0.0.1:5001/api/timezones`
2. /timezones/{timezoneId} `http://127.0.0.1:5001/api/timezones/{timezoneId}` Ex:  `http://127.0.0.1:5001/api/timezones/1`