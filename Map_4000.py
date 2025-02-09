import pygame
import sys

# Initialize pygame
pygame.init()

# Load the map image
map_image = pygame.image.load("map_4000.jpg")

# Set screen dimensions based on image size
SCREEN_WIDTH, SCREEN_HEIGHT = map_image.get_size()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fantasy Map Adventure")

# Define locations with clickable areas (x, y, width, height)
locations = {
    "Forests": (200, 200, 100, 100),
    "Forests": (690, 500, 130, 140),
    "Forests": (720, 630, 100, 150),
    "Forests": (710, 610, 100, 100),
    "Forests": (700, 600, 90, 90),
    "river Dons": (300, 100, 110, 110),
    "Io archepelagos": (50, 50, 10, 10)
}

# Define event messages for locations
events = {
    "Forests": "keep going!",
    "Forests": "keep going!!",
    "Forests": "coddiwople around the place!!it's about the journey mostly",
    "Forests": "go!",
    "Forests": "Ancient runes glow under the moonlight!",
    "river Dons": "You struggle against the  winds!",
    "Io archepelagos": "You found a hidden treasure chest!"
}

# Function to check if a point is inside a rectangle
def is_inside(x, y, rect):
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh

# Game loop
running = True
while running:
    screen.blit(map_image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for location, rect in locations.items():
                if is_inside(mx, my, rect):
                    print(events[location])  # Display event message in console

    pygame.display.flip()

pygame.quit()
sys.exit()
