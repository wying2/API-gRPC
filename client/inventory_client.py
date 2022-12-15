# an encapsulation of a gRPC client for our API
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../service"))

import grpc
import service.a3protos.a3Servicer_pb2_grpc as a3Servicer_pb2_grpc
import service.a3protos.a3Servicer_pb2 as a3Servicer_pb2
import service.a3protos.a3_pb2 as a3_pb2

def create_book(book):
    res = a3_pb2.Book(ISBN=book['ISBN'], title=book['title'], author=book['author'], genre=book['genre'], publishYear=book['publishYear'])
    return res

class inventory_client:
    # hide server api from user
    def runCreate(self, book):
        reqbook = create_book(book)
        response = self.stub.CreateBook(a3Servicer_pb2.CreateBookRequest(book=reqbook))
        return response

    # hide server api from user
    def runGet(self, ISBN):
        response = self.stub.GetBook(a3Servicer_pb2.GetBookRequest(ISBN=ISBN))
        return response

    # technical details (server address, port number) is provided at class instantiation
    def __init__(self):
        self.url = 'localhost'
        self.port = '50051'
        self.channel = grpc.insecure_channel(self.url + ':' + self.port)
        self.stub = a3Servicer_pb2_grpc.a3ServicerStub(self.channel)