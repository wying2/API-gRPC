# API-gRPC
Implemented a gRPC for createBook and getBook

### notes
/protos is named as /a3protos to avoid conflict

### commands
to generate protos:<br />
python -m grpc_tools.protoc -I./ --python_out=./service --pyi_out=./service --grpc_python_out=./service .\a3protos\a3.proto 

to generate services:<br />
python -m grpc_tools.protoc -I./ --python_out=./service --pyi_out=./service --grpc_python_out=./service .\a3protos\a3Servicer.proto

to run server:<br />
python .\service\a3_server.py

to print titles:<br />
python .\client\get_book_titles.py
