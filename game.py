import pygame
from random import randint
pygame.init()
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (147, 153, 35)
PURPLE = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRAPE = (100, 25, 125)
GRASS = (55, 155, 65)
BLACK = (0,0,0)
BP = (249, 244, 230)
BACKGROUND = (214, 214, 214)
WHITE = (255, 255, 255)
x = 0
y = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Game dành cho người buồn")
running = True
swap = 0
img_1 = pygame.image.load('chicken.png')
img1 = pygame.transform.scale(img_1, (100, 100))
img_2 = pygame.image.load("chicken1.png")
img2 = pygame.transform.scale(img_2, (100, 100))
img_3 = pygame.image.load("chicken2.jpg")
img3 = pygame.transform.scale(img_3, (100, 100))
img_dich = pygame.image.load("a.jpg")
imgdich = pygame.transform.scale(img_dich, (100, 100))
font = pygame.font.SysFont("sans", 40)
text_up = font.render("↑", True, WHITE)
text_down = font.render("↓", True, WHITE)
text_left = font.render("←", True, WHITE)
text_right = font.render("→", True, WHITE)
text_swap = font.render("swap charac", True, WHITE)
text_start = font.render("start", True, WHITE)
font1 = pygame.font.SysFont("sans", 20)
text_dat = font1.render("Product of Tien Dat", True, BLACK)
text_result = font.render("Result:", True, BLACK)
text_playing = font.render("Playing", True, BLACK)
text_win = font.render("winning", True, BLACK)
text_con = font.render("You are the winner. Have you ended your sadness yet?", True, BLUE)
img = img1
x_a = 10000
y_a = 10000
moniter = text_playing
is_True = False
while running:
	screen.fill(WHITE)
	clock.tick(60)
	screen.blit(img, (x, y))
	pygame.draw.rect(screen, BLACK, (1000,500, 50, 50))
	screen.blit(text_up, (1010, 500))
	pygame.draw.rect(screen, BLACK, (1000, 570, 50, 50))
	screen.blit(text_down, (1010, 570))
	pygame.draw.rect(screen, BLACK, (920, 535, 50, 50))
	screen.blit(text_left, (930, 535))
	pygame.draw.rect(screen, BLACK, (1080, 535, 50, 50))
	screen.blit(text_right, (1090, 535))
	pygame.draw.rect(screen, BLACK, (920, 400, 210, 50))
	screen.blit(text_swap, (920, 400))
	pygame.draw.rect(screen, BLACK, (920, 300, 210, 50))
	screen.blit(text_start, (980, 300))
	pygame.draw.rect(screen, BLACK, (915, 195, 215, 55))
	pygame.draw.rect(screen, BACKGROUND, (920, 200, 210, 50))
	screen.blit(moniter, (930, 200))
	screen.blit(text_dat, (500, 670))
	screen.blit(text_result, (930, 150))
	mouse_x, mouse_y = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if 1000 < mouse_x < 1050 and 500 < mouse_y < 550:
				if(0 <= x <= 1100 and 0 <= y <= 600):
					y -= 20
					if(y < 0):
						y = 0
			if 1000 < mouse_x < 1050 and 570 < mouse_y < 620:
				if(0 <= x <= 1100 and 0 <= y <= 600):
					y += 20
					if y > 600:
						y = 600
			if 920 < mouse_x < 970 and 535 < mouse_y < 585:
				if(0 <= x <= 1100 and 0 <= y <= 600):
					x -= 20
					if x < 0:
						x = 0
			if 1080 < mouse_x < 1130 and 535 < mouse_y < 585:
				if(0 <= x <= 1100 and 0 <= y <= 600):
					x += 20
					if x > 1100:
						x = 1100
			if 920 < mouse_x < 1130 and 400 < mouse_y < 450:
				swap += 1
				if (swap == 0):
					img = img1
				elif swap == 1:
					img = img2
				elif swap == 2:
					img = img3
				else:
					swap = 0
					img = img1
			if 920 < mouse_x < 1130 and 300 < mouse_y < 350:
				x_a = randint(0,1100)
				y_a = randint(0, 600)
				while x_a == x and y_a == y:
					x_a = randint(0,1100)
					y_a = randint(0, 600)
	while x_a == x and y_a == y:
		x_a = random(0,1100)
		y_a = random(0, 600)
	if(x_a < x + 50 < x_a + 100 and y_a < y + 50 < y_a + 100):
		moniter = text_win
		is_True = True
	if is_True:
		screen.blit(text_con, (200, 350))
	screen.blit(imgdich, (x_a, y_a))
	pygame.display.flip()
pygame.quit()
