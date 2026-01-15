// Simple Go test fixture for debugging.
package main

import "fmt"

func calculate(a, b int) int {
	result := a + b // Line 7: breakpoint target
	return result
}

func main() {
	x := 10
	y := 20
	total := calculate(x, y) // Line 14: breakpoint target
	fmt.Printf("Result: %d\n", total)
}
