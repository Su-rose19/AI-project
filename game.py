#saving_the_Cart
import pygame
import random
import sys
pygame.init()

WIDTTH = 800
HEIGHT = 600

Yellow = (255, 255, 0)
Blue = (0, 0, 255)
Background_color = (0, 0, 0)

player_siz = 50
player_pos = [WIDTTH/2,HEIGHT-2*player_siz]

enemy_siz = 50
enemy_pos = [random.randint(0,WIDTTH-enemy_siz),0]

Speed = 10

#player_Rect = (player_pos[0], player_pos[1], player_siz, player_siz)
screen = pygame.display.set_mode((WIDTTH,HEIGHT))

game_over = False
clock = pygame.time.Clock()

def detect_collision(player_pos, enemy_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x >= p_x and e_x < (p_x + player_siz)) or (p_x >= e_x and p_x < (e_x + enemy_siz)):
		if (e_y >= p_y and e_y < (p_y + player_siz)) or (p_y >= e_y and p_y < (e_y + enemy_siz)):
			return True
	return False

while not game_over:

	for event in pygame.event.get():
		#print(event)

		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			x=player_pos[0]
			y=player_pos[1]
			if event.key == pygame.K_LEFT:
				x-=player_siz
			elif event.key == pygame.K_RIGHT:
				x+=player_siz
			
			player_pos = [x,y]
	
	screen.fill(Background_color)
	if enemy_pos[1] >=0 and enemy_pos[1] < HEIGHT:
		enemy_pos[1] += Speed
	else:
		enemy_pos[0] = random.randint(0, WIDTTH-enemy_siz)
		enemy_pos[1] = 0
	
	if detect_collision(player_pos,enemy_pos):
		game_over = True

	pygame.draw.rect(screen, Blue, (enemy_pos[0],enemy_pos[1],enemy_siz,enemy_siz), 0)
	pygame.draw.rect(screen, Yellow, (player_pos[0], player_pos[1], player_siz, player_siz), 0)

	clock.tick(30)
	

	pygame.display.update()
