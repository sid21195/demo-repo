"""Full Python Code for Car Simulation"""
import time

import pygame

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚗 Forward-Driving Car Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Car Properties
car_x = 50  # Start position
car_y = HEIGHT // 2 - 25  # Centered vertically
car_width = 50
car_height = 30
velocity = 0
acceleration = 0.2  # Increase in speed when moving
friction = 0.05  # Slow down when no input

# Game Loop
running = True
while running:
    screen.fill(WHITE)  # Clear screen
    pygame.draw.rect(screen, RED, (car_x, car_y, car_width, car_height))  # Draw car
    
    keys = pygame.key.get_pressed()
    
    # Control Acceleration
    if keys[pygame.K_RIGHT]:  # Accelerate when right arrow is pressed
        velocity += acceleration
    elif keys[pygame.K_LEFT]:  # Brake when left arrow is pressed
        velocity -= acceleration
    
    # Apply Friction (Car slows down when no input)
    if velocity > 0:
        velocity -= friction
    elif velocity < 0:
        velocity += friction
    
    # Update Car Position
    car_x += velocity
    
    # Keep Car Within Screen Bounds
    if car_x > WIDTH - car_width:
        car_x = WIDTH - car_width
        velocity = 0
    elif car_x < 0:
        car_x = 0
        velocity = 0
    
    # Refresh Screen
    pygame.display.update()
    
    # Event Handling (Quit Simulation)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    time.sleep(0.01)  # Small delay to control update speed

pygame.quit()


# 🔹 How It Works
#     Pygame handles the graphical simulation.
#     The car accelerates forward when the right arrow key is pressed.
#     The car brakes when the left arrow key is pressed.
#     Friction slows the car down when no key is pressed.
#     Boundaries prevent the car from moving off-screen.
