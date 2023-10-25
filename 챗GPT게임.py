import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# Ball
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED

# Paddle
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 20, 120, 10)

# Blocks
block_width = 60
block_height = 20
blocks = []
block_color = (0, 255, 0)  # Block color (Green)
border_color = (255, 255, 255)  # Border color (White)

for row in range(5):
    for col in range(10):
        block = pygame.Rect(col * block_width + 10, row * block_height + 50, block_width, block_height)
        blocks.append(block)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddle
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with blocks
    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # Game over if the ball goes below the paddle
    if ball.bottom > HEIGHT:
        pygame.quit()
        sys.exit()

    # Check for win
    if len(blocks) == 0:
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))  # Background color (Black)

    # Draw everything
    pygame.draw.rect(screen, (0, 0, 255), paddle)  # Paddle color (Blue)
    pygame.draw.ellipse(screen, (255, 0, 0), ball)  # Ball color (Red)
    
    for block in blocks:
        # Draw the border of the block
        pygame.draw.rect(screen, border_color, block, 2)
        # Fill the block with the block color
        pygame.draw.rect(screen, block_color, block)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(30)
