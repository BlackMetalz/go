package hello

import (
	"strings"
)

func Say(names []string) string {
	if len(names) == 0 {
		names = []string{"Default without args"}
	}

	return "Hello, " + strings.Join(names, ", ") + "!"
}
