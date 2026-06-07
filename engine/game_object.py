class GameObject:
    def __init__(self, x=0, y=0, size=50):
        self.x = x
        self.y = y
        self.size = size

    def get_rect(self):
        return (self.x, self.y, self.size, self.size)

    def update(self, scene):
        pass

    def render(self, screen):
        pass