# small network game that has differnt blobs
# moving around the screen

import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from client import Network
import random
import os
pygame.font.init()

# Constants
PLAYER_RADIUS = 20
START_VEL = 9
BALL_RADIUS = 5

W, H = 1600, 830

NAME_FONT = pygame.font.SysFont("comicsans", 20)
TIME_FONT = pygame.font.SysFont("comicsans", 30)
SCORE_FONT = pygame.font.SysFont("comicsans", 26)

COLORS = [(255,0,0), (255, 128, 0), (255,255,0), (128,255,0),(0,255,0),(0,255,128),(0,255,255),(0, 128, 255), (0,0,255), (0,0,255), (128,0,255),(255,0,255), (255,0,128),(128,128,128), (0,0,0)]
PICTURES = ["Images/blue.png", "Images/red.png", "Images/orange.png", "Images/cyan.png"]
# Dynamic Variables
players = {}
balls = []


redImg = pygame.image.load('Images/red.png')  # load red image
cyanImg = pygame.image.load('Images/cyan.png')  # load red image
orangeImg = pygame.image.load('Images/orange.png')  # load red image
blueImg = pygame.image.load('Images/blue.png')  # load blue image
#########################################################################################################################################

class Lobby():

    def __init__(self, w, h, name="None"):
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        self.width = w
        self.height = h
        self.walls = []

    def getLobby(self):
        return self.screen

    def drawLobbyBackground(self):
        #Place background image for lobby
        self.screen.fill((0, 0, 1))
        self.bg_img = pygame.image.load('Images/lobbyShip.png').convert() #653x584
        self.screen.blit(self.bg_img, (375,0), self.bg_img.get_rect())
        #draw walls for lobby
        wall = Wall(365, 0, 10, 584) #left wall
        self.walls.append(wall)
        wall = Wall(1038, 0, 10, 584) #right wall
        self.walls.append(wall)
        wall = Wall(375, 584, 653, 10) #bottom wall
        self.walls.append(wall)
        for wall in self.walls:
            pygame.draw.rect(self.screen, ((0, 0, 1)), wall.rect)
        #myfont = pygame.font.SysFont("monspace", 20)
        #self.screen.blit(self.button, self.button.get_rect())

    def drawLobbyBackground2(self):
        self.bg_img = pygame.image.load('Images/serverEntry.png')
        self.screen.blit(self.bg_img, self.bg_img.get_rect())

    def drawPlayerInputLobby(self):
        self.bg_img = pygame.image.load('Images/homeScreen.png').convert_alpha()
        self.screen.blit(self.bg_img, self.bg_img.get_rect())
        # self.screen.fill((0,0,0))
########################################################################################################################################

class Map():

    def __init__(self, w, h, name="None"):
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        self.width = w
        self.height = h
        self.walls = []


    def getMap(self):
        return self.screen

    #makes window black and then draws the map walls
    def drawMapBackground(self):
        #fills window with black
        #walls holds every wall instance
        self.screen.fill((0, 0, 1))

        #walls at borders of window
        wall = Wall(1356, 0, 10, 768)
        self.walls.append(wall)
        wall = Wall(0, 758, 1366, 10)
        self.walls.append(wall)
        wall = Wall(0, 0, 10, 768)
        self.walls.append(wall)
        wall = Wall(0, 0, 1366, 10)
        self.walls.append(wall)
        #top left room (spawn)
        wall = Wall(0, 192, 80, 10)
        self.walls.append(wall)
        wall = Wall(145, 192, 80, 10)
        self.walls.append(wall)
        wall = Wall(225, 0, 10, 202)
        self.walls.append(wall)
        #top right room
        wall = Wall(960, 160, 406, 10)
        self.walls.append(wall)
        wall = Wall(960, 60, 10, 110)
        self.walls.append(wall)
        #middle room
        wall = Wall(350, 250, 200, 10)
        self.walls.append(wall)
        wall = Wall(620, 250, 390, 10)
        self.walls.append(wall)
        wall = Wall(350, 250, 10, 350)
        self.walls.append(wall)
        wall = Wall(350, 590, 590, 10)
        self.walls.append(wall)
        wall = Wall(1000, 250, 10, 350)
        self.walls.append(wall)
        #bottom right room
        wall = Wall(1100, 590, 140, 10)
        self.walls.append(wall)
        wall = Wall(1310, 590, 56, 10)
        self.walls.append(wall)
        wall = Wall(1100, 590, 10, 178)
        self.walls.append(wall)
        #bottom left room
        wall = Wall(0, 330, 120, 10)
        self.walls.append(wall)
        wall = Wall(110, 330, 10, 348)
        self.walls.append(wall)


        wall = Wall(110, 670, 700, 10)
        self.walls.append(wall)
        wall = Wall(800, 670, 10, 30)

        self.walls.append(wall)

        """
        self.button1 = Button(100, 100, 950, 350, Game.map, "red")  # voting buttons
        self.button2 = Button(100, 100, 950, 400, Game.map, "blue")
        self.button3 = Button(100, 100, 950, 450, Game.map, "cyan")
        self.button4 = Button(100, 100, 950, 500, Game.map, "orange")
        """


        # Voting boxes
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 250, 140, 40])
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 300, 140, 40])
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 350, 140, 40])
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 400, 140, 40])



        for wall in self.walls:
            pygame.draw.rect(self.screen, ((192, 192, 192)), wall.rect)




