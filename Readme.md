
# Project Title

Repositi ini berisi aplikasi machine learning end to end dengan streamlit dan fastapi

## Project workflow
![Diagram persiapan data](https://media.licdn.com/dms/image/C4E12AQFXLdW70AMxVA/article-inline_image-shrink_1000_1488/0/1528755587142?e=1694044800&v=beta&t=qkurOJUlMkMyP2tIdODVdOf1wHG0laziB_c-NE0BpTQ)


## Feature engineering 
![Diagram persiapan data](https://github.com/DwiCahyanto/API-concrete_str/blob/master/references/Model_diagram.drawio.png)
## Feature engineering 

![Diagram persiapan data](https://github.com/DwiCahyanto/API-concrete_str/blob/master/references/Model_diagram.drawio.png)
## API Reference

#### Predict items

```http
  Post/api/predict
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Cement` | `Float` | **Required**. None |
| `Fly_Ash` | `Float` | **Required**. None |
| `Water` | `Float` | **Required**. None |
| `Superplasticizer` | `Float` | **Required**. None |
| `Coarse_Aggregate` | `Float` | **Required**. None |
| `Fine_Aggregate` | `Float` | **Required**. None |
| `Age` | `Float` | **Required**. None |





## Running API
```http
  Uvicorn con_str-api-staging:app --reload
```
## Retraining model
```http
  Python concrete_str-yaml-without.py 
```
## Runing Docker
```http
  Docker-compose up 
```
