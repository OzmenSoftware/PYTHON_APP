import turtle

# Ekran Oluşturma
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("lightblue")  # Arka plan rengi
sc.setup(width=1000, height=600)

# Paddle Oluşturma Fonksiyonu
def create_paddle(x_pos, y_pos, color):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(color)  # Paddle rengi
    paddle.shapesize(stretch_wid=6, stretch_len=2)
    paddle.penup()
    paddle.goto(x_pos, y_pos)
    return paddle

# Sol ve Sağ Paddle
sol_pad = create_paddle(-400, 0, "darkred")  # Sol paddle rengi
sag_pad = create_paddle(400, 0, "darkgreen")  # Sağ paddle rengi

# Top
top = turtle.Turtle()
top.speed(40)
top.shape("circle")
top.color("purple")  # Top rengi
top.penup()
top.goto(0, 0)
top.dx = 5
top.dy = -5

# Oyuncuların Skorları
sol_oyuncu = 0
sag_oyuncu = 0

# Skor Tablosu
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("navy")  # Skor tablosu rengi
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)

def update_score():
    sketch.clear()
    sketch.write(f"Birinci Oyuncu : {sol_oyuncu}  İkinci Oyuncu : {sag_oyuncu}",
                 align="center", font=("Comic Sans MS", 24, "bold"))  # Yazı tipi değiştirildi

update_score()

# Hareket Fonksiyonları
def paddle_up(paddle):
    y = paddle.ycor()
    if y < 250:  # Ekran sınırında kalması için
        paddle.sety(y + 20)

def paddle_down(paddle):
    y = paddle.ycor()
    if y > -240:  # Ekran sınırında kalması için
        paddle.sety(y - 20)

# Klavye Atamaları
sc.listen()
sc.onkeypress(lambda: paddle_up(sol_pad), "w")  # W tuşunu atadık
sc.onkeypress(lambda: paddle_down(sol_pad), "s")  # S tuşunu atadık
sc.onkeypress(lambda: paddle_up(sag_pad), "Up")
sc.onkeypress(lambda: paddle_down(sag_pad), "Down")

# Topun hızını artırma fonksiyonu
def increase_speed():
    top.dx *= 1.05
    top.dy *= 1.05

# Oyun Döngüsü
while True:
    sc.update()

    # Top Hareketi
    top.setx(top.xcor() + top.dx)
    top.sety(top.ycor() + top.dy)

    # Duvarlara Çarpma Kontrolü
    if top.ycor() > 280:
        top.sety(280)
        top.dy *= -1
        increase_speed()  # Hız artırma

    if top.ycor() < -280:
        top.sety(-280)
        top.dy *= -1
        increase_speed()  # Hız artırma

    # Skor Güncelleme ve Reset
    if top.xcor() > 500:
        top.goto(0, 0)
        top.dx = 5  # Hızı sıfırlıyoruz
        top.dy = -5
        sol_oyuncu += 1
        update_score()

    if top.xcor() < -500:
        top.goto(0, 0)
        top.dx = 5  # Hızı sıfırlıyoruz
        top.dy = -5
        sag_oyuncu += 1
        update_score()

    # Paddle Çarpışma Kontrolü
    if (380 < top.xcor() < 400) and (sag_pad.ycor() - 60 < top.ycor() < sag_pad.ycor() + 60):
        top.setx(380)
        top.dx *= -1
        increase_speed()  # Hız artırma

    if (-400 < top.xcor() < -380) and (sol_pad.ycor() - 60 < top.ycor() < sol_pad.ycor() + 60):
        top.setx(-380)
        top.dx *= -1
        increase_speed()  # Hız artırma
