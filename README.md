# clipthatoff_v2


## Setup Instructions

* Copy the `docker.env.sample` to `docker.env`
* Fill in your secret values
* `docker-compose build`
* `docker-compose up -d`
* Run `docker exec -it clipthatoffv2_db_1 psql -d postgres -U postgres` and once
  in run `create database clipthatoff_v2;`. Exit the docker shell afterwards
* Run `docker exec -it clipthatoffv2_web_1 python create.py
