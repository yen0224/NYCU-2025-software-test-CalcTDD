from Calc import Calculator


def main():
    """Interactive calculator using the Calculator class"""
    print("Hello from hw2!")
    print("Interactive Calculator")
    print("=" * 50)

    calc = Calculator()

    # Demo of calculator functionality
    print("\nCalculator Demo:")
    print(f"  2 + 3 = {calc.add(2, 3)}")
    print(f"  5 - 3 = {calc.subtract(5, 3)}")
    print(f"  4 * 3 = {calc.multiply(4, 3)}")
    print(f"  10 / 2 = {calc.divide(10, 2)}")
    print(f"  7 / 2 = {calc.divide(7, 2)}")

    print("\nAll operations completed successfully!")


if __name__ == "__main__":
    main()
