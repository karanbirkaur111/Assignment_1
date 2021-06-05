def circle_radius(radius):
    area=(22/7)*radius**2
    print(f"radius of circle is{radius}and area of circle is{str(area)}")
def main():
    radius=float(input("Enter the radius of circle:"))
    circle_radius(radius)
main()
