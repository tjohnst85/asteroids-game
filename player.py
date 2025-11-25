import pygame
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOT_COOLDOWN_SECONDS
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0
    
    def rotateplayer(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
           self.rotateplayer(dt) 
        if keys[pygame.K_d]:
           self.rotateplayer(-dt) 
        if keys[pygame.K_w]:
           self.moveplayer(dt) 
        if keys[pygame.K_s]:
           self.moveplayer(-dt)   
        if keys[pygame.K_SPACE]:
            self.shoot() 
        
        self.shot_cooldown -= dt

    def moveplayer(self, dt):    
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def shoot(self):
        if self.shot_cooldown > 0:
            pass
        else:
            self.shot_cooldown = PLAYER_SHOT_COOLDOWN_SECONDS
            shot_vector = Shot(self.position.x, self.position.y, SHOT_RADIUS )
            shot_vector.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        


        
