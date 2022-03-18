import pygame
import time

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)

WIDTH = 500
HEIGHT = 500

font_size = 32

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

initiating_window = pygame.image.load("tic-tac-toe-hand-drawn-game.png")
x_img = pygame.image.load("X_modified.png")
o_img = pygame.image.load("o_modified.png")

x_img = pygame.transform.scale(x_img, (WIDTH // 3, HEIGHT // 3))
o_img = pygame.transform.scale(o_img, (WIDTH // 3, HEIGHT // 3))

icon = pygame.image.load('tic-tac-toe.png')
pygame.display.set_icon(icon)

font = pygame.font.Font('freesansbold.ttf', font_size)

x_score = 0
o_score = 0

text_reset = font.render("press r to play again", True, GREEN, BLUE)
text_reset_rect = text_reset.get_rect()
text_reset_rect.center = (WIDTH // 2, (HEIGHT // 2) - (font_size + 10))

text_stalemate = font.render('Stalemate', True, GREEN, BLUE)
text_stalemate_rect = text_stalemate.get_rect()
text_stalemate_rect.center = (WIDTH // 2, HEIGHT // 2)


turn = 'x'

sqaure_num = 0

square1_val = ''
square2_val = ''
square3_val = ''
square4_val = ''
square5_val = ''
square6_val = ''
square7_val = ''
square8_val = ''
square9_val = ''

def Winner(x_score, o_score, winner):
	pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
	if winner == 'x':
		x_score += 1

	if winner == 'o':
		o_score += 1

	text_x_score = font.render("X's score: " + str(x_score), True, GREEN, BLUE)
	text_o_score = font.render("O's score: " + str(o_score), True, GREEN, BLUE)
	text_x_score_rect = text_x_score.get_rect()
	text_x_score_rect.center = (WIDTH // 2, HEIGHT // 2 + (font_size + 10))
	text_o_score_rect = text_o_score.get_rect()
	text_o_score_rect.center = (WIDTH // 2, HEIGHT // 2 + (font_size + 10) * 2)
	winner_text = font.render(winner.upper() + ' won', True, GREEN, BLUE)
	winner_text_rect = winner_text.get_rect()
	winner_text_rect.center = (WIDTH // 2, HEIGHT // 2)
	screen.blit(winner_text,winner_text_rect)
	screen.blit(text_x_score, text_x_score_rect)
	screen.blit(text_o_score, text_o_score_rect)
	screen.blit(text_reset, text_reset_rect)
	pygame.display.update()

	return x_score, o_score



def draw(x, y):
	global turn
	if turn == 'x':
		screen.blit(x_img, (x, y))
		pygame.display.update()
		turn = 'o'

	elif turn == 'o':
		screen.blit(o_img, (x, y))
		pygame.display.update()
		turn = 'x'

def draw_player(square_num):
	global square1_val
	global square2_val
	global square3_val
	global square4_val
	global square5_val
	global square6_val
	global square7_val
	global square8_val
	global square9_val

	global turn

	if square_num == 1:
		if square1_val == '':
			square1_val = turn
			draw(0, 0)

	elif square_num == 2:
		if square2_val == '':
			square2_val = turn
			draw(WIDTH // 3, 0)

	elif square_num == 3:
		if square3_val == '':
			square3_val = turn
			draw((2 * WIDTH) // 3, 0)

	elif square_num == 4:
		if square4_val == '':
			square4_val = turn
			draw(0, HEIGHT // 3)

	elif square_num == 5:
		if square5_val == '':
			square5_val = turn
			draw(WIDTH // 3, HEIGHT // 3)

	elif square_num == 6:
		if square6_val == '':
			square6_val = turn
			draw((2 * WIDTH) // 3, HEIGHT // 3)

	elif square_num == 7:
		if square7_val == '':
			square7_val = turn
			draw(0, (2 * HEIGHT) // 3)

	elif square_num == 8:
		if square8_val == '':
			square8_val = turn
			draw(WIDTH // 3, (2 * HEIGHT) // 3)

	elif square_num == 9:
		if square9_val == '':
			square9_val = turn
			draw((2 * WIDTH) // 3, (2 * HEIGHT) // 3)

winner = ''

running = True

screen.blit(initiating_window, (0, 0))
pygame.display.update()
time.sleep(3)

screen.fill(BLACK)

pygame.draw.line(screen, WHITE, (0,166), (500,166))
pygame.draw.line(screen, WHITE, (0,332), (500,332))	
pygame.draw.line(screen, WHITE, (166,0), (166,500))	
pygame.draw.line(screen, WHITE, (332, 0), (332, 500))
pygame.display.update()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
				screen.fill(BLACK)
				pygame.display.update()

				turn = 'x'

				square1_val = ''
				square2_val = ''
				square3_val = ''
				square4_val = ''
				square5_val = ''
				square6_val = ''
				square7_val = ''
				square8_val = ''
				square9_val = ''

				winner = ''

				pygame.draw.line(screen, WHITE, (0,166), (500,166))
				pygame.draw.line(screen, WHITE, (0,332), (500,332))	
				pygame.draw.line(screen, WHITE, (166,0), (166,500))	
				pygame.draw.line(screen, WHITE, (332, 0), (332, 500))
				pygame.display.update()

		if square1_val == square2_val == square3_val and winner == '' and square1_val != '':
			winner = square1_val
			pygame.draw.line(screen, WHITE, (3,83),(497,83), 11)
			pygame.display.update()
			x_score, o_score = Winner(x_score, o_score, winner)

		elif square1_val == square4_val == square7_val and winner == '' and square1_val != '':
			winner = square1_val
			pygame.draw.line(screen, WHITE, (83,3),(83,497), 11)
			pygame.display.update()
			x_score, o_score = Winner(x_score, o_score, winner)

		elif square1_val == square5_val == square9_val and winner == '' and square1_val != '':
			winner = square1_val
			pygame.draw.line(screen, WHITE, (3,3),(497,497), 11)
			pygame.display.update()
			x_score, o_score = Winner(x_score, o_score, winner)

		elif square3_val == square5_val == square7_val and winner == '' and square3_val != '':
			winner = square3_val
			pygame.draw.line(screen, WHITE, (497,3),(3,497), 11)
			pygame.display.update()
			x_score, o_score = Winner(x_score, o_score, winner)

		elif square2_val == square5_val == square8_val and winner == '' and square2_val != '':
			winner = square2_val
			pygame.draw.line(screen, WHITE, (249,3),(249,497), 11)
			pygame.display.update()
			x_score, o_score = Winner(x_score, o_score, winner)

		elif square3_val == square6_val == square9_val and winner == '' and square3_val != '':
			winner = square3_val
			pygame.draw.line(screen, WHITE, (415,3),(415,497), 11)
			pygame.display.update()
			x_score, o_score = Winner(x_score, o_score, winner)

		elif square4_val == square5_val == square6_val and winner == '' and square4_val != '':
			winner = square4_val
			pygame.draw.line(screen, WHITE, (3,249),(497,249), 11)
			pygame.display.update()
			x_score, o_score = Winner(x_score, o_score, winner)

		elif square7_val == square8_val == square9_val and winner == '' and square7_val != '':
			winner = square7_val
			pygame.draw.line(screen, WHITE, (3,415),(497,415), 11)
			pygame.display.update()
			x_score, o_score = Winner(x_score, o_score, winner)


		elif square1_val != '' and square2_val != '' and square3_val != '' and square4_val != '' and square5_val != '' and square6_val != '' and square7_val != '' and square8_val != '' and square9_val != '' and not winner:
			screen.blit(text_stalemate,text_stalemate_rect)
			screen.blit(text_reset, text_reset_rect)
			pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)			
			pygame.display.update()

		x, y = pygame.mouse.get_pos()

		if x < WIDTH / 3 and y < HEIGHT / 3:
			if event.type == pygame.MOUSEBUTTONDOWN:
				sqaure_num = 1
				draw_player(sqaure_num)

		elif x < (2 * WIDTH) / 3 and x > WIDTH / 3 and y < HEIGHT / 3:
			if event.type == pygame.MOUSEBUTTONDOWN:
				sqaure_num = 2
				draw_player(sqaure_num)

		elif x < WIDTH and x > (2 * WIDTH) / 3 and y < HEIGHT / 3:
			if event.type == pygame.MOUSEBUTTONDOWN:
				sqaure_num = 3
				draw_player(sqaure_num)

		elif x < WIDTH / 3 and y < (2 * HEIGHT) / 3 and y > HEIGHT / 3:
			if event.type == pygame.MOUSEBUTTONDOWN:
				sqaure_num = 4
				draw_player(sqaure_num)

		elif x < (2 * WIDTH) / 3 and x > WIDTH / 3 and y < (2 * HEIGHT) / 3 and y > HEIGHT / 3:
			if event.type == pygame.MOUSEBUTTONDOWN:
				sqaure_num = 5
				draw_player(sqaure_num)

		elif x < WIDTH and x > (2 * WIDTH) / 3 and y < (2 * HEIGHT) / 3 and y > HEIGHT / 3:
			if event.type == pygame.MOUSEBUTTONDOWN:
				sqaure_num = 6
				draw_player(sqaure_num)

		elif x < WIDTH / 3 and y < HEIGHT and y > (2 * HEIGHT) / 3:
			if event.type == pygame.MOUSEBUTTONDOWN:
				sqaure_num = 7
				draw_player(sqaure_num)

		elif x < (2 * WIDTH) / 3 and x > WIDTH / 3 and y < HEIGHT and y > (2 * HEIGHT) / 3:
			if event.type == pygame.MOUSEBUTTONDOWN:
				sqaure_num = 8
				draw_player(sqaure_num)

		elif x < WIDTH and x > (2 * WIDTH) / 3 and y < HEIGHT and y > (2 * HEIGHT) / 3:
			if event.type == pygame.MOUSEBUTTONDOWN:
				sqaure_num = 9
				draw_player(sqaure_num)



