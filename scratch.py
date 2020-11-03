
class LetterBox:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.pressed = False

    def mouse_drag(self, surface):  # Not needed but could become useful
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_dx, mouse_dy = pygame.mouse.get_rel()
        if pygame.mouse.get_pressed() == LEFT_PRESS and self.rect.collidepoint(mouse_x, mouse_y) and not self.pressed:
            self.pressed = True
        elif pygame.mouse.get_pressed() == (1, 0, 0) and self.pressed:
            self.rect.x += mouse_dx
            self.rect.y += mouse_dy
            surface.fill((0, 0, 0))
            surface.blit(image, self.rect.topleft)
        elif pygame.mouse.get_pressed() != (1, 0, 0):
            self.pressed = False

    def move_to(self, surface, image, target_pos, speed):
        displacement = int(sqrt((target_pos[1] - self.rect.y)**2 + (target_pos[0] - self.rect.x)**2))
        direction = atan2(target_pos[1] - self.rect.y, target_pos[0] - self.rect.x)

        dx = cos(direction) * speed
        dy = sin(direction) * speed

        if displacement > 0:
            self.rect.x += dx
            self.rect.y += dy
            displacement += speed
        else:
            displacement = 0

        x_new = int(self.rect.x)
        y_new = int(self.rect.y)

        surface.fill(BLACK)
        surface.blit(image, (x_new, y_new))