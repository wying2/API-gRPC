import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../service"))

import service.a3protos.a3Servicer_pb2 as a3Servicer_pb2
import inventory_client

# create a dict from a book
def create_book(book):
    res = {'ISBN':book.ISBN,'title':book.title,'author':book.author,'genre':book.genre,'publishYear':book.publishYear}
    return res

# taking a list of ISBNs and a client (stub)
# calling GetBook RPC to retrieve corresponding titles
# return them as a list
def runGet(ISBNs, stub):
    res = []
    for ISBN in ISBNs:
        response = stub.GetBook(a3Servicer_pb2.GetBookRequest(ISBN=ISBN))
        if (response.code == 0):
            res.append({})
        else:
            res.append(create_book(response.book))
    return res

if __name__ == '__main__':
    # create an instance of client api object with reasonable defaults
    client = inventory_client.inventory_client()
    # call the defined function using two hardcoded ISBNs as a parameter
    ISBNs = ['1982143707','1938120752']
    books = runGet(ISBNs, client.stub)
    for book in books:
        print(book['title'])