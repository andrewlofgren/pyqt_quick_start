import random

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def constrain(self, lowerLeft, upperRight):

        if self.x < lowerLeft.x:
            self.x = lowerLeft.x
        if self.x > upperRight.x:
            self.x = upperRight.x
        if self.y < lowerLeft.y:
            self.y = lowerLeft.y
        if self.y > upperRight.y:
            self.y = upperRight.y

    def randomize(self, geometry):
        self.x = random.randint(0, geometry.width())
        self.y = random.randint(0, geometry.height())

class Line(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'({self.start.x},{self.start.y}) -> ({self.end.x},{self.end.y})'

class Roamer(object):

    def __init__(self, numberOfLines):
        self.numberOfLines = numberOfLines
        self.lines = []
        point1 = Point(50, 50)
        point2 = Point(100, 100)
        line = Line(point1, point2)
        self.lines.append(line)

    def advance(self):
        if len(self.lines) > self.numberOfLines:
            self.lines.pop(0)
        lastLine = self.lines[-1]
        newLine = Line(Point(lastLine.start.x, lastLine.start.y), Point(lastLine.end.x, lastLine.end.y))
        point = random.choice([newLine.start, newLine.end])
        point.x += random.choice([-10, 10])
        point.y += random.choice([-10, 10])
        self.lines.append(newLine)

    def set_line(self, lines):
        self.numberOfLines = lines



