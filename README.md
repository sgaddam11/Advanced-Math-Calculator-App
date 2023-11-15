
# Adnaced Math Calculator Flask Web Application
This web service provides the user with   
    1. Lucas series,   
    2. Fibonacci series,   
    3. Factorial of a number after user gives the input integer. 

You can build and run the docker image using the below commands
```
docker-compose build 
docker-compose up -d
```


Once the docker image is up and running you can access the web service using the below url

 http://127.0.0.1:80 with the below API calls.




Rest API
=======

This API helps to perform Lucas series, Fibonacci series and factorial for a number. 

Usage
-----

### Lucas Series ###

##### API Call #####
```API
http://<hostname>:<port>/lucas/<int:number>
```
##### Parameters #####
number : number is of int data type

##### API Call example #####
```API
http://127.0.0.1:80/lucas/5
```

##### API Response #####
```Result
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/0.11.11 Python/2.7.12
Date: Wed, 09 Nov 2016 02:43:41 GMT

{"lucas": "2, 1, 3, 4, 7"}


```
The output is in json data format






### Fibonacci Series ###

##### API call #####
```API
http://<hostname>:<port>/fibonacci/<int:number>
```
##### Parameters #####
number : number is of int data type

##### API Call example #####
```API
http://127.0.0.1:80/fibonacci/5
```
##### API Response#####
```Result
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 31
Server: Werkzeug/0.11.11 Python/2.7.12
Date: Wed, 09 Nov 2016 02:44:45 GMT

{"fibonacci": "0, 1, 1, 2, 3"}

```
The output is in json data format







### Factorial ###

##### API Call #####
```API
http://<hostname>:<port>/fact/<int:number>
```
##### Parameters #####
number : number is of int data type

##### API call Example #####
```API
http://127.0.0.1:80/fact/5
```
##### API Response#####
```Result
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 19
Server: Werkzeug/0.11.11 Python/2.7.12
Date: Wed, 09 Nov 2016 02:45:40 GMT

{"factorial": 120}

```
The output is in json data format
