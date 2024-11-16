func findMostFrequentWord() {
    inputFile, err := os.Open("results.txt")
    if err != nil {
        log.Println("Error opening file:", err)
        return
    }
    defer inputFile.Close()

    wordCounts := make(map[string]int)
    scanner := bufio.NewScanner(inputFile)

    for scanner.Scan() {
        line := scanner.Text()
        words := strings.Fields(line)
        for _, word := range words {
            wordCounts[word]++
        }
    }

    if err := scanner.Err(); err != nil {
        log.Println("Error reading file:", err)
    }

    mostFrequentWord := ""
    highestCount := 0

    for word, count := range wordCounts {
        if count > highestCount {
            mostFrequentWord = word
            highestCount = count
        }
    }

    if mostFrequentWord != "" {
        fmt.Printf("The most frequent word is '%s', appearing %d times.\n", mostFrequentWord, highestCount)
    } else {
        fmt.Println("No words found in the file.")
    }
}
