import random
import copy

class Point(object):

    speeds = [-20, -15, -10, -5, 5, 10, 15, 20]

    def __init__(self, x=0, y=0, xVelocity=None, yVelocity=None):
        self.x = x
        self.y = y
        self.lowerLeftBound = None
        self.upperRightBound = None
        if xVelocity == None:
            xVelocity = random.choice(Point.speeds)
        if yVelocity == None:
            yVelocity = random.choice(Point.speeds)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self, lowerLeftBound, upperRightBound):
        self.lowerLeftBound = lowerLeftBound
        self.upperRightBound = upperRightBound
        self.x += self.xVelocity
        self.y += self.yVelocity
        self.constrain()

    def constrain(self):
        #
        # Hit the left wall.
        #
        if self.x < self.lowerLeftBound.x:
            self.x = self.lowerLeftBound.x
            self.xVelocity = -self.xVelocity
        #
        # Hit the right wall.
        #
        if self.x > self.upperRightBound.x:
            self.x = self.upperRightBound.x
            self.xVelocity = -self.xVelocity
        #
        # Hit the bottom.
        #
        if self.y > (self.lowerLeftBound.y - 44):
            self.y = self.lowerLeftBound.y - 44
            self.yVelocity = -self.yVelocity
        #
        # Hit the top.
        #
        if self.y < (self.upperRightBound.y - 44):
            self.y = self.upperRightBound.y - 44
            self.yVelocity = -self.yVelocity

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

    def advance(self, lowerLeftBound, upperRightBound):
        if len(self.lines) > self.numberOfLines:
            self.lines.pop(0)
        lastLine = self.lines[-1]
        #newLine = Line(Point(lastLine.start.x, lastLine.start.y), Point(lastLine.end.x, lastLine.end.y))
        newLine = copy.deepcopy(lastLine)
        newLine.start.move(lowerLeftBound, upperRightBound)
        newLine.end.move(lowerLeftBound, upperRightBound)
        self.lines.append(newLine)

    def set_line(self, lines):
        self.numberOfLines = lines



