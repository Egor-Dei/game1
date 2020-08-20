import printtext
import parametrs


class Gamer:
    def __init__(self, name, x, y, size, points, color):
        self.name = str(name)
        self.x = x
        self.y = y
        self.size = size
        self.points = str(points)
        self.color = color
        self.width, self.height = printtext.print_text2(self.name, self.x, self.y, self.size, self.color, other=True)
        self.points_x = self.x
        self.points_y = self.y + 0.8 * parametrs.gamer_height
        self.points_width, self.points_height = printtext.print_text2(str(self.points), self.points_x, self.points_y, \
                                                                      1.1 * self.size, self.color, other=True)

    def print(self):
        size = self.size
        parametrs.window.blit(parametrs.image_gamer, (int(self.x - parametrs.gamer_width // 2), \
                                                      int(self.y - parametrs.gamer_height // 2)))
        self.width, self.height = printtext.print_text2(self.name, self.x, self.y, size, self.color, other=True)
        while self.width >= int(0.9 * parametrs.gamer_width):
            size *= 0.9
            self.width, self.height = printtext.print_text2(self.name, self.x, self.y, size, self.color, other=True)
        printtext.print_text2(self.name, self.x, self.y, size, (255, 255, 255))
        self.points_width, self.points_height = printtext.print_text2(str(self.points), self.points_x, self.points_y, \
                             1.1 * self.size, self.color)
