package main

import (
	"context"
	"database/sql"
	"fmt"
	"log"
	"net"

	pb "main/api"

	_ "github.com/mattn/go-sqlite3"
	"google.golang.org/grpc"
)

type Server struct {
	pb.UnimplementedStudentOperationsServer
}

func (s *Server) FetchStudents(ctx context.Context, in *pb.FetchStudentsRequest) (*pb.StudentsResponse, error) {
	sqliteDatabase, _ := sql.Open("sqlite3", "./server/data.db")
	defer sqliteDatabase.Close()

	row, err := sqliteDatabase.Query("SELECT * FROM students")

	if err != nil {
		log.Fatal(err)
	}

	defer row.Close()

	students := []*pb.Student{}

	var id int32
	var name string
	var age int32

	for row.Next() {
		row.Scan(&id, &name, &age)

		students = append(students, &pb.Student{
			Id:   id,
			Name: name,
			Age:  age,
		})
	}

	return &pb.StudentsResponse{
		Status:   true,
		Message:  "Students data were loaded successfully !",
		Students: students,
	}, nil
}

func (s *Server) CreateStudent(ctx context.Context, in *pb.CreateStudentRequest) (*pb.StudentsResponse, error) {
	sqliteDatabase, _ := sql.Open("sqlite3", "./server/data.db")
	defer sqliteDatabase.Close()

	insertStudentStatement := `INSERT INTO students(name, age) VALUES (?, ?)`
	statement, err := sqliteDatabase.Prepare(insertStudentStatement)

	if err != nil {
		log.Fatalln(err.Error())
	}
	_, err = statement.Exec(in.Name, in.Age)

	if err != nil {
		log.Fatalln(err.Error())
	}

	return &pb.StudentsResponse{
		Status:   true,
		Message:  "Student was created successfully !",
		Students: []*pb.Student{},
	}, nil
}

func (s *Server) UpdateStudent(ctx context.Context, in *pb.UpdateStudentRequest) (*pb.StudentsResponse, error) {
	sqliteDatabase, _ := sql.Open("sqlite3", "./server/data.db")
	defer sqliteDatabase.Close()

	updateStudentStatement := `UPDATE students SET name = ?, age = ? WHERE id = ?`
	statement, err := sqliteDatabase.Prepare(updateStudentStatement)

	if err != nil {
		log.Fatalln(err.Error())
	}
	_, err = statement.Exec(in.Name, in.Age, in.Id)

	if err != nil {
		log.Fatalln(err.Error())
	}

	return &pb.StudentsResponse{
		Status:   true,
		Message:  "Student was updated successfully !",
		Students: []*pb.Student{},
	}, nil
}

func (s *Server) DeleteStudent(ctx context.Context, in *pb.DeleteStudentRequest) (*pb.StudentsResponse, error) {
	sqliteDatabase, _ := sql.Open("sqlite3", "./server/data.db")
	defer sqliteDatabase.Close()

	deleteStudentStatement := `DELETE FROM students WHERE id = ?`
	statement, err := sqliteDatabase.Prepare(deleteStudentStatement)

	if err != nil {
		log.Fatalln(err.Error())
	}
	_, err = statement.Exec(in.Id)

	if err != nil {
		log.Fatalln(err.Error())
	}

	return &pb.StudentsResponse{
		Status:   true,
		Message:  "Student was deleted successfully !",
		Students: []*pb.Student{},
	}, nil
}

func main() {
	port := 50051

	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", port))

	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer()
	pb.RegisterStudentOperationsServer(s, &Server{})

	log.Printf("server listening at %v", lis.Addr())

	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
