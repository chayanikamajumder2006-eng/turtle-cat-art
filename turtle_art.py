import turtle
import math

# --- Screen Setup ---
screen = turtle.Screen()
# screen.setup(width=1.0, height=1.0) # Fullscreen (requires manual close)
screen.bgcolor("#0f0f1b")  # Dark midnight blue/black
screen.title("GitHub Turtle Spira-Turtle Art")

# --- Turtle Setup ---
t = turtle.Turtle()
t.speed(0)  # Maximum speed
t.hideturtle()
t.pensize(1)

# --- Define the Color Palette ---
# A vibrant gradient ranging from greens (classic turtle) to blues/purples
colors = [
    "#32CD32",  # LimeGreen
    "#00FA9A",  # MediumSpringGreen
    "#00CED1",  # DarkTurquoise
    "#1E90FF",  # DodgerBlue
    "#8A2BE2",  # BlueViolet
    "#FF00FF"   # Magenta
]

# --- Parameters for the Radial Pattern ---
num_segments = 140      # Total number of radial vectors (loops)
rotation_factor = 7     # Controls the swirl/interlocking geometry
base_radius = 280       # The maximum extension of the design

# --- Drawing Loop ---
for i in range(num_segments):
    t.penup()
    t.goto(0, 0)  # Start from center origin

    # 1. Color Selection (Cycle through the palette smoothly)
    color_index = i % len(colors)
    t.color(colors[color_index])

    # 2. Angle and Geometry Calculation
    # Convert loop index to radians (0 to 2*PI)
    angle_rad = i * (math.pi * 2) / num_segments
    
    # Parametric geometry formula (Rose curve variation)
    # This creates the oscillating 'petals' of turtles
    r = base_radius * math.cos(rotation_factor * angle_rad)
    
    # Convert polar coordinates (r, angle) to Cartesian (x, y)
    x = r * math.cos(angle_rad)
    y = r * math.sin(angle_rad)

    # 3. Draw the Radial Line (The spoke)
    t.pendown()
    # If the radius is positive, it draws outwards; negative draws inward/opposite
    t.goto(x, y)

    # 4. Draw the Terminal Accent Shape
    # (Replacing the 8-pointed star with a 6-pointed star/hexagon accent)
    t.setheading(t.towards(0,0)) # Face back to center before star
    for _ in range(6):
        t.forward(12)
        t.backward(12)
        t.right(60)

# --- Finalize ---
# Keep the window open until clicked
turtle.exitonclick()
