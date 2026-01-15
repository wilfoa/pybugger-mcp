// Simple Rust test fixture for debugging.

fn calculate(a: i32, b: i32) -> i32 {
    let result = a + b;  // Line 4: breakpoint target
    result
}

fn main() {
    let x = 10;
    let y = 20;
    let total = calculate(x, y);  // Line 11: breakpoint target
    println!("Result: {}", total);
}
