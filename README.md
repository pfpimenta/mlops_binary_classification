# mlops_binary_classification
Repositorio para um desafio de desenvolvimento MLOps para uma oportunidade de emprego.

O desafio tem como base um problema do Kaggle:
https://www.kaggle.com/mlg-ulb/creditcardfraud

O objetivo desse projeto é, então, desenvolver uma solução estruturada para levar o modelo preditivos para produção.
O projeto deve incluir:
- Uma solução para predições instantâneas
- Uma solução para predições em lote, grandes quantidades de predições
- Gerenciamento de dependências externas
- Geração de features


## How to use the API using linux terminal:
- Call Hello-World endpoint:
`curl -X GET http://0.0.0.0:9200/`

- Call Healthcheck endpoint:
`curl -X GET http://0.0.0.0:9200/healthcheck`

- Call train endpoint:
`curl -X GET http://0.0.0.0:9200/train`

- Call classify_sample endpoint:
`curl -X GET http://0.0.0.0:9200/classify_random_sample`

- Call classify_sample endpoint:
`curl -X GET http://0.0.0.0:9200/classify_sample`

- Call classify_batch endpoint:
`curl -X GET http://0.0.0.0:9200/classify_batch`

## TODOs
- Some kind of feature generation/engineering.
- Save metadata (metrics, training time, data used, etc) when a model is trained and saved.
- Improve model validation.
- Improve data validation.

## Features
TODO ! escrever mais aqui
- API with 6 endpoints
    - /: hello world checkpoint (may be useful to test if API is up).
    - /healthcheck: returns current system health information.
    - /train: trains a binary classifier model and saves its state in the API for future use.
    - /classify_random_sample: creates a sample with random features, classifies it using the most recent trained model, and then returns the result.
    - /classify_sample: classifies the sample given as a query argument using the most recent trained model.
    - /classify_batch: classifies the samples in the batch given as a query argument using the most recent trained model.
- Pre-commit: verification to ensure code style consistency + some other verifications
- Dependecies management: one requirements.txt file containing the dependencies of the API and another containing the dependencies of the test functions.
- Basic model validation: for now, only checks if metrics are above an acceptable level.
- Basic data validation: for now, only checks if data has the expected features and if each feature has the expected type.
