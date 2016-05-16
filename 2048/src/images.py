import pygame


def create_background_image(nrb_of_cell, cell_width, cell_height, cell_color, border_size, border_color):
    image = pygame.Surface((nrb_of_cell*cell_width, nrb_of_cell*cell_height))
    image.fill(border_color)
    pos_x = 0
    pos_y = 0
    fill_cell_width = cell_width - border_size*2
    fill_cell_height = cell_height - border_size*2
    for i in list(range(nrb_of_cell)):
        pos_x = 0
        for j in list(range(nrb_of_cell)):
            pygame.draw.rect(image, cell_color, (pos_x+border_size, pos_y+border_size, fill_cell_width, fill_cell_height))
            pos_x += cell_width
        pos_y += cell_height

    return image


def create_player_image(width, height, color):
    image = pygame.Surface((width, height))
    image = image.convert_alpha()
    image.fill((0, 0, 0, 0))  # make transparent
    pygame.draw.circle(image, color, (int(width/2), int(height/2)), int(width/2))
    return image