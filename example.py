import pygame
from msgbox import MessageBox

pygame.init()
screen = pygame.display.set_mode((750, 500))
clock = pygame.time.Clock()

message = 'The quick brown fox jumps over the lazy dog, but that does not tell us anything about what the cat did \n This starts a new line'
title = 'This is a title'

messageBox = MessageBox(screen, message, title)

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        messageBox.handle_input_event(event)
        if messageBox.should_exit == False: #Prevents any other actions taking place on screen while the messagebox is visible.
            break
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    messageBox.update()
    if messageBox.should_exit == False:
        messageBox.draw(screen)
    pygame.display.flip()

pygame.quit()
