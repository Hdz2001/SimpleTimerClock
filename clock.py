import pygame
import time
import math

pygame.init()
pygame.display.set_caption('Cheem Timer')

width = 750
height = 750
# width and height should be the same 

screen = pygame.display.set_mode((width,height))
bg = pygame.image.load('cheem.png')
bg = pygame.transform.scale(bg, (width, height))
sound = pygame.mixer.Sound('ding-sound-effect_2.mp3')

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREY = (128,128,128)
RED = (255, 0, 0)

running = True
total_secs = 0 
total = 0
start = False

size = int(width/20)
font = pygame.font.Font('CONSOLA.TTF', size) 

text_1 = font.render('+', True, BLACK)
text_rect1 = text_1.get_rect(center=(0.15*width, 0.15*height))
text1_rect1 = text_1.get_rect(center=(0.35*width,0.15*height))

text_2 = font.render('-', True, BLACK)
text_rect2 = text_2.get_rect(center=(0.15*width, 0.35*height))
text2_rect2 = text_2.get_rect(center=(0.35*width,0.35*height))

text_3 = font.render('Start', True, BLACK)
text_rect3 = text_3.get_rect(center=(0.75*width, 0.15*height))
text_4 = font.render('Reset', True, BLACK)
text_rect4 = text_4.get_rect(center=(0.75*width, 0.35*height))
text_5 = font.render('Pause', True, BLACK)
text_rect5 = text_5.get_rect(center=(0.75*width, 0.25*height))

while running: 
	screen.blit(bg, (0,0))
	thickness =3 
	radius = 0.15 * height

	#create buttons 
	pygame.draw.rect(screen, BLACK, (0.1*width,0.1*height,0.1*width,0.1*height),thickness)
	pygame.draw.rect(screen, BLACK, (0.3*width,0.1*height,0.1*width,0.1*height),thickness)
	pygame.draw.rect(screen, BLACK, (0.6*width,0.1*height,0.3*width,0.1*height),thickness)
	# upper
	pygame.draw.rect(screen, BLACK, (0.1*width,0.3*height,0.1*width,0.1*height),thickness)
	pygame.draw.rect(screen, BLACK, (0.3*width,0.3*height,0.1*width,0.1*height),thickness)
	pygame.draw.rect(screen, BLACK, (0.6*width,0.3*height,0.3*width,0.1*height),thickness)
	# lower 
	pygame.draw.circle(screen, BLACK, (0.5*width,0.65*height), radius,thickness)
	# clock 
	pygame.draw.rect(screen, BLACK, (0.05*width,0.85*height,0.9*width,0.1*height),thickness)
	# time line 
	pygame.draw.rect(screen, BLACK, (0.6*width,0.2*height,0.3*width,0.1*height),thickness)

	# create signals/words inside buttons 
	screen.blit(text_1,text_rect1)
	screen.blit(text_1,text1_rect1)
	screen.blit(text_2,text_rect2)
	screen.blit(text_2,text2_rect2)
	screen.blit(text_3,text_rect3)
	screen.blit(text_4,text_rect4)
	screen.blit(text_5,text_rect5)
	
	# variables
	mouse_X, mouse_Y = pygame.mouse.get_pos()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		 	running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
		 	if event.button == 1:
		 		if ((0.1*width<mouse_X<0.2*width) and (0.1*height<mouse_Y<0.2*height)):
		 			total_secs+=60
		 			total+=60
		 			print("Press +")
		 			print(total_secs)
		 		if ((0.3*width<mouse_X<0.4*width) and (0.1*height<mouse_Y<0.2*height)):
		 			total_secs+=1
		 			total+=1
		 		if ((0.1*width<mouse_X<0.2*width) and (0.3*height<mouse_Y<0.4*height)):
		 			total_secs-=60
		 			total-=60
		 			print("Press -")
		 			print(total_secs)
		 		if ((0.3*width<mouse_X<0.4*width) and (0.3*height<mouse_Y<0.4*height)):
		 			total_secs-=1
		 			total-=1
		 		if (0.6*width<mouse_X<0.9*width) and (0.1*height<mouse_Y<0.2*height):
		 			start = True
		 			print("Press Start")
		 		if (0.6*width<mouse_X<0.9*width) and (0.2*height<mouse_Y<0.3*height):
		 			start = False
		 			print("Press Pause")
		 		if (0.6*width<mouse_X<0.9*width) and (0.3*height<mouse_Y<0.4*height):
		 			total_secs=0 
		 			total = 0
		 			start = False
		 			print("Press Reset")


	if start:
		total_secs-=1
		if total_secs == 0:
			start = False
			sound.play()
			time.sleep(1)
			sound.stop()
		time.sleep(1)

	if total_secs < 0:
		total_secs = 0

	mins = int(total_secs/60)
	secs = total_secs - mins*60

	time_now = str(mins)+":"+str(secs)
	text_time = font.render(time_now, True, BLACK)
	texttime_rect = text_time.get_rect(center = (0.25*width,0.25*height))
	screen.blit(text_time, texttime_rect)

	x_sec = 0.5*width + 13/15*radius*math.sin(6*secs*math.pi/180)
	y_sec = 0.65*height -13/15*radius*math.cos(6*secs*math.pi/180)
	pygame.draw.line(screen, BLACK, (0.5*width,0.65*height),(x_sec,y_sec),thickness)

	x_min = 0.5*width + 7/15*radius*math.sin(6*mins*math.pi/180)
	y_min = 0.65*height -7/15*radius*math.cos(6*mins*math.pi/180)
	pygame.draw.line(screen, RED, (0.5*width,0.65*height),(x_min,y_min),thickness)

	if total !=0:
		pygame.draw.rect(screen, RED, (0.05*width,0.85*height,int(0.9*width*(total_secs/total)), 0.1*height))
	
	pygame.display.flip()

pygame.quit()

