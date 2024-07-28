import math

def calculate_triangle_area(a, b, c):
  """Calculates the area of a triangle using Heron's formula."""
  s = (a + b + c) / 2
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  return area

def main():
  """Calculates the total area and contribution of two triangles."""
 
  side1_triangle1 = float(input("Enter side 1 of triangle 1: "))
  side2_triangle1 = float(input("Enter side 2 of triangle 1: "))
  side3_triangle1 = float(input("Enter side 3 of triangle 1: "))

  side1_triangle2 = float(input("Enter side 1 of triangle 2: "))
  side2_triangle2 = float(input("Enter side 2 of triangle 2: "))
  side3_triangle2 = float(input("Enter side 3 of triangle 2: "))


  area1 = calculate_triangle_area(side1_triangle1, side2_triangle1, side3_triangle1)
  area2 = calculate_triangle_area(side1_triangle2, side2_triangle2, side3_triangle2)


  total_area = area1 + area2
  contribution1 = (area1 / total_area) * 100
  contribution2 = (area2 / total_area) * 100

  print("Total area:", total_area)
  print("Contribution of triangle 1:", contribution1, "%")
  print("Contribution of triangle 2:", contribution2, "%")

if __name__ == "__main__":
  main()
