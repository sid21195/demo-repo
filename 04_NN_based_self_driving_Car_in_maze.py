"""🚀 Full Python Code: Car in Maze + Neural Network Visualization"""

# Goal:

# We want the neural network to take a simple input (such as the car's current position and the goal position) and 
# output a binary decision: move forward (1) or not move forward (0).
# Plan for this simple module:

#     Maze Setup: We'll keep the maze structure simple with a start position and a goal.
#     Inputs: The neural network will use the car's current position and the goal position.
#     Outputs: The neural network will output either 1 (move forward) or 0 (don't move forward).
#     Neural Network: A simple neural network with 2 inputs, 1 hidden layer, and 1 output (binary decision).
#     Pygame Visualization: The car will move forward if the neural network decides to do so, and stop otherwise.

# Step 1: Define a Basic Neural Network

# We’ll create a very simple neural network with the following setup:

#     Inputs: car_x, car_y (normalized between 0 and 1)
#     Output: A binary decision, either 0 (don’t move forward) or 1 (move forward)

# To ensure the car stops at walls and does not go outside of the maze, we need to add a check to 
# verify if the car is moving into a wall before making the move.
# Plan:

#     Wall Check: Before updating the car's position, check if the new position would cause the car to hit a wall.
#     Boundary Check: Ensure the car doesn't move beyond the maze boundaries.


import numpy as np
import pygame
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

# Initialize Pygame
pygame.init()

# Screen Settings
WIDTH, HEIGHT = 600, 600
TILE_SIZE = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚗 Simple Neural Network Car in Maze")

# Colors
WHITE, BLACK, RED, GREEN = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0)

# Maze Setup
maze = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],  # 0 = Path, 1 = Wall
    [1, 0, 1, 0, 0, 1],  # 2 = Goal
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

# Initial Car Position
car_x, car_y = 1 * TILE_SIZE, 1 * TILE_SIZE  # Start position (in the middle of the maze)
goal_x, goal_y = WIDTH - TILE_SIZE * 2, TILE_SIZE
velocity = TILE_SIZE

# Simple Neural Network Model
def create_model():
    model = Sequential([
        Dense(4, input_dim=2, activation="relu"),  # 2 inputs (car_x, car_y)
        Dense(1, activation="sigmoid")  # Output: 1 (move forward) or 0 (do not move)
    ])
    model.compile(loss="binary_crossentropy", optimizer=Adam(learning_rate=0.01))
    return model

model = create_model()

# Dummy Training Data (for demonstration)
X_train = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [1, 3]])
y_train = np.array([1, 0, 0, 1, 1])  # Just for demonstration, adjust as needed
model.fit(X_train, y_train, epochs=100, verbose=0)  # Train model for a few epochs

# Flag for pausing Neural Network (NN)
nn_paused = False

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif maze[row][col] == 0:
                pygame.draw.rect(screen, WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif maze[row][col] == 2:
                pygame.draw.rect(screen, GREEN, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def move_car():
    global car_x, car_y
    state = np.array([car_x / WIDTH, car_y / HEIGHT]).reshape(1, -1)

    # Neural Network Decision: Move forward or not
    move_forward = model.predict(state)[0][0]

    # Make Decision: Move car forward if neural network predicts 1, otherwise stay
    if move_forward > 0.5:
        new_x = car_x + velocity

        # Ensure the new_x and car_y indices are within the maze bounds
        car_row = car_y // TILE_SIZE
        new_x_col = new_x // TILE_SIZE
        
        # Check if new_x is outside the maze or hits a wall (with boundary checks)
        if new_x_col < len(maze[0]) and car_row < len(maze) and maze[car_row][new_x_col] != 1:
            car_x = new_x  # Move the car to the right (forward)

def handle_keypress(event):
    global car_x, car_y, nn_paused
    car_row = car_y // TILE_SIZE
    car_col = car_x // TILE_SIZE

    if event.key == pygame.K_UP:  # Move car up
        if car_y > TILE_SIZE and maze[car_row - 1][car_col] != 1:  # Check if above is not a wall
            car_y -= TILE_SIZE
        nn_paused = True
    elif event.key == pygame.K_DOWN:  # Move car down
        if car_y < HEIGHT - TILE_SIZE and maze[car_row + 1][car_col] != 1:  # Check if below is not a wall
            car_y += TILE_SIZE
        nn_paused = True
    elif event.key == pygame.K_LEFT:  # Move car left
        if car_x > TILE_SIZE and maze[car_row][car_col - 1] != 1:  # Check if left is not a wall
            car_x -= TILE_SIZE
        nn_paused = True
    elif event.key == pygame.K_RIGHT:  # Move car right
        if car_x < WIDTH - TILE_SIZE and maze[car_row][car_col + 1] != 1:  # Check if right is not a wall
            car_x += TILE_SIZE
        nn_paused = True
    elif event.key == pygame.K_SPACE:  # Spacebar to resume NN
        nn_paused = False
        
# --- GAME LOOP ---
running = True
while running:
    screen.fill(WHITE)
    draw_maze()

    # Draw Car
    pygame.draw.rect(screen, RED, (car_x, car_y, TILE_SIZE - 10, TILE_SIZE - 10))

    if not nn_paused:
        move_car()

    # Event Handling for Keypresses (moving the car's initial position)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            handle_keypress(event)

    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()
