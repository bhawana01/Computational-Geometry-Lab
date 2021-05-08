class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def input_point(point):
        return point(
            int(input('Please enter X-Coordinate:')),
            int(input('Please enter Y-Coordinate:')),
        )

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


def compute_area(base_point, first_point, second_point):
    vecA = Point(first_point.x - base_point.x, first_point.y - base_point.y)
    vecB = Point(second_point.x - base_point.x, second_point.y - base_point.y)
    crossAB = vecA.x * vecB.y - vecA.y * vecB.x
    return crossAB


def check_left_turn(base_point, first_point, second_point):
    area = compute_area(base_point, first_point, second_point)
    return True if area > 0 else False


def check_right_turn(base_point, first_point, second_point):
    area = compute_area(base_point, first_point, second_point)
    return True if area < 0.0 else False


def check_colinear(base_point, first_point, second_point):
    area = compute_area(base_point, first_point, second_point)
    return True if area == 0.0 else False


def main():
    print("\n***************************Output*******************************\n")
    print("Enter coordinates of base point (P0)")
    base_point = Point.input_point()
    print("\nEnter coordinates of first point (P1)")
    first_point = Point.input_point()
    print("\nEnter coordinates of second point (P2)")
    second_point = Point.input_point()
    area = compute_area(base_point, first_point, second_point)
    print("\n Area of triangle formed by P0 P1 P2 is", area)
    if area > 0:
        print("\n So the point P2" + str(second_point) + "has left turn with base point P0"+str(base_point)+"and point P1"+str(first_point))
    elif area < 0:
        print("\n So the point P2" + str(second_point) + "has right turn with base point P0"+str(base_point)+"and point P1"+str(first_point))
    else:
        print("\n So the point P2"+str(second_point)+"is collinear with base point P0"+str(base_point)+"and point P1"+str(first_point))

