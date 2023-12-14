package main

import (
	"context"
	"log"
	pb "main/api"
	"time"

	"github.com/gin-gonic/gin"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	address := "localhost:50051"
	app := gin.Default()
	conn, err := grpc.Dial(address, grpc.WithTransportCredentials(insecure.NewCredentials()))

	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}

	defer conn.Close()

	c := pb.NewStudentOperationsClient(conn)

	app.GET("/students", func(con *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), time.Second)
		defer cancel()

		r, err := c.FetchStudents(ctx, &pb.FetchStudentsRequest{Id: 0, Query: "", PerPage: 0})

		if err != nil {
			log.Fatalf("could not fetch: %v", err)
		}

		con.JSON(200, gin.H{
			"status":   r.GetStatus(),
			"message":  r.GetMessage(),
			"students": r.GetStudents(),
		})
	})

	app.POST("/students", func(con *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), time.Second)
		defer cancel()

		var insertRequestBody pb.CreateStudentRequest

		if err := con.BindJSON(&insertRequestBody); err != nil {
			log.Fatalf("did not connect: %v", err)
		}

		r, err := c.CreateStudent(ctx, &insertRequestBody)

		if err != nil {
			log.Fatalf("could not fetch: %v", err)
		}

		con.JSON(200, gin.H{
			"status":   r.GetStatus(),
			"message":  r.GetMessage(),
			"students": r.GetStudents(),
		})
	})

	app.PUT("/students", func(con *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), time.Second)
		defer cancel()

		var updateRequestBody pb.UpdateStudentRequest

		if err := con.BindJSON(&updateRequestBody); err != nil {
			log.Fatalf("did not connect: %v", err)
		}

		r, err := c.UpdateStudent(ctx, &updateRequestBody)

		if err != nil {
			log.Fatalf("could not fetch: %v", err)
		}

		con.JSON(200, gin.H{
			"status":   r.GetStatus(),
			"message":  r.GetMessage(),
			"students": r.GetStudents(),
		})
	})

	app.DELETE("/students", func(con *gin.Context) {
		ctx, cancel := context.WithTimeout(context.Background(), time.Second)
		defer cancel()

		var deleteRequestBody pb.DeleteStudentRequest

		if err := con.BindJSON(&deleteRequestBody); err != nil {
			log.Fatalf("did not connect: %v", err)
		}

		r, err := c.DeleteStudent(ctx, &deleteRequestBody)

		if err != nil {
			log.Fatalf("could not fetch: %v", err)
		}

		con.JSON(200, gin.H{
			"status":   r.GetStatus(),
			"message":  r.GetMessage(),
			"students": r.GetStudents(),
		})
	})

	app.Run(":5050")
}
