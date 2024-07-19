import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

# Create the Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beautiful Gradient Design")

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the beautiful gradient design with circles, rectangles, and squares
    for y in range(HEIGHT):
        color = (
            int(255 * (y / HEIGHT)),                    # Red component
            int(255 * (1 - abs((y - HEIGHT/2) / HEIGHT))),  # Green component
            int(255 * ((HEIGHT - y) / HEIGHT))           # Blue component
        )

        # Draw circles
        pygame.draw.circle(screen, color, (WIDTH // 4, y), y // 10)
        pygame.draw.circle(screen, color, (WIDTH // 2, y), y // 10)
        pygame.draw.circle(screen, color, (3 * WIDTH // 4, y), y // 10)

        # Draw rectangles
        pygame.draw.rect(screen, color, (WIDTH // 4 - y // 2, y, y, y))
        pygame.draw.rect(screen, color, (WIDTH // 2 - y // 2, y, y, y))
        pygame.draw.rect(screen, color, (3 * WIDTH // 4 - y // 2, y, y, y))

        # Draw squares
        pygame.draw.rect(screen, color, (WIDTH // 4 - y // 2, HEIGHT // 2 + y, y, y))
        pygame.draw.rect(screen, color, (WIDTH // 2 - y // 2, HEIGHT // 2 + y, y, y))
        pygame.draw.rect(screen, color, (3 * WIDTH // 5 - y // 8, HEIGHT // 3 + y, y, y))

    # Update the display
    pygame.display.flip()
display.stop()