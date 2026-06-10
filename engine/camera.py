class Camera:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def follow(self, target):
        self.x = target.x + target.size // 2 - self.width // 2
        self.y = target.y + target.size // 2 - self.height // 2