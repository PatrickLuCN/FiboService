import unittest
from flask import Flask

from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from future.utils import iteritems

app = Flask('calcRestService')

def get_server_url(number):
    url='http://127.0.0.1:5000/calc/api/v1.0/fibo/' + str(number)
    return url

def do_test(number):

    try:
        response = urlopen(get_server_url(number))
        rst2 = response.read()
        #print("rst2: %s" % rst2)
        dictRst = eval(rst2)
        '''
        for (k,v) in iteritems(dictRst):
            print("dictRst[%s]=" % k,v)
        '''
        code = response.code
        number = dictRst["rst"].get('number')
        fiNumber = dictRst["rst"].get('fiNumber')
        return (code, number, fiNumber)

    except HTTPError as e:
        #print(e)
        code = e.code
        return code

class FiboServiceTestCase(unittest.TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUP(self):
        print("Start testing...")

    def tearDown(self):
        print("Test completed!")

    def test_server_is_up_and_running(self):
        response = urlopen(get_server_url(1))
        self.assertEqual(response.code, 200)

    def test_normal_case(self):
        (code, number, fiNumber) = do_test('5')
        #print("test_normal_case: \nResponse code: %s\nnumber: %s\nfiNumber %s" %
        #(code, number, fiNumber))

        self.assertEqual(code, 200)
        self.assertEqual(number, 5)
        self.assertEqual(fiNumber, '0 1 1 2 3')

    def test_negative_case(self):
        (code) = do_test('-1')
        #print("test_negative_case: \nResponse code: %s" % (code))
        self.assertEqual(code, 404)

        # ToDo: verify the content of the HTTP exception


if __name__ == '__main__':
    unittest.main()
