"""Contain all necessary instruments for work with image"""

from PIL import Image, ImageDraw


class Picture:
    img = object
    width = int()
    height = int()
    img_ar = []

    def __init__(self, file_name: str):
        self.img = Image.open(file_name).convert("RGB")
        self.width, self.height = self.img.size
        self.convert_img()

    def convert_img(self):
        temporary_array = []
        for h in range(self.height):
            for w in range(self.width):
                temporary_array.append(self.img.getpixel((h, w)))
            self.img_ar.append(temporary_array)
            temporary_array = []

    def show(self):
        self.img.show()

    def color_pixel(self, x: int, y: int, color: list):
        draw = ImageDraw.Draw(self.img)
        draw.point((x, y), fill=color)

    def safe_changes(self):
        self.img.save("1.png")

    def find_start(self):
        for h in range(self.height):
            for w in range(self.width):
                if self.img_ar[h][w] == (0, 255, 0):
                    return h, w

    def find_finish(self):
        for h in range(self.height):
            for w in range(self.width):
                if self.img_ar[h][w] == (255, 0, 0):
                    return h, w
