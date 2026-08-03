import turtle
import math

# --- Screen Setup ---
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#F5F5DC")  # Cream background
screen.title("Parametric Turtle Cat Art")

# --- Turtle Setup ---
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1.5)

# Natural Turtle Green Palette
colors = [
    "#2E8B57",  # Sea Green
    "#006400",  # Dark Green
    "#228B22",  # Forest Green
    "#3CB371",  # Medium Sea Green
    "#556B2F",  # Dark Olive Green
    "#6B8E23",  # Olive Drab
]

# --- Drawing Loop ---
num_lines = 180

for i in range(num_lines):
    t.penup()
    t.goto(0, -20)  # Center origin
    
    angle = i * (math.pi * 2) / num_lines
    
    # Parametric Cat Outline
    r = 160 + 50 * math.sin(2 * angle)**2 - 40 * math.cos(3 * angle)
    if math.sin(angle) > 0.3 and abs(math.cos(angle)) > 0.4:
        r += 60  # Pointy ears
        
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    
    # Apply color and draw line
    t.color(colors[i % len(colors)])
    t.pendown()
    t.goto(x, y)
    
    # Accent star points at perimeter
    for _ in range(8):
        t.forward(4)
        t.backward(4)
        t.right(45)

# Keep canvas active
turtle.done()
