import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])
logger = logging.getLogger("logs")


class Rhombus:
    def __init__(self):
        self.__angle_a = None
        self.__angle_b = None
        self.__side_a = None

    def __setattr__(self, name, value):
        if value is not None:
            if value <= 0:
                logger.error("Value should be > 0")
                return
        super().__setattr__(name, value)

    def __str__(self):
        return f"Rhombus:\n[side_a={self.__side_a} angle_a={self.__angle_a} angle_b={self.__angle_b}]"

    @property
    def side_a(self):
        return self.__side_a

    @side_a.setter
    def side_a(self, value):
        self.__side_a = value

    @property
    def angle_a(self):
        return self.__angle_a

    @angle_a.setter
    def angle_a(self, value):
        self.__angle_a = value
        self.__angle_b = 180 - value

    @property
    def angle_b(self):
        return self.__angle_b

    @angle_b.setter
    def angle_b(self, value):
        self.__angle_b = value
        self.__angle_a = 180 - value


rhombus_1 = Rhombus()
rhombus_1.angle_a = 45
print(rhombus_1)
rhombus_1.angle_b = 63
rhombus_1.side_a = 5
print(rhombus_1)

rhombus_1.side_a = 0
rhombus_1.angle_a = 0
rhombus_1.angle_b = 0
print(rhombus_1)
