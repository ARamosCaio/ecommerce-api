# E-commerce API

## Description

The objective of this project is to create an API to manage a web store, in which the user will able to see a product stock, receive purchase orders and make refunds.

## Tools Used

- [Python](https://realpython.com/installing-python/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/installation/)

## How To Run It

To run a docker container using a mysql image, run the following command

```shell
docker run --name ecommerce-db -v /db:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=senha123 -p 3306:3306 -d mysql:latest
```
 
## What I've Learned