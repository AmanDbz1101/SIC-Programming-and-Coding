import pygame

def draw_board(screen, board, n, cell_size=80):
    """Draws the chessboard and places queens as red circles."""
    screen.fill((255, 255, 255))  # White background
    
    # Colors
    black = (0, 0, 0)
    red = (255, 0, 0)
    
    for row in range(n):
        for col in range(n):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, black, rect, 1)  # Draw grid
            
            if board[row][col] == 1:  # Draw queen as a red circle
                center = (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
                pygame.draw.circle(screen, red, center, cell_size // 3)
    
    pygame.display.flip()

def main(board):
    """Initialize pygame and display the board."""
    pygame.init()
    n = len(board)
    cell_size = 80
    screen_size = n * cell_size
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption("N-Queens Visualization")
    
    draw_board(screen, board, n, cell_size)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()