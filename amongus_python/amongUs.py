import sys
import pygame
from client import Client
from pygame import mixer


TIMEOUT = 4  # number of seconds until timeout


#########################################################################################################################################
class Lobby():

    def __init__(self, w, h, name="None"):
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        self.width = w
        self.height = h

    def getLobby(self):
        return self.screen

    def drawLobbyBackground(self):
        #Place background image for lobby
        self.screen.fill((0, 0, 1))
        self.bg_img = pygame.image.load('Images/lobbyShip.png')
        self.screen.blit(self.bg_img, (375,0), self.bg_img.get_rect())
        #myfont = pygame.font.SysFont("monspace", 20)
        #self.screen.blit(self.button, self.button.get_rect())

    def drawLobbyBackground2(self):
        # Place background image for lobby
        self.bg_img = pygame.image.load('Images/starz.png')
        self.screen.blit(self.bg_img, self.bg_img.get_rect())
        # myfont = pygame.font.SysFont("monspace", 20)
        # self.screen.blit(self.button, self.button.get_rect())

########################################################################################################################################


class Map():

    def __init__(self, w, h, name="None"):
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        self.width = w
        self.height = h

    def getMap(self):
        return self.screen

    #makes window black and then draws the map walls
    def drawMapBackground(self):
        #fills window with black
        self.screen.fill((0, 0, 1))
        #walls holds every wall instance
        walls = pygame.sprite.Group()
        #walls at borders of window
        wall = Wall(1356, 0, 10, 768)
        walls.add(wall)
        wall = Wall(0, 758, 1366, 10)
        walls.add(wall)
        wall = Wall(0, 0, 10, 768)
        walls.add(wall)
        wall = Wall(0, 0, 1366, 10)
        walls.add(wall)
        #top left room (spawn)
        wall = Wall(0, 192, 80, 10)
        walls.add(wall)
        wall = Wall(145, 192, 80, 10)
        walls.add(wall)
        wall = Wall(225, 0, 10, 202)
        walls.add(wall)
        #top right room
        wall = Wall(960, 160, 406, 10)
        walls.add(wall)
        wall = Wall(960, 60, 10, 110)
        walls.add(wall)
        #middle room
        wall = Wall(350, 250, 200, 10)
        walls.add(wall)
        wall = Wall(620, 250, 390, 10)
        walls.add(wall)
        wall = Wall(350, 250, 10, 350)
        walls.add(wall)
        wall = Wall(350, 590, 590, 10)
        walls.add(wall)
        wall = Wall(1000, 250, 10, 350)
        walls.add(wall)
        #bottom right room
        wall = Wall(1100, 590, 140, 10)
        walls.add(wall)
        wall = Wall(1310, 590, 56, 10)
        walls.add(wall)
        wall = Wall(1100, 590, 10, 178)
        walls.add(wall)
        #bottom left room
        wall = Wall(0, 330, 120, 10)
        walls.add(wall)
        wall = Wall(110, 330, 10, 348)
        walls.add(wall)
        wall = Wall(110, 670, 700, 10)
        walls.add(wall)
        wall = Wall(800, 670, 10, 30)
        walls.add(wall)

        walls.draw(self.screen)

########################################################################################################################################
# wall class that takes coordinates, width, and height to make rectangle
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super(Wall, self).__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill((192, 192, 192))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

########################################################################################################################################
class Player(pygame.sprite.Sprite):

    def __init__(self, startx, starty, w, h, color, colorDead):
        pygame.sprite.Sprite.__init__(self)
        self.x = startx
        self.y = starty
        self.rate = 2
        self.height = h  # 48pixels
        self.width = w  # 36pixels
        self.screen = pygame.display.set_mode((w, h))
        self.color = color  # color is not a string it is a pygame.Surface type containing the .png file that will produce character
        self.dead = colorDead

        self.images = [pygame.image.load(self.color).convert_alpha(), pygame.image.load(self.dead).convert_alpha()]
        self.current_image = self.images[0]

    # directKey parameter will be used to move player instance in certain direction
    def move(self, directKey):
        if directKey == 0:  # right
            self.x = self.x + self.rate
        elif directKey == 1:  # left
            self.x = self.x - self.rate
        elif directKey == 2:  # up
            self.y = self.y - self.rate
        else:  # down
            self.y = self.y + self.rate

    def draw(self, player):
        self.screen.blit(self.current_image, (self.x, self.y))  # params converted image, starting positions of characters


