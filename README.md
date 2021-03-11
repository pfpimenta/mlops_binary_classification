# mlops_binary_classification
Repositorio para um desafio de desenvolvimento MLOps.

O desafio tem como base um problema do Kaggle:
https://www.kaggle.com/mlg-ulb/creditcardfraud

O objetivo desse projeto é, então, desenvolver uma solução estruturada para levar o modelo preditivos para produção.
O projeto deve incluir:
- Uma solução para predições instantâneas
- Uma solução para predições em lote, grandes quantidades de predições
- Gerenciamento de dependências externas
- Geração de features


## How to build the docker container:
`sh docker_build.sh`

## How to use the API using linux terminal:
- Call Hello-World endpoint:
`curl -X GET http://0.0.0.0:9200/`

- Call Healthcheck endpoint:
`curl -X GET http://0.0.0.0:9200/healthcheck`

- Call train endpoint:
`curl -X GET http://0.0.0.0:9200/train`

- Call classify_random_sample endpoint:
`curl -X GET http://0.0.0.0:9200/classify_random_sample`

- Call classify_sample endpoint:
`curl -X GET http://0.0.0.0:9200/classify_sample?sample=<sample>`

- Call classify_batch endpoint:
`curl -X GET http://0.0.0.0:9200/classify_batch?batch=<batch>`

For endpoints classify_sample and classify_batch enpoints, you need to send the sample or batch in a JSON format as a query string parameter.

## TODOs
- Some kind of feature generation/engineering.
- Save metadata (metrics, training time, data used, etc) when a model is trained and saved.
- Improved model persistance: have the option to choose between models and/or upload trained models.
- Improve model validation.
- Improve data validation.
- Unit and integration tests.

## Main project features
- API with 6 endpoints
    - /: hello world endpoint (may be useful to test if API is up).
    - /healthcheck: returns current system health information.
    - /train: trains a binary classifier model and saves its state in the API for future use.
    - /classify_random_sample: creates a sample with random features, classifies it using the most recent trained model, and then returns the result.
    - /classify_sample: classifies the sample given as a query argument using the most recent trained model.
    - /classify_batch: classifies the samples in the batch given as a query argument using the most recent trained model.
- Pre-commit: verification to ensure code style consistency + some other verifications]
- Dependecies management: one requirements.txt file containing the dependencies of the API and another containing the dependencies of the test functions.
- One basic automated test for each endpoint
- Basic model validation: for now, only checks if metrics are above an acceptable level.
- Basic data validation: for now, only checks if data has the expected features and if each feature has the expected type.
- Logging
- Data cleaning and preparation: generation of train and test datasets in a way that deals with the class imbalance of the raw data.
- Smart data management: instead of having it saved in the repository, automatically downloads from kaggle when container is ran. When train and test datasets are generated, they are saved in the container to avoid generating them again.
- Multiple binary classification metrics: F1, Precision, Recall, PR AUC, and ROC AUC.
- Management of trained models: when the API trains a model, it saves it for future use.
