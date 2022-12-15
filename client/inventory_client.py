# an encapsulation of a gRPC client for our API
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "../service"))

import grpc
import service.a3protos.a3Servicer_pb2_grpc as a3Servicer_pb2_grpc

class inventory_client:
    
    # technical details (server address, port number) is provided at class instantiation
    def __init__(self):
        self.url = 'localhost'
        self.port = '50051'
        self.channel = grpc.insecure_channel(self.url + ':' + self.port)
        self.stub = a3Servicer_pb2_grpc.a3ServicerStub(self.channel)