########################################################################################################################################
class Enemy(pygame.sprite.Sprite):

    def __init__(self, startx, starty, w, h, end, color, colorDead):
        pygame.sprite.Sprite.__init__(self)
        self.x = startx
        self.y = starty
        self.height = h  # 48pixels
        self.width = w  # 36pixels
        self.end = end
        self.path = [self.x, self.end]  # represents where we are starting and where we are ending
        self.walkCount = 0
        self.rate = 2
        self.screen = pygame.display.set_mode((w, h))
        self.color = color  # color is not a string it is a pygame.Surface type containing the .png file that will produce character
        self.dead = colorDead

        self.images = [pygame.image.load(self.color).convert_alpha(), pygame.image.load(self.dead).convert_alpha()]
        self.current_image = self.images[0]

    def moveX(self):
        if self.rate > 0:
            if self.x + self.rate < self.path[1]:
                self.x = self.x + self.rate
            else:
                self.rate = self.rate * -1
                self.walkCount = 0
        else:
            if self.x - self.rate > self.path[0]:
                self.x = self.x + self.rate
            else:
                self.rate = self.rate * -1
                self.walkCount = 0

    def draw(self, g):
        if self.current_image == self.images[0]:
            self.moveX()
        self.screen.blit(self.current_image, (self.x, self.y))  # params converted image, starting positions of characters


##############################################################################################################################

class Button():
    def __init__(self, w, h, x, y, Lobby, text=""):
        self.width = w
        self.height = h
        self.posx = x
        self.posy = y
        self.screen = pygame.display.set_mode((w, h))
        self.Lobby = Lobby
        self.text = text

    def draw(self):
        # rect = pygame.draw.rect(self.screen, (0,200,0), (150, 550, 100, 50))
        # self.screen.blit(rect, (self.posx, self.posy))
        pygame.draw.rect(self.Lobby.getLobby(), (0, 200, 0), (150, 500, 100, 50))

##############################################################################################################################

class Label():
    def __init__(self, xCoord, yCoord, text, fontSize, Lobby):
        self.x = xCoord
        self.y = yCoord
        self.text = text
        self.size = fontSize
        self.lobby = Lobby

        self.colors = [ (255, 255, 255), (0, 0, 0)]
        self.current = self.colors[0]


    def draw(self):
        font = pygame.font.Font(None, self.size)
        label = font.render(self.text, 1, self.current)
        self.lobby.getLobby().blit(label, (self.x, self.y))


##############################################################################################################################


