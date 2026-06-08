class Camera:
    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

    def follow(self, target):
        # центрируем камеру на игроке
        self.x = target.x - self.width // 2
        self.y = target.y - self.height // 2