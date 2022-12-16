import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../service"))
from unittest.mock import MagicMock
from service.a3_server import a3_server
import service.a3protos.a3_pb2 as a3_pb2
import service.a3protos.a3Servicer_pb2 as a3Servicer_pb2
import client.inventory_client as inventory_client
import client.get_book_titles as get_book_titles

import unittest   # The test framework

class test_TestGetBook(unittest.TestCase):
    # test with mock client
    def testMockClient(self):
        # create mock client object
        mockClient = inventory_client.inventory_client()
        # define mock return
        resBook = a3_pb2.Book(ISBN='1982143707', title='esse occaecat adipisicing', author='minim Duis', genre=1, publishYear=2022)
        response = a3Servicer_pb2.GetBookResponse(code=1,book=resBook)
        mockClient.runGet = MagicMock(return_value=response)
        # call with mock client
        ISBNs = ['1982143707','0']
        books = get_book_titles.runGet(ISBNs, mockClient)
        for ISBN in ISBNs:
            mockClient.runGet.assert_any_call(ISBN)

    # test with real server and client
    def testRealClient(self):
        # create client object
        Client = inventory_client.inventory_client()
        # define expected return
        resBook = ['you',None,'Turning the Pyramid Upside Down']
        # call with real client
        ISBNs = ['1982143709','0','1938120752']
        books = get_book_titles.runGet(ISBNs, Client)
        self.assertEqual(resBook, books, 'test passed')
        

if __name__ == '__main__':
    unittest.main()


