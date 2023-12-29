import pygame

def create_rect(width, height, border, color, border_color):
    surf = pygame.Surface((width+border*2, height+border*2), pygame.SRCALPHA)
    pygame.draw.rect(surf, color, (border, border, width, height), 0)
    for i in range(1, border):
        pygame.draw.rect(surf, border_color, (border-i, border-i, width+5, height+5), 1)
    return surf
