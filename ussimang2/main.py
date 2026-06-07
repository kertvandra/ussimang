import turtle, time, random, sqlite3

# SQLite andmebaas
db = sqlite3.connect("score.db")
c = db.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS scores (
    score INTEGER
)
""")
db.commit()

# mänguaken
s = turtle.Screen()
s.setup(400, 400)
s.bgcolor("black")
s.tracer(0)

# ussi pea
h = turtle.Turtle()
h.shape("square")
h.color("green")
h.penup()
h.d = "stop"

# toit
f = turtle.Turtle()
f.shape("circle")
f.color("red")
f.penup()
f.goto(100, 100)

# ussi keha ja punktid
body = []
score = 0

# liikumise funktsioonid
def up():
    h.d = "up"

def down():
    h.d = "down"

def left():
    h.d = "left"

def right():
    h.d = "right"

# klahvid
s.listen()
s.onkey(up, "w")
s.onkey(down, "s")
s.onkey(left, "a")
s.onkey(right, "d")

# mängutsükkel
while True:
    s.update()

    # söögi söömine
    if h.distance(f) < 20:
        f.goto(random.randint(-9, 9) * 20, random.randint(-9, 9) * 20)

        b = turtle.Turtle()
        b.shape("square")
        b.color("lightgreen")
        b.penup()
        body.append(b)

        score += 1

    # keha liikumine
    for i in range(len(body) - 1, 0, -1):
        body[i].goto(body[i - 1].pos())

    if body:
        body[0].goto(h.pos())

    # ussi liikumine
    if h.d == "up":
        h.sety(h.ycor() + 20)
    if h.d == "down":
        h.sety(h.ycor() - 20)
    if h.d == "left":
        h.setx(h.xcor() - 20)
    if h.d == "right":
        h.setx(h.xcor() + 20)

    # mäng lõpeb kui läheb vastu seina
    if abs(h.xcor()) > 190 or abs(h.ycor()) > 190:
        break

    time.sleep(0.15)

# salvestab skoori andmebaasi
c.execute("INSERT INTO scores VALUES (?)", (score,))
db.commit()

print("Skoor:", score)
print("Skoor salvestatud andmebaasi.")

db.close()

turtle.done()