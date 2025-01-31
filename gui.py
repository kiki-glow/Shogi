import pygame
from game import Game

# Constants
WIDTH, HEIGHT = 720, 800
CELL_SIZE = WIDTH // 9
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

def load_images():
    """Load all piece images into a dictionary."""
    pieces = ['pawn', 'lance', 'knight', 'silver', 'gold', 'king', 'bishop', 'rook']  # English names for pieces
    images = {}
    for piece in pieces:
        for player in [1, -1]:
            key = f"{piece}_{player}"
            images[key] = pygame.image.load(f"assets/{key}.png")
            images[key] = pygame.transform.scale(images[key], (CELL_SIZE - 10, CELL_SIZE - 10))
    return images

def draw_board(screen, board, images):
    """Draw the grid and pieces."""
    for row in range(9):
        for col in range(9):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE if (row + col) % 2 == 0 else BLACK, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

            piece = board.grid[row][col]
            if piece:
                key = f"{piece.name}_{piece.player}"  # Use Kanji names for pieces
                print(f"Drawing piece: {key} at position: ({row}, {col})")  # Debug print statement
                if key in images:
                    screen.blit(images[key], (col * CELL_SIZE + 5, row * CELL_SIZE + 5))

def draw_captured_pieces(screen, captured_pieces, images, player):
    """Draw captured pieces for a player."""
    y_offset = HEIGHT - 80 if player == 1 else 10
    x_offset = 10
    for piece in captured_pieces[player]:
        key = f"{piece.name}_{piece.player}"
        if key in images:
            screen.blit(images[key], (x_offset, y_offset))
            x_offset += CELL_SIZE

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shogi")
    clock = pygame.time.Clock()

    game = Game()
    images = load_images()
    selected = None
    running = True

    print("Starting the game loop...")  # Debug print statement

    while running:
        draw_board(screen, game.board, images)
        draw_captured_pieces(screen, game.board.captured_pieces, images, 1)
        draw_captured_pieces(screen, game.board.captured_pieces, images, -1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE

                if selected:
                    if game.move_piece(selected, (row, col)):
                        selected = None
                    else:
                        piece = game.board.grid[selected[0]][selected[1]]
                        if piece and piece in game.board.captured_pieces[game.current_player]:
                            if game.drop_piece(piece, (row, col)):
                                selected = None
                else:
                    selected = (row, col)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
