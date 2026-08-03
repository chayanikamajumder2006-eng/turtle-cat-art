import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("#F5F5DC")  # Soft beige / cream background

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1.5)

# Organic turtle color palette
colors = [
    "#2E8B57",  # Sea Green
    "#006400",  # Dark Green
    "#228B22",  # Forest Green
    "#3CB371",  # Medium Sea Green
    "#556B2F",  # Dark Olive Green
    "#6B8E23",  # Olive Drab
]

num_lines = 180

for i in range(num_lines):
    t.penup()
    t.goto(0, -20)  # Center anchor
    
    # Angle calculation
    angle = i * (math.pi * 2) / num_lines
    
    # Parametric feline head outline
    r = 160 + 50 * math.sin(2 * angle)**2 - 40 * math.cos(3 * angle)
    if math.sin(angle) > 0.3 and abs(math.cos(angle)) > 0.4:
        r += 60  # Ear extensions
        
    x_scaled = r * math.cos(angle)
    y_scaled = r * math.sin(angle)
    
    # Cycle through turtle green shades
    c = colors[i % len(colors)]
    t.color(c)
    t.pendown()
    t.goto(x_scaled, y_scaled)
    
    # Accent star tips
    for _ in range(8):
        t.forward(4)
        t.backward(4)
        t.right(45)

turtle.done()
