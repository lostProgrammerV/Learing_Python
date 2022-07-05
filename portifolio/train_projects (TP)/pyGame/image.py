import pygame
font = pygame.font.Font(None, 30)

def debug(info, y = 10, x = 10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'while')
    debug_rect = debug_surf.get_rect(topleft   )









