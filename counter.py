func filterOperationsByKeyword() {
    file, err := os.Open("results.txt")
    if err != nil {
        log.Println("Error opening file:", err)
        return
    }
    defer file.Close()

    var keyword string
    fmt.Print("Enter the keyword to filter operations: ")
    fmt.Scanln(&keyword)

    scanner := bufio.NewScanner(file)
    fmt.Printf("Operations containing the keyword '%s':\n", keyword)

    for scanner.Scan() {
        line := scanner.Text()
        if strings.Contains(line, keyword) {
            fmt.Println(line)
        }
    }

    if err := scanner.Err(); err != nil {
        log.Println("Error reading file:", err)
    }
}