class Game():
    clock = pygame.time.Clock()  # create an object to help track time
    #started will be true if enter is pressed to start the game
    started = False

    def __init__(self, w, h, mapw, maph):
        self.width = w
        self.height = h
        self.mapwidth = mapw
        self.mapheight = maph
        self.network = Client()
        self.player1 = Player(435, 75, 36, 48, 'Images/cyan.png', 'Images/cyanDead.png')  # Initializing Player class instance at set point(40,40) in map
        self.player2 = Player(450, 50, 36, 48, 'Images/orange.png', 'Images/orangeDead.png')  # Initializing Player class instance at set point(300,300) in map
        self.enemy1 = Enemy(435, 150, 36, 48, 495, 'Images/blue.png', 'Images/blueDead.png')  # Initializing Player class instance at set point(100,100)
        self.lobby = Lobby(self.width, self.height, "Version 1.0")  # Creating Lobby class instance
        self.botLabel = Label(1030, 300, "BlueBot in game", 20, self.lobby)
        self.p1Label = Label(1030, 315, "Player1 has joined", 20, self.lobby)
        self.p2Label = Label(1030, 330, "Player2 has joined", 20, self.lobby)

        self.button1 = Button(100, 100, 950, 350, self.lobby, "red") #voting buttons
        self.button2 = Button(100, 100, 950, 400, self.lobby, "blue")
        self.button3 = Button(100, 100, 950, 450, self.lobby, "cyan")
        self.button4 = Button(100, 100, 950, 500, self.lobby, "orange")

    # will get info from server in a form we can understand so we can then draw the other character
    @staticmethod
    def parseData(data):
        try:
            arr = data.split(":")[1].split(",")
            return int(arr[0]), int(arr[1])
        except:
            return -1, -1

    # this is what will send ur current position in certain form to the server
    def sendData(self):
        data = str(self.network.id) + ":" + str(self.player1.x) + "," + str(self.player1.y)
        reply = self.network.sendData(data)
        return reply

    """
    def interrupted(signum, frame):
        # Called when the text input times out
        print("Interrupted")
    signal.signal(signal.SIGALRM, interrupted)
    """

    def run(self):
        running = True
        msg_bool = False  # boolean for if theres a message
        p1_input = 'a'
        p1_bytes = ''
        while running:
            self.clock.tick(60)  # once per frame, the program will never running at more than 60 fps.self.started = True

            # Properly quit (pygame will crash without this)
            for event in pygame.event.get():
                # If closed out, quit program
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    # If key pressed is ESC key, quit program
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # If enter is pressed, lobby will close and game will start
                    if event.key == pygame.K_RETURN:
                        self.started = True
                        running = False

            # making character move
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if self.player1.x <= self.width - self.player1.rate:
                    self.player1.move(0)
            if keys[pygame.K_LEFT]:
                if self.player1.x >= self.player1.rate:
                    self.player1.move(1)
            if keys[pygame.K_UP]:
                if self.player1.y >= self.player1.rate:
                    self.player1.move(2)
            if keys[pygame.K_DOWN]:
                if self.player1.y <= self.height - self.player1.rate:
                    self.player1.move(3)
            """     
            if keys[pygame.K_0]:
                p1_input = input("enter an input :")
                # p1_text = font.render("player 1: " + p1_input, 1, (255, 255, 255)) # player 1 text
                msg_bool = True
                print(msg_bool)
            """
            # Send Network data
            self.player2.x, self.player2.y = self.parseData(self.sendData())

            # Update Lobby
            pygame.init()  # initialize pygame, needed to create fonts, etc.
            self.lobby.drawLobbyBackground()
            self.player1.draw(self.lobby.getLobby())
            self.player2.draw(self.lobby.getLobby())
            self.enemy1.draw(self.lobby.getLobby())
            #Joined labels for each player that state player has entered lobby
            self.botLabel.draw()
            self.p1Label.draw()
            self.p2Label.draw()

            #ENTER LABEL PLACED IN LOBBY TO ENTER GAME#
            #pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load('Images/audio.wav')
            pygame.mixer.music.play(0)
            font = pygame.font.Font(None, 30)
            enterLabel = font.render("Press 'Enter' when all players have joined.", 1, (255, 255, 255))
            self.lobby.getLobby().blit(enterLabel, (495, 457))


            #FADING OUT JOINED LABELS IF NUM KEY 1 PRESSED
            if keys[pygame.K_1]:
                self.botLabel.current = self.botLabel.colors[1]
                self.p1Label.current = self.p1Label.colors[1]
                self.p2Label.current = self.p2Label.colors[1]
                pygame.display.flip()



            #KILLING CHARACTERS#
            #press 2 on keyboard to transform player2 to dead image
            if keys[pygame.K_2]:
                self.player2.current_image = self.player2.images[1]
                pygame.display.flip()
            # press 3 on keyboard to transform 3rd player aka enemy1 to dead image
            if keys[pygame.K_3]:
                self.enemy1.current_image = self.enemy1.images[1]
                pygame.display.flip()

            # CHAT BOX SHIT#
            # signal.alarm(TIMEOUT)
            font = pygame.font.Font(None, 30)
            if keys[pygame.K_0]:
                p1_input = input("enter an input :")
            #else:
                #p1_input = ""
            print(p1_input) # Test, prints current output
            p1_text = font.render("player: " + p1_input, 1, (255, 255, 255)) # player 1 text
            self.lobby.getLobby().blit(p1_text, (15, 20))
            #signal.alarm(0) # Disable alarm after success

            """
            if msg_bool:
                print(msg_bool)
                print("delivered")
                print(p1_input)
                p1_text = font.render("player 1: ", 1, (255, 255, 255))  # player 1 text
                #self.lobby.getLobby().blit(p1_text, (150, 2)) # Display
                p1_bytes = bytes("wow", 'ascii')
                scoretext = font.render(p1_bytes, 1, (255, 255, 255))
                self.lobby.getLobby().blit(scoretext, (150, 457))
                msg_bool = False
                #print(p1_text)
                #print(msg_bool)
            """

            pygame.display.update()

        if not self.started:
            pygame.quit()
        else:
            Game.rungame(self)






    #runs the actual game
    def rungame(self):

        running = True
        #creates the game map
        self.map = Map(self.mapwidth, self.mapheight, "Version 1.0")
        msg_bool = False  # boolean for if theres a message
        p1_input = 'a'
        p1_bytes = ''
        while running:
            self.clock.tick(60)  # once per frame, the program will never running at more than 60 fps.self.started = True

            # Properly quit (pygame will crash without this)
            for event in pygame.event.get():
                # If closed out, quit program
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # If key pressed is ESC key, quit program
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # making character move
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if self.player1.x <= self.width - self.player1.rate:
                    self.player1.move(0)
            if keys[pygame.K_LEFT]:
                if self.player1.x >= self.player1.rate:
                    self.player1.move(1)
            if keys[pygame.K_UP]:
                if self.player1.y >= self.player1.rate:
                    self.player1.move(2)
            if keys[pygame.K_DOWN]:
                if self.player1.y <= self.height - self.player1.rate:
                    self.player1.move(3)
            """     
            if keys[pygame.K_0]:
                p1_input = input("enter an input :")
                # p1_text = font.render("player 1: " + p1_input, 1, (255, 255, 255)) # player 1 text
                msg_bool = True
                print(msg_bool)
            """
            # Send Network data
            self.player2.x, self.player2.y = self.parseData(self.sendData())

            # Update map
            self.map.drawMapBackground()
            self.player1.draw(self.map.getMap())
            self.player2.draw(self.map.getMap())
            self.enemy1.draw(self.map.getMap())

            # ENTER LABEL PLACED IN LOBBY TO ENTER GAME#
            pygame.init()  # initialize pygame
            font = pygame.font.Font(None, 30)
            enterLabel = font.render("", 1, (255, 255, 255))
            self.map.getMap().blit(enterLabel, (500, 457))


            # KILLING CHARACTERS#
            # press 2 on keyboard to transform player2 to dead image
            if keys[pygame.K_2]:
                self.player2.current_image = self.player2.images[1]
                pygame.display.flip()
            # press 3 on keyboard to transform 3rd player aka enemy1 to dead image
            if keys[pygame.K_3]:
                self.enemy1.current_image = self.enemy1.images[1]
                pygame.display.flip()

            # CHAT BOX SHIT#
            # signal.alarm(TIMEOUT)
            if keys[pygame.K_0]:
                p1_input = input("enter an input :")
            # else:
            # p1_input = ""
            print(p1_input)  # Test, prints current output
            p1_text = font.render("player: " + p1_input, 1, (255, 255, 255))  # player 1 text
            self.map.getMap().blit(p1_text, (15, 620))

            # signal.alarm(0) # Disable alarm after success
            # Code for Displaying the mission prompts
            mission = 1
            mision_prompt = 'mission: '
            mission_text = ''
            if (mission == 1):
                print("mission: 1")
                mission_prompt = "Move to your colored circle"
                pygame.draw.circle(self.lobby.getLobby(), (255, 0, 0), (700, 300), 25) # Red circle
                pygame.draw.circle(self.lobby.getLobby(), (0, 0, 255), (700, 400), 25)  # Blue circle
                pygame.draw.circle(self.lobby.getLobby(), (255, 140, 0), (800, 300), 25)  # Orange circle
                pygame.draw.circle(self.lobby.getLobby(), (0, 255, 255), (800, 400), 25)  # cyan circle

            elif (mission == 2):
                print("mission: 2")
                mission_prompt = "Go to the bottom right corner of the screen"
            elif (mission == 3):
                print("mission: 3")
                mission_prompt = "Use the movement keys to do a dance party"
            elif (mission == 4):
                print("mission: 4")
                mission_prompt = "Type your favorite color in the chat"
            elif (mission == 5):
                print("mission: 5")
                mission_prompt = "Type a meaningful number in the cha"
            elif (mission == 6):
                print("mission: 6")
                mission_prompt = "Type your favorite beverage in the chat"
            elif (mission == 7):
                print("mission: 7")
                mission_prompt = "Simon says; go to the corresponding colors when instructed"
            elif (mission == 8):
                print("mission: 8")
                mission_prompt = "Stand in a line"
            else :
                print("mission: 9")
                mission_prompt = "Go to the left of the screen and race to the right of the screen"

            mission_text = font.render(mission_prompt, 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(mission_text, (625, 475))

            vote_text = font.render("vote", 1, (255, 255, 255))  # voting text
            self.map.getMap().blit(vote_text, (800, 200))

            """
            if msg_bool:
                print(msg_bool)
                print("delivered")
                print(p1_input)
                p1_text = font.render("player 1: ", 1, (255, 255, 255))  # player 1 text
                #self.lobby.getLobby().blit(p1_text, (150, 2)) # Display
                p1_bytes = bytes("wow", 'ascii')
                scoretext = font.render(p1_bytes, 1, (255, 255, 255))
                self.lobby.getLobby().blit(scoretext, (150, 457))
                msg_bool = False
                #print(p1_text)
                #print(msg_bool)
            """

            pygame.display.update()

        pygame.quit()




#########################################################################################################################################################################################################################################
