class Scene:
    def __init__(self, width=800, height=600):
        self.objects = []
        self.width = width
        self.height = height

    def add(self, obj):
        print("ADD:", obj, obj.x, obj.y)
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

    def render(self, screen, camera):
        for obj in self.objects:
            obj.render_with_camera(screen, camera)

    def get_player(self):
        for obj in self.objects:
            if hasattr(obj, "tag") and obj.tag == "player":
                return obj
        return None