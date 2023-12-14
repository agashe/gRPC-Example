import logging
import sys
import os
import grpc
from concurrent import futures
from sqlalchemy import *

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from api import students_pb2
from api import students_pb2_grpc

class StudentService(students_pb2_grpc.StudentOperationsServicer):
    def FetchStudents(self, request, context):
        engine = create_engine("sqlite:///server/data.db")
        db = engine.connect()
        
        result = db.execute(text("select * from students"))

        students = []

        for student in result:
            students.append(students_pb2.Student(id=student.id, name=student.name, age=student.age))

        return students_pb2.StudentsResponse(
            status=False,
            message="Students data were loaded successfully !",
            students=students
        )

    def CreateStudent(self, request, context):
        engine = create_engine("sqlite:///server/data.db")
        db = engine.connect()
        
        students_table = table('students',  column('id'), column('name'), column('age'))

        db.execute(students_table.insert().values({'name': request.name, 'age': request.age}))
        db.commit()
        
        return students_pb2.StudentsResponse(
            status=True,
            message="Student was created successfully !",
            students=[]
        )

    def UpdateStudent(self, request, context):
        engine = create_engine("sqlite:///server/data.db")
        db = engine.connect()
        
        students_table = table('students',  column('id'), column('name'), column('age'))

        db.execute(students_table.update().where(students_table.c.id == request.id)
            .values({'name': request.name, 'age': request.age}))

        db.commit()
        
        return students_pb2.StudentsResponse(
            status=True,
            message="Student was updated successfully !",
            students=[]
        )

    def DeleteStudent(self, request, context):
        engine = create_engine("sqlite:///server/data.db")
        db = engine.connect()
        
        students_table = table('students',  column('id'), column('name'), column('age'))

        db.execute(students_table.delete().where(students_table.c.id == request.id))
            
        db.commit()
        
        return students_pb2.StudentsResponse(
            status=True,
            message="Student was deleted successfully !",
            students=[]
        )

def serve():
    port = "50051"
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    students_pb2_grpc.add_StudentOperationsServicer_to_server(StudentService(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()