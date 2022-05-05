# Bewise.ai_task

This API allows to get required amount of questions from https://jservice.io/ API. It writes received questions to the DB in case they are new. Otherwise, new requests will be made untill new questions will be recevied. The API return the last existing question in the DB ( or empy list if there is none). 


## Installation
By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary.
The same is about DB settings and env variables storage(currently dotenv is being used). 
API requires [Docker](https://www.docker.com/products/docker-desktop/) to run.
Depending on your OS you may need to install [docker-compose](https://docs.docker.com/compose/install/).

Go to 'bewise_task' folder and run command:

```sh
cd bewise_task
docker-compose up
```


## Usage

Verify the deployment by sending POST request to your server.

#### Request examples:
![request example to empty DB](https://github.com/dkudrik/bewise.ai_task/bewise_task/main/request_example_to_empty_db?raw=true)
![request example](https://github.com/dkudrik/bewise.ai_task/bewise_task/main/request_example_to_empty_db?raw=true)


