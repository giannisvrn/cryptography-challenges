package main

import (
	"bufio"
	"fmt"
	"net"
	"strings"
)

func main() {
	// Connect to the server
	host := "195.134.67.7"
	port := "10090"
	conn, err := net.Dial("tcp", host+":"+port)
	if err != nil {
		fmt.Println("Error connecting to server:", err)
		return
	}
	defer conn.Close()

	reader := bufio.NewReader(conn)
	writer := bufio.NewWriter(conn)

	// Print welcome messages
	welcome1, _ := reader.ReadString('\n')
	welcome2, _ := reader.ReadString('\n')
	welcome3, _ := reader.ReadString('\n')
	fmt.Println(welcome1, "\n", welcome2, "\n", welcome3, "\n")

	for i := 0; i < 10; i++ {
		// Define the plaintexts
		t0 := strings.Repeat("A", 16)
		t1 := strings.Repeat("B", 16)
		t2 := strings.Repeat("C", 16)

		// Encrypt t0 and t1
		cmd := fmt.Sprintf("encrypt(%s,%s)\n", t0, t1)
		writer.WriteString(cmd)
		writer.Flush()

		ct, _ := reader.ReadString('\n')
		parts := strings.Split(strings.TrimSpace(ct), ": ")

		var ct0 string
		if i == 0 {
			ct0 = strings.TrimSpace(parts[2])
		} else {
			fmt.Println(parts[0])
			ct0 = strings.TrimSpace(parts[3])
		}
		fmt.Println("cipher:", ct0)

		// Encrypt t0 and t2
		cmd = fmt.Sprintf("encrypt(%s,%s)\n", t0, t2)
		writer.WriteString(cmd)
		writer.Flush()

		ct, _ = reader.ReadString('\n')
		parts = strings.Split(strings.TrimSpace(ct), ": ")
		
		ct1 := strings.TrimSpace(parts[2])
		fmt.Println("cipher:", ct1)

		// Compare ciphertexts and solve
		var solveCmd string
		if ct0 == ct1 {
			solveCmd = "solve(0)\n"
		} else {
			solveCmd = "solve(1)\n"
		}
		fmt.Println("solve_cmd", solveCmd)
		writer.WriteString(solveCmd)
		writer.Flush()
	}

	// Read the flag
	flag, _ := reader.ReadString('\n')
	fmt.Println(flag)
}

