from turtle import Turtle


with open("data.txt") as file:
    contents = int(file.read())



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = contents
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0,250)
        self.write(f"Scoreboard : {self.score}  High Score : {self.highscore}",False, align="center",font=("Courier",15, "normal"))

    def refresh(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Scoreboard : {self.score}  High Score : {self.highscore}",False, align="center",font=("Verdana",15, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.clear()
        self.write(f"Scoreboard : {self.score}  High Score : {self.highscore}", False, align="center", font=("Verdana", 15, "normal"))

# def lose(self):
   #     self.setposition(0, 0)
   #     self.color("red")
   #     self.write("GAME OVER", False, align="center", font=("Verdana", 20, "normal"))
