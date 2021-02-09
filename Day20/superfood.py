
from food import Food
import random


class Super(Food):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.speed("slow")

    def refresh(self):
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 290)
        self.goto(random_x, random_y)
