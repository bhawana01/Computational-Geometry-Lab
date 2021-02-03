from matplotlib import pyplot as plt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:

    def __init__(self, start, end):
        # takes point object as start and end
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.start.__str__()} ---- {self.end.__str__() }"

    def get_points(self):
        return [self.start, self.end]


class Ray:

    def __init__(self, start, passing, end):
        self.start = start
        self.passing = passing
        self.end = end

    def get_points(self):
        return [self.start, self.passing, self.end]

    def __str__(self):
        return f"{self.start.__str__()}----{self.passing.__str__()}"


def plot_graph(points):
    plt.plot([p.x for p in points], [p.y for p in points], marker='o')
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.title('Graph Plot')
    plt.show()


def plot_point():
    p = input('Enter x and y coordinates as x, y :')
    p = p.split(',')
    x = int(p[0])
    y = int(p[1])
    point = Point(x, y)
    plot_graph([point])


def plot_line():
    startp = input('Enter start  point as x, y :')
    endp = input('Enter end point as x, y :')
    startp = startp.split(',')
    endp = endp.split(',')
    x1, y1 = int(startp[0]), int(startp[1])
    x2, y2 = int(endp[0]), int(endp[1])
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    l = Line(p1, p2)
    plot_graph(l.get_points())


def plot_ray():
    startp = input('Enter start  point as x, y :')
    passingp = input('Enter passing  point as x, y :')
    endp = input('Enter end point as x, y :')
    startp = startp.split(',')
    passingp = passingp.split(',')
    endp = endp.split(',')
    x1, y1 = int(startp[0]), int(startp[1])
    x2, y2 = int(passingp[0]), int(passingp[1])
    x3, y3 = int(endp[0]), int(endp[1])
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    r = Ray(p1, p2, p3)
    plot_graph(r.get_points())


def main():
    print('\n\n************************  Plot Point  **********************\n\n')
    plot_point()
    print('\n\n************************  Plot Line  **********************\n\n')
    plot_line()
    print('\n\n************************  Plot Ray  **********************\n\n')
    plot_ray()

