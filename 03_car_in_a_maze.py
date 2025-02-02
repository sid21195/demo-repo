"""🚗 Adding a Car to a Maze in Python (Pygame)"""

# To place a car in a maze, we need to:
# ✅ Create a maze using a grid system.
# ✅ Allow the car to move within the maze.
# ✅ Detect collisions so the car stays within paths.
import time

import pygame

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 600, 600
TILE_SIZE = 50  # Size of each maze tile
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚗 Car in a Maze")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Maze Layout (1 = Wall, 0 = Path)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Car Properties
car_x, car_y = TILE_SIZE, TILE_SIZE  # Start Position
car_width, car_height = TILE_SIZE - 10, TILE_SIZE - 10  # Car Size

# Movement Variables
velocity = TILE_SIZE  # Move one tile at a time

# Game Loop
running = True
while running:
    screen.fill(WHITE)  # Clear screen

    # Draw Maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:  # Draw walls
                pygame.draw.rect(
                    screen, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw Car
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))

    # Get Key Presses
    keys = pygame.key.get_pressed()

    # Move Car with Collision Detection
    new_x, new_y = car_x, car_y
    if keys[pygame.K_UP]:
        new_y -= velocity
    if keys[pygame.K_DOWN]:
        new_y += velocity
    if keys[pygame.K_LEFT]:
        new_x -= velocity
    if keys[pygame.K_RIGHT]:
        new_x += velocity

    # Check if New Position is Inside a Wall
    row, col = new_y // TILE_SIZE, new_x // TILE_SIZE
    if maze[row][col] == 0:  # Only move if the tile is a path (0)
        car_x, car_y = new_x, new_y

    # Refresh Screen
    pygame.display.update()

    # Event Handling (Quit Simulation)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.1)  # Slow down movement for better control

pygame.quit()


# 🛠 Features in This Code

# ✅ Maze Grid System – 1 = Walls, 0 = Path.
# ✅ Collision Detection – Car moves only if the new tile is not a wall.
# ✅ Smooth Movement – Moves tile by tile using arrow keys.

# 📌 Example Output

# 🔳 The maze appears on the screen.
# 🚗 A red car moves through the maze, following open paths.
# 🧱 Walls prevent movement beyond the maze.

# 🌟 Enhancements

# ✅ Add AI (A Algorithm)* to automate car movement.
# ✅ Implement a goal (e.g., "reach the finish line").
# ✅ Add rotational movement (realistic car turns).
