# E-commerce API

## Description

The objective of this project is to create an API to manage a web store, in which the user will able to see a product stock, receive purchase orders and make refunds.

## Tools Used

- [Python](https://realpython.com/installing-python/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/installation/)
- [Flask SQLALchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#installation)
- [MySQL](https://dev.mysql.com/doc/workbench/en/wb-installing.html)
- [Docker](https://docs.docker.com/get-docker/)

## How To Run It

To run a docker container using a mysql image, run the following command

To run a docker container using a mysql image, run the following command

```shell
docker run --name ecommerce-db -v /db:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=senha123 -p 3306:3306 -d mysql:latest
```

Create a virtual environment by running:

```shell
python3 -m venv .venv
```

And then activate it by running:

```shell
source .venv/bin/activate
```

Now install the dependencies:

```shell
pip install -r requirements.txt
```
## What I've Learned

I learned how to use flask and flask SQLAlchemy to create an API.