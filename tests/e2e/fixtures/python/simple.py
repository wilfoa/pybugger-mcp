"""Simple Python test fixture for debugging."""


def calculate(a: int, b: int) -> int:
    """Add two numbers."""
    result = a + b  # Line 6: breakpoint target
    return result


def main() -> None:
    """Main entry point."""
    x = 10
    y = 20
    total = calculate(x, y)  # Line 14: breakpoint target
    print(f"Result: {total}")


if __name__ == "__main__":
    main()
