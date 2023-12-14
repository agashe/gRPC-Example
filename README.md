# gRPC Example


In this application we implemented simple gRPC in both golang and python. In each we have server/client.

Using the example we can connect the server/client of the same lang to each other , or we could connect different client with different server (e.g golang server to python client).

The necessary packages to run this example can be found in both `go.mod` for golang and `requirements.txt` for python. All what you have to do is to run the installation commands , then run the servers.

The application idea is a CRUD system for students , that use a SQL database to preform all the operations.

## Requirements

* SQLite3 (or any SQL)
* Python3 (with venv installed)
* GOLang (>= 1.21)

## Installation

### Proto Buffer tools

First thing first , you need to make sure that you have the gRPC tools for both golang and python , you can get those easily from the official gRPC site. 

Generating proto source code for golang :

```
# Proto buffer is in the same directory with project

protoc --go_out=. --go-grpc_out=. --go_opt=paths=source_relative --go-grpc_opt=paths=source_relative protos/students.proto

# Proto buffer is outside project's directory

protoc -I ../protos --go_out=./api --go-grpc_out=./api --go_opt=paths=source_relative --go-grpc_opt=paths=sou
rce_relative ../protos/students.proto
```

Generating proto source code for python :

```
# Proto buffer is in the same directory with project

python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/students.proto

# Proto buffer is outside project's directory

python3 -m grpc_tools.protoc -I ../protos --python_out=./api --pyi_out=./api --grpc_python_out=./api ../protos/students.proto
```

### Golang 

To install required dependencies :

```
go mod tidy
```

### Python

First create virtual environment :

```
python3 -m venv .venv
```

Then activate the venv :

```
source .venv/bin/activate
```

Install the dependencies 
```
pip install -r requirements.txt
```

### Database

For simplicity we use sqlite3 database which doesn't require database credentials. 
In both servers golang/python you will find a sqlite3 database file called `data.db`.

To create the database file and the `students` table that we use in both golang/python 
servers run the following commands :

```
# for golang
touch go-grpc/server/data.db
sqlite3 go-grpc/server/data.db < migrations.sql

for python
touch py-grpc/server/data.db
sqlite3 py-grpc/server/data.db < migrations.sql
```

## Running the application


Please note : you will need to run both server/client in to separated terminals !

For golang :

```
# Server 
go run server/main.go

# Client 
go run client/main.go
```

For python :

```
# Server 
python3 server/main.py

# Client 
python3 client/main.py
```