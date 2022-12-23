import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define food list
food_list = [
    (200, 200),
    (400, 200),
    (300, 300),
    (400, 400)
]

# Define creature class
class Creature:
    def __init__(self, size, speed, color, weight, vision_radius):
        self.size = size
        self.speed = speed
        self.color = color
        self.weight = weight
        self.vision_radius = vision_radius
        self.x = random.randint(0, window_size[0])
        self.y = random.randint(0, window_size[1])

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# Function to calculate distance between two points
def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Function to create creature
def create_creature(parent):
    size = random.gauss(parent.size, 0.1)
    speed = random.gauss(parent.speed, 0.1)
    color = parent.color
    weight = random.gauss(parent.weight, 0.1)
    vision_radius = random.gauss(parent.vision_radius, 0.1)
    return Creature(size, speed, color, weight, vision_radius)

# Function to simulate food competition
def simulate_food_competition(creatures):
    for creature in creatures:
        # check if creature is within vision radius of any food
        food_found = False
        for food in food_list:
            distance = calculate_distance(creature.x, creature.y, food[0], food[1])
            if distance <= creature.vision_radius:
                food_found = True
                break

        if food_found:
            # creature can eat food, so increase its weight
            creature.weight += 1
        else:
            # creature cannot find food, so decrease its weight
            creature.weight -= 1

# Function to simulate death
def simulate_death(creatures):
    for creature in creatures:
        if random.random() < 0.01:  # 1% chance of dying
            creatures.remove(creature)

# Function to simulate reproduction
def simulate_reproduction(creatures):
    for creature in creatures:
        if random.random() < 0.01:  # 1% chance of reproducing
            new_creature = create_creature(creature)
            creatures.append(new_creature)

# Function to move creatures
def move_creatures(creatures):
    for creature in creatures:  
        if int(creature.speed) > 0:
            creature.x += random.randrange(int(-creature.speed), int(creature.speed))
            creature.y += random.randrange(int(-creature.speed), int(creature.speed))

# Function to draw food
def draw_food():
    for food in food_list:
        pygame.draw.circle(screen, YELLOW, food, 5)

# Create initial list of creatures
creatures = [
    Creature(10, 10, RED, 1, 1),
    Creature(10, 10, GREEN, 2, 2),
    Creature(20, 20, BLUE, 3, 1),
]

# Main game loop
while len(creatures) > 1:
    # Generate random positions for the food
    food_list = [(random.randint(0, window_size[0]), random.randint(0, window_size[1])) for _ in range(4)]

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear the screen before drawing
    screen.fill(WHITE)

    # Draw all creatures
    for creature in creatures:
        creature.draw()

    # Draw food
    draw_food()

    # Simulate food competition
    simulate_food_competition(creatures)

    # Simulate reproduction
    simulate_reproduction(creatures)

    # Simulate death
    simulate_death(creatures)

    # Move creatures
    move_creatures(creatures)

    # Update the screen
    pygame.display.flip()

    # Pause for a short time
    pygame.time.delay(100)

# Print the final surviving creature 
print(creatures[0])

# Wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()