class Scene:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def check_collision(self, obj, dx=0, dy=0):
        px = obj.x + dx
        py = obj.y + dy
        ps = obj.size

        for other in self.objects:
            if other == obj:
                continue

            ox = other.x
            oy = other.y
            os = other.size

            if (
                    px < ox + os and
                    px + ps > ox and
                    py < oy + os and
                    py + ps > oy
            ):
                return True

        return False

    def update(self):
        for obj in self.objects:
            obj.update(self)

    def render(self, screen):
        for obj in self.objects:
            obj.render(screen)

    def get_player(self):
        for obj in self.objects:
            if hasattr(obj, "tag") and obj.tag == "player":
                return obj
        return None