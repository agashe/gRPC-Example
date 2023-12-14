import logging
import sys
import os
import grpc
import json
from flask import Flask, jsonify, request
from google.protobuf.json_format import MessageToDict

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from api import students_pb2
from api import students_pb2_grpc

app = Flask(__name__)

@app.route("/students", methods=['GET', 'POST', 'PUT', 'DELETE'])
def students():
    if request.method == 'GET':
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = students_pb2_grpc.StudentOperationsStub(channel)
            response = stub.FetchStudents(students_pb2.FetchStudentsRequest(id=0, query="", perPage=0))

        values = MessageToDict(response, including_default_value_fields=True)

        return jsonify(
            status=values['status'],
            message=values['message'],
            students=values['students']
        )

    elif request.method == 'POST':
        data = request.json

        with grpc.insecure_channel("localhost:50051") as channel:
            stub = students_pb2_grpc.StudentOperationsStub(channel)
            response = stub.CreateStudent(students_pb2.CreateStudentRequest(
                name=data['name'], 
                age=data['age']
            ))

        values = MessageToDict(response, including_default_value_fields=True)

        return jsonify(
            status=values['status'],
            message=values['message'],
            students=values['students']
        )

    elif request.method == 'PUT':
        data = request.json

        with grpc.insecure_channel("localhost:50051") as channel:
            stub = students_pb2_grpc.StudentOperationsStub(channel)
            response = stub.UpdateStudent(students_pb2.UpdateStudentRequest(
                id=data['id'], 
                name=data['name'], 
                age=data['age']
            ))

        values = MessageToDict(response, including_default_value_fields=True)

        return jsonify(
            status=values['status'],
            message=values['message'],
            students=values['students']
        )
    elif request.method == 'DELETE':
        data = request.json

        with grpc.insecure_channel("localhost:50051") as channel:
            stub = students_pb2_grpc.StudentOperationsStub(channel)
            response = stub.DeleteStudent(students_pb2.DeleteStudentRequest(
                id=data['id']
            ))

        values = MessageToDict(response, including_default_value_fields=True)

        return jsonify(
            status=values['status'],
            message=values['message'],
            students=values['students']
        )
    else:
        return "The requested URL is not found !", 404
