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

The `<$int_number>` is the Fibonacci number that you want to calculate

To do the test, you can try:

```

$ make test

```

Enjoy it! :smiley:
