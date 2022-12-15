from __future__ import print_function

import logging

import grpc
import protos.a3Servicer_pb2 as a3Servicer_pb2
import protos.a3Servicer_pb2_grpc as a3Servicer_pb2_grpc
import protos.a3_pb2 as a3_pb2

def create_book(book):
    res = a3_pb2.Book(ISBN=book['ISBN'], title=book['title'], author=book['author'], genre=book['genre'], publishYear=book['publishYear'])
    return res

def runCreate(book, stub):
    reqbook = create_book(b)
    response = stub.CreateBook(a3Servicer_pb2.CreateBookRequest(book=reqbook))
    print("a3 client received: " + response.message)
    return response

def runGet(ISBN, stub):
    response = stub.GetBook(a3Servicer_pb2.GetBookRequest(ISBN=ISBN))
    if (response.code == 0):
        print(response.message)
    else:
        print(response.book)
    return response


if __name__ == '__main__':
    logging.basicConfig()
    b = {'ISBN':'1982143707','title':'you','author':'me','genre':0,'publishYear':2022}
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = a3Servicer_pb2_grpc.a3ServicerStub(channel)
        # runCreate(book=b, stub=stub)
        runGet(ISBN='1982143707', stub=stub)