########################################################################################################################################

# wall class that takes coordinates, width, and height to make rectangle
class Wall(object):
    def __init__(self, x, y, w, h):
        super(Wall, self).__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill((192, 192, 192))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

######################################################################################


















# FUNCTIONS
def convert_time(t):
	"""
	converts a time given in seconds to a time in
	minutes

	:param t: int
	:return: string
	"""
	if type(t) == str:
		return t

	if int(t) < 60:
		return str(t) + "s"
	else:
		minutes = str(t // 60)
		seconds = str(t % 60)

		if int(seconds) < 10:
			seconds = "0" + seconds

		return minutes + ":" + seconds


def redraw_window(players, balls, game_time, score, current_id):
	"""
	draws each frame
	:return: None
	"""
	lobby = Lobby(1700, 850, "Version 1.0")  # Creating
	lobby.drawLobbyBackground()
	#WIN.fill((255,255,255)) # fill screen white, to clear old frames
	'''
	# draw all the orbs/balls
	for ball in balls:
		pygame.draw.circle(WIN, ball[2], (ball[0], ball[1]), BALL_RADIUS)
	'''
	# draw each player in the list
	for player in sorted(players, key=lambda x: players[x]["score"]):
		p = players[player]
		print(current_id) # printing the player info
		# pygame.draw.circle(WIN, p["color"], (p["x"], p["y"] + 30), PLAYER_RADIUS + round(p["score"]))
		# WIN.blit(redImg, (p["x"], p["y"] + 30))
		why = p["y"] + 30
		drawPlayer(p["x"], why, p["pid"])
		# render and draw name for each player
		text = NAME_FONT.render(p["name"], 1, (255,255,255))
		lobby.screen.blit(text, (p["x"] - text.get_width()/2, p["y"] - text.get_height()/2))

	# draw scoreboard
	sort_players = list(reversed(sorted(players, key=lambda x: players[x]["score"])))
	title = TIME_FONT.render("Players", 1, (255,255,255))
	start_y = 25
	x = W - title.get_width() - 10
	lobby.screen.blit(title, (x, 5))

	ran = min(len(players), 8)
	for count, i in enumerate(sort_players[:ran]):
		text = SCORE_FONT.render(str(count+1) + ". " + str(players[i]["name"]), 1, (255,255,255))
		lobby.screen.blit(text, (x, start_y + count * 20))

	# draw time
	text = TIME_FONT.render("Time: " + convert_time(game_time), 1, (255,255,255))
	lobby.screen.blit(text,(10,10))
	# draw score
	# text = TIME_FONT.render("Score: " + str(round(score)),1,(0,0,0))
	# WIN.blit(text,(10,15 + text.get_height()))

def redraw_gameWindow(players, balls, game_time, score, current_id):
	"""
	draws each frame
	:return: None
	"""
	map = Map(1700, 850, "Version 1.0")
	map.drawMapBackground()
	'''
	# draw all the orbs/balls
	for ball in balls:
		pygame.draw.circle(WIN, ball[2], (ball[0], ball[1]), BALL_RADIUS)
	'''
	# draw each player in the list
	for player in sorted(players, key=lambda x: players[x]["score"]):
		p = players[player]
		print(current_id) # printing the player info
		# pygame.draw.circle(WIN, p["color"], (p["x"], p["y"] + 30), PLAYER_RADIUS + round(p["score"]))
		# WIN.blit(redImg, (p["x"], p["y"] + 30))
		why = p["y"] + 30
		drawPlayer(p["x"], why, p["pid"])
		# render and draw name for each player
		text = NAME_FONT.render(p["name"], 1, (255,255,255))
		map.screen.blit(text, (p["x"] - text.get_width()/2, p["y"] - text.get_height()/2))

	# draw scoreboard
	sort_players = list(reversed(sorted(players, key=lambda x: players[x]["score"])))
	title = TIME_FONT.render("Players", 1, (255,255,255))
	start_y = 25
	x = W - title.get_width() - 10
	map.screen.blit(title, (x, 5))

	ran = min(len(players), 8)
	for count, i in enumerate(sort_players[:ran]):
		text = SCORE_FONT.render(str(count+1) + ". " + str(players[i]["name"]), 1, (255,255,255))
		map.screen.blit(text, (x, start_y + count * 20))

	# draw time
	text = TIME_FONT.render("Time: " + convert_time(game_time), 1, (255,255,255))
	map.screen.blit(text,(10,10))
	# draw score
	# text = TIME_FONT.render("Score: " + str(round(score)),1,(0,0,0))
	# WIN.blit(text,(10,15 + text.get_height()))

def drawPlayer(ex, ey, player_id):
	if(player_id == 0):
		WIN.blit(redImg, (ex, ey))
	elif(player_id == 1):
		WIN.blit(cyanImg, (ex, ey))
	elif (player_id == 2):
		WIN.blit(orangeImg, (ex, ey))
	else:
		WIN.blit(blueImg, (ex, ey))
	# pygame.draw.circle(WIN, p["color"], (p["x"], p["y"]), PLAYER_RADIUS + round(p["score"]))

def assignImposter():
	x = random.randint(0,len(players)-1)
	p = players[x]
	p["role"] = "imposter"
	print(p)

def main(name):

	"""
	function for running the game,
	includes the main loop of the game

	:param players: a list of dicts represting a player
	:return: None
	"""
	global players

	# start by connecting to the network
	server = Network()
	current_id = server.connect(name)
	balls, players, game_time = server.send("get")

	# setup the clock, limit to 30fps
	clock = pygame.time.Clock()
	assignImposter()

	started = False
	run = True
	while run:
		clock.tick(30) # 30 fps max
		player = players[current_id]
		#print(players[current_id]) # print player id
		#print(current_id)
		# print(player["x"]) # player x
		# print("draw player")
		#drawPlayer(200,100, player)
		#drawPlayer(player["x"], player["y"])

		if(current_id == 4):
			# WIN.blit("red.png", (player["x"], player["x"]))
			print('')
		vel = START_VEL - round(player["score"]/14)
		if vel <= 1:
			vel = 1

		# get key presses
		keys = pygame.key.get_pressed()

		data = ""
		# movement based on key presses
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			if player["x"] - vel - PLAYER_RADIUS - player["score"] >= 0:
				player["x"] = player["x"] - vel

		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			if player["x"] + vel + PLAYER_RADIUS + player["score"] <= W:
				player["x"] = player["x"] + vel

		if keys[pygame.K_UP] or keys[pygame.K_w]:
			if player["y"] - vel - PLAYER_RADIUS - player["score"] >= 0:
				player["y"] = player["y"] - vel

		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			if player["y"] + vel + PLAYER_RADIUS + player["score"] <= H:
				player["y"] = player["y"] + vel

		data = "move " + str(player["x"]) + " " + str(player["y"])

		# send data to server and recieve back all players information
		balls, players, game_time = server.send(data)

		for event in pygame.event.get():
			# if user hits red x button close window
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				# if user hits a escape key close program
				if event.key == pygame.K_ESCAPE:
					run = False
				# If enter is pressed, lobby will close and game will start
				if event.key == pygame.K_RETURN:
					started = True
					#run = False


		# redraw window then update the frame
		if started:
			redraw_gameWindow(players, balls, game_time, player["score"], current_id)
		else:
			redraw_window(players, balls, game_time, player["score"], current_id)
		pygame.display.update()

		#redraw_gameWindow(players, balls, game_time, player["score"], current_id)


	server.disconnect()
	pygame.quit()
	quit()


# get users name
while True:
 	name = input("Please enter your name: ")
 	if  0 < len(name) < 20:
 		break
 	else:
 		print("Error, this name is not allowed (must be between 1 and 19 characters [inclusive])")

# make window start in top left hand corner
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)

# setup pygame window
WIN = pygame.display.set_mode((W,H))
pygame.display.set_caption("Blobs")

# start game
main(name)
