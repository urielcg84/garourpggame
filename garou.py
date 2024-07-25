import pygame
import sys
import tkinter as tk
import json


# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir tamaño de la pantalla
root = tk.Tk()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()-300
TILE_SIZE = 50

# Configurar la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GAROU The legend")

# Cargar imagen del personaje
character = pygame.image.load("character.png")
character = pygame.transform.scale(character, (TILE_SIZE, TILE_SIZE))
character_rect = character.get_rect()
character_rect.topleft = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Cargar imágenes de tiles
grass_tile = pygame.image.load("grass.png")
grass_tile=pygame.transform.scale(grass_tile, (TILE_SIZE, TILE_SIZE))

wall_tile = pygame.image.load("wall.png")
wall_tile=pygame.transform.scale(wall_tile, (TILE_SIZE, TILE_SIZE))

floor_tile = pygame.image.load("floor.png")
floor_tile=pygame.transform.scale(floor_tile, (TILE_SIZE, TILE_SIZE))

# Definir el mapa (0 = grass, 1 = wall)
game_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,2],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,2]
]

# Velocidad del personaje
character_speed = 5

# Función para dibujar el mapa
def draw_map():
    for row in range(len(game_map)):
        for col in range(len(game_map[row])):
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            if game_map[row][col] == 0:
                screen.blit(grass_tile, (x, y))
            elif game_map[row][col] == 1:
                screen.blit(wall_tile, (x, y))
            elif game_map[row][col] == 2:
                screen.blit(floor_tile, (x, y))

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_rect.x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_rect.x += character_speed
    if keys[pygame.K_UP]:
        character_rect.y -= character_speed
    if keys[pygame.K_DOWN]:
        character_rect.y += character_speed

    # Limitar el movimiento del personaje a la pantalla
    if character_rect.left < 0:
        character_rect.left = 0
    if character_rect.right > SCREEN_WIDTH:
        character_rect.right = SCREEN_WIDTH
    if character_rect.top < 0:
        character_rect.top = 0
    if character_rect.bottom > SCREEN_HEIGHT:
        character_rect.bottom = SCREEN_HEIGHT

    # Dibujar el mapa
    draw_map()

    # Dibujar el personaje
    screen.blit(character, character_rect)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    pygame.time.Clock().tick(30)
