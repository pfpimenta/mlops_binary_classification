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
`curl -X GET http://0.0.0.0:9200/classify_test_sample`

- Call classify_sample endpoint:
`curl -X GET http://0.0.0.0:9200/classify_sample`

- Call classify_batch endpoint:
`curl -X GET http://0.0.0.0:9200/classify_batch`

## TODOs
- Implement other metrics: precision, recall, F1
- Improve test data: put more negative samples. It does not matter if it is not balanced.
- Model persistance: saving the model with a different name each time.
- Save train.csv and test.csv locally instead of generating test and train datasets again each time.
- Improve model validation.
- Improve data validation.
