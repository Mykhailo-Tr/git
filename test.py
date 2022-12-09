import turtle

t = turtle.Pen()

class Coords:
    def __init__(self, x :int, y :int) -> int:
        self.x = x
        self.y = y

    def GoToMain(self):
        t.goto(self.x, self.y)

    def GoTo(self, x1 :int, y1 :int):
        t.goto(x1, y1)

usr = Coords(20, 20)

def main():
    usr.GoToMain()
    usr.GoTo(50, 70)
    input()

if __name__ == "__main__":
    main()