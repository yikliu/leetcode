package iterate

import (
	"fmt"
)

func main() {
	m := map[string]string{"key1": "val1", "key2": "val2"}
	fmt.Println("Range over keys and values...")
	for k, v := range m {
		fmt.Printf("Key[%s] value[%s]\n", k, v)
	}
	fmt.Println("Range over keys")
	for k := range m {
		fmt.Printf("Key[%s], value[%s]\n", k, m[k])
	}
}
