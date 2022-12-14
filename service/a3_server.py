# server file of a3

from concurrent import futures
import logging
import grpc
import protos.a3_pb2 as a3_pb2
import protos.a3Servicer_pb2 as a3Servicer_pb2
import protos.a3Servicer_pb2_grpc as a3Servicer_pb2_grpc
import json

# helper function to create a new Book defined as the proto file
# from a dictionary
def create_book(book):
    res = a3_pb2.Book(ISBN=book['ISBN'], title=book['title'], author=book['author'], genre=book['genre'], publishYear=book['publishYear'])
    return res

class a3_server(a3Servicer_pb2_grpc.a3Servicer):
    # CreateBook api, write book to db
    # return error code and a corresponding message
    def CreateBook(self, request, context):
        global db
        if request.book.ISBN == '':
            print(request.book)
            return a3Servicer_pb2.CreateBookResponse(code='ERR', message='Must provide ISBN.')
        if request.book.ISBN in db:
            return a3Servicer_pb2.CreateBookResponse(code='ERR',message='ISBN %s already has Book %s.' % (request.book.ISBN, db.get(request.book.ISBN)))
        book = {'ISBN':request.book.ISBN,'title':request.book.title,'author':request.book.author,'genre':request.book.genre,'publishYear':request.book.publishYear}
        db[request.book.ISBN] = book
        with open("service\database.json", 'w+') as f:
            json.dump(db, f)
        return a3Servicer_pb2.CreateBookResponse(code='NOERR',message='ISBN %s Title %s is stored.' % (request.book.ISBN, request.book.title))

    # GetBook api, get book from db
    def GetBook(self, request, context):
        global db
        if request.ISBN in db:
            book = db[request.ISBN]
            resbook = create_book(book)
            return a3Servicer_pb2.GetBookResponse(code='NOERR',book=resbook)
        return a3Servicer_pb2.GetBookResponse(code='ERR',message='ISBN %s is not stored.' % request.ISBN)
        

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    a3Servicer_pb2_grpc.add_a3ServicerServicer_to_server(a3_server(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    with open("service\database.json") as f:
        db = json.load(f)
    serve()