#  File: Geometry.py

#  Description: Develops several geometry classes and test their functions.

#  Student Name: Rose Eichelmann

#  Student UT EID: ree585

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 6-21-21

#  Date Last Modified:  6-23-21

import math
import sys

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)


    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__ (self):
        print("({x}, {y}, {z})".format(x = self.x, y = self.y, z = self.z))


    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance (self, other):
        distance = math.sqrt((other.x - self.x) **2 + (other.y - self.y) **2 + (other.z - self.z) **2)
        return distance


    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__ (self, other):
        tol = 1.0e-6
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Sphere (object):
    # constructor with default values
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = (radius)
        self.center = Point(x, y, z)

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
        print("({x}, {y}, {z}, {r})".format(x = self.x, y = self.y, z = self.z, r = self.radius))

    # compute surface area of Sphere
    # returns a floating point number
    def area (self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return surface_area


    # compute volume of a Sphere
    # returns a floating point number
    def volume (self):
        volume = 4 * math.pi * (self.radius ** 3)
        return volune


    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point (self, p):
        return self.center.distance(p) < self.radius


    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, other):
        dist_centers = self.center.distance(other.center)
        return (dist_centers + other.radius) < self.radius

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly 
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        pass

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl (self, a_cyl):
        pass

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere (self, other):
        dist_centers = self.center.distance(other.center)
        return (not self.is_inside_sphere(other)) and (not((dist_centers - other.radius) > self.radius))


    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, a_cube):
        pass

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):
        pass

class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0, y = 0, z = 0, side = 1):
        self.x = x
        self.y = y
        self.z = z
        self.center = Point(x, y, z)
        self.side = side

    # string representation of a Cube of the form: 
    # Center: (x, y, z), Side: value
    def __str__ (self):
        print("({x}, {y}, {z}, {s})".format(x = self.x, y = self.y, z = self.z, s = self.side))

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self):
        surface_area = (self.side ** 2) * 6
        return surface_area

    # compute volume of a Cube
    # returns a floating point number
    def volume (self):
        volume = (self.side ** 3)
        return volume

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, p):
        pass

    # determine if a Sphere is strictly inside this Cube 
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        pass

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        pass

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        pass

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, other):
        pass

    # determine the volume of intersection if this Cube 
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        pass

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):
        pass


    # return list of 8 corners of cube
    def return_corners(self):
        corner_list = [(self.center - self.side, self.center - self.y, self.center - self.z), 
        (self.center + self.side, self.center - self.side, self.center - self.side), 
        (self.center + self.side, self.center + self.side, self.center - self.side),
        (self.center + self.side, self.center + self.side, self.center + self.side),
        (self.center - self.side, self.center + self.side, self.center + self.side),
        (self.center - self.side, self.center - self.side, self.center + self.side),
        (self.center - self.side, self.center + self.side, self.center - self.side),
        (self.center + self.side, self.center - self.side, self.center + self.side)]
        return corner_list

class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height

    # returns a string representation of a Cylinder of the form: 
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):
        print("({x}, {y}, {z}, {r}, {h})".format(x = self.x, y = self.y, z = self.z, r = self.radius, h = self.height))

    # compute surface area of Cylinder
    # returns a floating point number
    def area (self):
        surface_area = 2 * math.pi * (self.radius ** 2) + 2 * math.pi * self.radius * self.height
        return surface_area

    # compute volume of a Cylinder
    # returns a floating point number
    def volume (self):
        volume = math.pi * self.radius ** 2 * self.height
        return volume

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point (self, p):
        pass
        

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        pass

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        pass

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, other):
        pass

    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder (self, other):
        pass

# return the coordinates of point
def read_point_coordinates(coordinate_line):
    coordinate_line = [coordinate_line[0], coordinate_line[1], coordinate_line[2]]
    x, y, z = [float(coordinate_line[0]), float(coordinate_line[1]), float(coordinate_line[2])]
    return x, y, z

# return the coordinates and radius of sphere
def read_sphere_coordinates(coordinate_line):
    coordinate_line = [coordinate_line[0], coordinate_line[1], coordinate_line[2], coordinate_line[3]]
    x, y, z, radius = [float(coordinate_line[0]), float(coordinate_line[1]), float(coordinate_line[2]), float(coordinate_line[3])]
    return x, y, z, radius

