import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../service"))
from unittest.mock import MagicMock
from service.a3_server import a3_server
import service.a3protos.a3_pb2 as a3_pb2
import service.a3protos.a3Servicer_pb2 as a3Servicer_pb2
from inventory_client import inventory_client
import get_book_titles

mockClient = inventory_client()
resBook = a3_pb2.Book(ISBN='1982143707', title='esse occaecat adipisicing', author='minim Duis', genre=1, publishYear=2022)
response = a3Servicer_pb2.GetBookResponse(code=1,book=resBook)
mockClient.GetBook = MagicMock(return_value=response)

client = inventory_client()
ISBNs = ['1982143707']
books = get_book_titles.runGet(ISBNs, client.stub)
mockServer.GetBook.assert_called()

