import math


def calculate_area(radius):
    area = math.pi * radius**2
    return area


def main():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius < 0:
                raise ValueError("Radius must be a positive number.")
            break
        except ValueError as e:
            print(e)
    area = calculate_area(radius)
    print(f"The area of the circle is {area}.")


if __name__ == "__main__":
    main()
