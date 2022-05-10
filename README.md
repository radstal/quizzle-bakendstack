# Basic Usage

## RUN

### Run with attached terminal

~~~ bash
docker-compose pull
docker-compose up 
~~~

### Run headless mode

~~~ bash
docker-compose pull
docker-compose up -d
~~~

## Kill and Delete everything in localstorage **volume** *(eg. stored mongo database)*

~~~ bash
docker-compose down -v
~~~

## devlopment mode

~~~ bash
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
~~~

## Pull from Internet Repo

~~~ bash
docker-compose pull
~~~

## Build and Push

~~~ bash
docker-compose build
docker-compose push
~~~
