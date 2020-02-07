class Cylinder():

   # Cylinder.pi = 3.14

    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius


    def volume(self):
        return 3.14 * self.radius ** 2 * self.height

    def surface_area(self):
        return (2 * 3.14 * self.radius) * (self.radius + self.height)

c = Cylinder(2,3)
print(c.surface_area())

