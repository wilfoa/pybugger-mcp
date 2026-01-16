/**
 * Simple JavaScript test fixture for debugging.
 */

function calculate(a, b) {
    const result = a + b;  // Line 6: breakpoint target
    return result;
}

function main() {
    const x = 10;
    const y = 20;
    const total = calculate(x, y);  // Line 13: breakpoint target
    console.log(`Result: ${total}`);
}

main();
