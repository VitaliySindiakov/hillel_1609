import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])
logger = logging.getLogger("logs")


class Rhombus:
    def __init__(self):
        self.angle_b = None
        self.angle_a = None
        self.side_a = None

    def __str__(self):
        return f"Rhombus:\n[side_a={self.side_a} angle_a={self.angle_a} angle_b={self.angle_b}]"

    def get_angle_a(self):
        return self.angle_a

    def set_angle_a(self, angle_a):
        logger.info(f"set angle_a={angle_a}")
        if self.angle_b is not None:
            logger.error(f"angle_b already defined angle_b={self.angle_b}")
            logger.error(f"Overriding angle_b={180 - angle_a}")
        setattr(self, "angle_a", angle_a)
        setattr(self, "angle_b", 180 - angle_a)

    def get_angle_b(self):
        return self.angle_a

    def set_angle_b(self, angle_b):
        logger.info(f"set angle_b={angle_b}")
        if self.angle_a is not None:
            logger.error(f"angle_a already defined angle_a={self.angle_a}")
            logger.error(f"Overriding with new value angle_a={180 - angle_b}")
        setattr(self, "angle_b", angle_b)
        setattr(self, "angle_a", 180 - angle_b)

    def get_side_a(self):
        return self.side_a

    def set_side_a(self, side):
        if side <= 0:
            logger.error(f"Couldn't set side={side}. Use value > 0")
            return
        logger.info(f"set side_a={side}")
        setattr(self, "side_a", side)


rhombus_1 = Rhombus()
rhombus_1.set_side_a(5)
rhombus_1.set_side_a(0)
rhombus_1.set_angle_a(45)
rhombus_1.set_angle_b(60)
print(rhombus_1)
