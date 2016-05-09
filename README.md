# FiboService


Overview
========

FiboService is a micro service for fibonacci numbers calculation.


Features
========

* The web service accepts a number, n, as input and returns the fi numbers, starting from 0. i.e. given n = 5, appropriate output would represent the sequence "0 1 1 2 3".
* Given a negative number, it will respond with an appropriate error.


Requirements
============

* Python 2.7
* Python Flask library is required
* Works on Linux, Windows, Mac OSX and (quite possibly) BSD.


Install/Deploy
===============


The quick way is use the provided `make` file.

 
```
$ make install
```

Starting and Stopping Services:

==============================

To launch the service:

```
$ make launch
```

To stop the service:

```
$ make shutdown
```

Test and run
=============

To calculate the fibonacci number via the RESTful micro-service, you can refer to below steps:

1. Start the Micro Service
2. Access below URL to do the calculation:

```
http://127.0.0.1:5000/calc/api/v1.0/fibo/<$int_number>
```

The `<$int_number>` is the Fibonacci number that you want to calculate.

e.g:

```
ubuntu:~/FiboService$ curl -i http://localhost:5000/calc/api/v1.0/fibo/2
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 57
Server: Werkzeug/0.11.9 Python/2.7.11+
Date: Mon, 09 May 2016 09:41:09 GMT

{
  "rst": {
    "fiNumber": "0 1",
    "number": 2
  }
}
```

To run integration test, you can try below method.

```
$ make test
```

Enjoy it! :smiley:
