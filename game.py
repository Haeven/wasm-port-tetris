import pygame
from elements.entity import Tetris
from lib.enums import BLUE, WHITE, colors
from lib.utils import create_rect

def start():
    pygame.init()
    size = (600, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tetris in Python")

    done = False
    clock = pygame.time.Clock()
    fps = 30
    game = Tetris(20, 18)
    counter = 0
    pressing_down = False

    while not done:
        if game.shape is None:
            game.new_shape()

        counter += 1
        if counter > 100000:
            counter = 0

        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "play":
                game.go_down()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            else:
                pressing_down = handle_input(event, game, pressing_down)

        screen.fill(WHITE)
        screen.blit(create_rect(360, 400, 5, BLUE, (0, 0, 0)), (95, 55))
        font_m = pygame.font.SysFont('Arial', 25, True, False)
        font_xl = pygame.font.SysFont('Arial', 65, True, False)
        font_s = pygame.font.SysFont('Arial', 20, True, False)
        font_xs = pygame.font.SysFont('Arial', 23, True, False)
        font_l = pygame.font.SysFont('Arial', 50, True, False)
        score_text = font_m.render("Score: " + str(game.score), True, BLUE)
        controls_text = font_xs.render("Controls:", True, BLUE)
        instruction_text1 = font_s.render("Move ←→", True, BLUE)
        instruction_text2 = font_s.render("Rotate ↑", True, BLUE)
        sig_text = font_m.render("x.com/hvndevs", True, BLUE)
        text_game_over = font_xl.render("Game Over", True, (193, 5, 5))
        text_game_over1 = font_l.render("Press ESC", True, (0, 5, 5))

        screen.blit(score_text, [95, 30])
        screen.blit(controls_text, [470, 35])
        screen.blit(instruction_text1, [475, 60])
        screen.blit(instruction_text2, [475, 85])
        screen.blit(sig_text, [5, 470])
        pygame.display.flip()
        if game.state == "complete":
            screen.blit(text_game_over, [105, 200])
            screen.blit(text_game_over1, [145, 265])

        
        draw_grid_and_blocks(screen, game)
        draw_current_shape(screen, game)

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()

def draw_grid_and_blocks(screen, game):
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, BLUE, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1, 0, 2)
            if game.grid[i][j] > 0:
                pygame.draw.rect(screen, colors[game.grid[i][j]],
                                [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1], 0, 2)

def draw_current_shape(screen, game):
    if game.shape is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.shape.block():
                    pygame.draw.rect(screen, colors[game.shape.color],
                                    [game.x + game.zoom * (j + game.shape.x) + 1,
                                    game.y + game.zoom * (i + game.shape.y) + 1,
                                    game.zoom - 2, game.zoom - 2], 0, 2)

def handle_input(event, game, pressing_down):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            game.rotate()
        elif event.key == pygame.K_DOWN:
            pressing_down = True
        elif event.key in (pygame.K_LEFT, pygame.K_RIGHT):
            game.go_side(1 if event.key == pygame.K_RIGHT else -1)
        elif event.key == pygame.K_SPACE:
            game.go_space()
        elif event.key == pygame.K_ESCAPE:
            game.__init__(20, 10)
    elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
        pressing_down = False

    return pressing_down