# return the coordinates and side of cube
def read_cube_coordinates(coordinate_line):
    coordinate_line = [coordinate_line[0], coordinate_line[1], coordinate_line[2], coordinate_line[3]]
    x, y, z, side = [float(coordinate_line[0]), float(coordinate_line[1]), float(coordinate_line[2]), float(coordinate_line[3])]
    return x, y, z, side

# return the coordinates, radius, and height of cylinder
def read_cylinder_coordinates(coordinate_line):
    coordinate_line = [coordinate_line[0], coordinate_line[1], coordinate_line[2], coordinate_line[3], coordinate_line[4]]
    x, y, z, radius, height = [float(coordinate_line[0]), float(coordinate_line[1]), float(coordinate_line[2]), float(coordinate_line[3]), float(coordinate_line[4])]
    return x, y, z, radius, height


def main():
    # read data from standard input
    coordinates_file = sys.stdin.readlines()
    # read the coordinates of the first Point p
    coordinates_p = coordinates_file[0].split(" ")
    x, y, z = (read_point_coordinates(coordinates_p))
    # create a Point object 
    Point_P = Point(x, y, z)
    # read the coordinates of the second Point q
    coordinates_q = coordinates_file[1].split(" ")
    x, y, z = read_point_coordinates(coordinates_q)
    # create a Point object 
    Point_Q = Point(x, y, z)
    # read the coordinates of the center and radius of sphereA
    coordinates_sphereA = coordinates_file[2].split(" ")
    x, y, z, radius = read_sphere_coordinates(coordinates_sphereA)
    # create a Sphere object 
    Sphere_A = Sphere(x, y, z, radius)
    # read the coordinates of the center and radius of sphereB
    coordinates_sphereB = coordinates_file[3].split(" ")
    x, y, z, radius = read_sphere_coordinates(coordinates_sphereB)
    # create a Sphere object
    Sphere_B = Sphere(x, y, z, radius)
    # read the coordinates of the center and side of cubeA
    coordinates_cubeA = coordinates_file[4].split(" ")
    x, y, z, side = read_cube_coordinates(coordinates_cubeA)
    # create a Cube object 
    Cube_A = Cube(x, y, z, side)
    # read the coordinates of the center and side of cubeB
    coordinates_cubeB = coordinates_file[5].split(" ")
    x, y, z, side = read_cube_coordinates(coordinates_cubeB)
    # create a Cube object 
    Cube_B = Cube(x, y, z, side)
    # read the coordinates of the center, radius and height of cylA
    coordinates_cylA = coordinates_file[6].split(" ")
    x, y, z, radius, height = read_cylinder_coordinates(coordinates_cylA)
    # create a Cylinder object 
    Cyl_A = Cylinder(x, y, z, radius, height)
    # read the coordinates of the center, radius and height of cylB
    coordinates_cylB = coordinates_file[7].split(" ")
    x, y, z, radius, height = read_cylinder_coordinates(coordinates_cylB)
    # create a Cylinder object
    Cyl_B = Cylinder(x, y, z, radius, height)
    Point_Origin = Point(0, 0, 0)
    orig_dist_p = (Point_P.distance(Point_Origin))
    orig_dist_q = (Point_Q.distance(Point_Origin))
    # print if the distance of p from the origin is greater 
    # than the distance of q from the origin
    print(orig_dist_p > orig_dist_q)
    # print if Point p is inside sphereA
    print(Sphere_A.is_inside_point(Point_P))
    # print if sphereB is inside sphereA
    print(Sphere_A.is_inside_sphere(Sphere_B))
    # print if cubeA is inside sphereA

    # print if cylA is inside sphereA

    # print if sphereA intersects with sphereB

    # print if cubeB intersects with sphereB

    # print if the volume of the largest Cube that is circumscribed 
    # by sphereA is greater than the volume of cylA

    # print if Point p is inside cubeA

    # print if sphereA is inside cubeA

    # print if cubeB is inside cubeA

    # print if cylA is inside cubeA

    # print if cubeA intersects with cubeB

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA

    # print if the surface area of the largest Sphere object inscribed 
    # by cubeA is greater than the surface area of cylA

    # print if Point p is inside cylA

    # print if sphereA is inside cylA

    # print if cubeA is inside cylA

    # print if cylB is inside cylA

    # print if cylB intersects with cylA

if __name__ == "__main__":
    main()
