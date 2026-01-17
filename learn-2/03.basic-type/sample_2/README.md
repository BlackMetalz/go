This is literal fun for me. Fscanln() function can read from file or stdin

Example:
```bash
go run main.go < nums.txt
```

Output:
```
Hello World + os /Users/kienlt/data/github.com/go/learn-2/03.basic-type/sample_2
The avg:  2
```

Same result:
```bash
kienlt@Luongs-MacBook-Pro sample_2 % cat nums.txt|go run .
Hello World + os /Users/kienlt/data/github.com/go/learn-2/03.basic-type/sample_2
The avg:  2
```

So program will read from stdin or where it came from.