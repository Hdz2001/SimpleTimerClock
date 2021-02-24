import pygame
import time
import math

pygame.init()
pygame.display.set_caption('Cheem Timer')

screen = pygame.display.set_mode((500,500))
bg = pygame.image.load('cheem.png')
sound = pygame.mixer.Sound('ding-sound-effect_2.mp3')

BLACK = (0,0,0)
WHITE = (255, 255, 255)
GREY = (128,128,128)
RED = (255, 0, 0)

running = True
total_secs = 0 
total = 0
start = False

font = pygame.font.SysFont('sans', 25) 
text_1 = font.render('+', True, BLACK)
text_2 = font.render('-', True, BLACK)
text_3 = font.render('Start', True, BLACK)
text_4 = font.render('Reset', True, BLACK)
text_5 = font.render('Pause', True, BLACK)

while running: 
	screen.blit(bg, (0,0))

	#create buttons 
	pygame.draw.rect(screen, BLACK, (50,50,50,50),3)
	pygame.draw.rect(screen, BLACK, (150,50,50,50),3)
	pygame.draw.rect(screen, BLACK, (300,50,150,50),3)
	# upper
	pygame.draw.rect(screen, BLACK, (50,150,50,50),3)
	pygame.draw.rect(screen, BLACK, (150,150,50,50),3)
	pygame.draw.rect(screen, BLACK, (300,150,150,50),3)
	# lower 
	pygame.draw.circle(screen, BLACK, (250,325), 75,3)
	# clock 
	pygame.draw.rect(screen, BLACK, (25,425,450,50),3)
	# time line 
	pygame.draw.rect(screen, BLACK, (300,100,150,50),3)

	
	# create signals/words inside buttons 
	screen.blit(text_1,(65,60))
	screen.blit(text_1,(165,60))
	screen.blit(text_2,(65,160))
	screen.blit(text_2,(165,160))
	screen.blit(text_3,(350,60))
	screen.blit(text_4,(350,160))
	screen.blit(text_5,(350,110))
	
	# variables
	mouse_X, mouse_Y = pygame.mouse.get_pos()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		 	running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
		 	if event.button == 1:
		 		if ((50<mouse_X<100) and (50<mouse_Y<100)):
		 			total_secs+=60
		 			total+=60
		 			print("Press +")
		 			print(total_secs)
		 		if ((150<mouse_X<200) and (50<mouse_Y<100)):
		 			total_secs+=1
		 			total+=1
		 		if ((50<mouse_X<100) and (150<mouse_Y<200)):
		 			total_secs-=60
		 			total-=60
		 			print("Press -")
		 			print(total_secs)
		 		if ((150<mouse_X<200) and (150<mouse_Y<200)):
		 			total_secs-=1
		 			total-=1
		 		if (300<mouse_X<450) and (50<mouse_Y<100):
		 			start = True
		 			print("Press Start")
		 		if (300<mouse_X<450) and (100<mouse_Y<150):
		 			start = False
		 			print("Press Pause")
		 		if (300<mouse_X<450) and (150<mouse_Y<200):
		 			total_secs=0 
		 			total = 0
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
	screen.blit(text_time, (105,110))

	x_sec = 250 + 65*math.sin(6*secs*math.pi/180)
	y_sec = 325 -65*math.cos(6*secs*math.pi/180)
	pygame.draw.line(screen, BLACK, (250,325),(x_sec,y_sec),3)

	x_min = 250 + 35*math.sin(6*mins*math.pi/180)
	y_min = 325 -35*math.cos(6*mins*math.pi/180)
	pygame.draw.line(screen, RED, (250,325),(x_min,y_min),3)

	if total!=0:
		pygame.draw.rect(screen, RED, (25,425,int(450*(total_secs/total)), 50))

	pygame.display.flip()


pygame.quit()
