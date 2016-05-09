#!flask/bin/python

from flask import Flask, jsonify
from flask import request
from flask import abort

app = Flask(__name__)

rst = [
    { 
        'number': 1,
        'fiNumber': u'0 '
    },
]

def fib(size):
    a, b = 0, 1
    while size:
        yield a
        a, b = b, a + b
        size -= 1

from flask import make_response
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Invalid number, only positive integer is allowed'}), 404)

@app.route('/calc/api/v1.0/fibo/<int:number>',methods=['GET'])
def gen_fibo(number):

    fiNumList = []

    if number <= 0:
        abort(404)
    if number > 0:
        for x in fib(number):
            fiNumList.append(x)
            fiNumber = ' '.join(map(str, fiNumList)) 
    rst[0]['number'] = number
    rst[0]['fiNumber'] = fiNumber

    return jsonify({'rst': rst[0]})


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    app.run(debug=True)

