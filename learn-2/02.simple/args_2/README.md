### 2 way to run:
Need to be folder learn-02/02.simple/args_2
- `go run ./cmd`
- `go run ./cmd kienlt`

### Init go mod for current directory:
- `go mod init learn-2/args_2`

### Remember for test:
- `go test ./..` : fucking wrong!
- `go test ./...`: correct!

```bash
args_2 % go test ./...
?       learn-2/args_2/cmd      [no test files]
ok      learn-2/args_2/hello    0.370s
```