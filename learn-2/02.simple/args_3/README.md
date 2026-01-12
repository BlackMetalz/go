### 2 way to run:
Need to be folder learn-02/02.simple/args_3
- `go run ./cmd`
- `go run ./cmd kienlt`

### Init go mod for current directory:
- `go mod init learn-2/args_3`

### Remember for test:
- `go test ./..` : fucking wrong!
- `go test ./...`: correct!

```bash
args_2 % go test ./...
?       learn-2/args_3/cmd      [no test files]
ok      learn-2/args_3/hello    0.370s
```