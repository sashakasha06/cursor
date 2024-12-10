import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Курсор')
cursor_image = pygame.image.load('arrow.png')
pygame.mouse.set_visible(False)
draw = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            draw = True
        else:
            draw = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
    screen.fill((0, 0, 0))
    if draw:
        screen.blit(cursor_image, (x, y))
    pygame.display.flip()

pygame.quit()