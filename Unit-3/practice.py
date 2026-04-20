import shapes

def main:
  print("choose")
  print("\n1. area of circle\n2. area of rectangle")

choice = int(input("enter your choice: "))

try:
    if choice == 1:
        radius = float(input("enter radius: "))
        print(f"area of circle is: {shapes.area_circle(radius): .2f}")
    elif choice == 2:
        length = int(input("enter length: "))
        width = int(input("enter width: "))
        print(f"area of rectange is: {shapes.area_rectangle(length,width): .2f}")
    else: 
        print("invalid choice")

except ValueError as e:
    print(f" error: {e}")

if __name__ == "__main__":