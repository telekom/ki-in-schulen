#
# Calliope Rennspiel mit Künstlicher Intelligenz
# ----------------------------------------------
# Modul: IQ-TEst
# Lizenz: siehe LICENSE.TXT
#
# Funktion:
# Führt einen "IQ-Test" für ein mit Scikit-Learn oder Orange trainiertes künstliches neuronales Netzwerk durch.
# Es werden 50 Episoden gespielt und der Medianwert der erreichten Punktzahl berechnet.
#
# Nutzung:
#
# 	python ki-rennspiel.py <Backend-Option> <Modell-Datei>
#
#   <Backend-Option>: 'sklearn' für Scikit-Learn oder 'orange3' für Orange3
#	<Modell-Datei>  : Name der Datei des trainierten ML-Modells\n
#



# notwendige Bibliotheken importieren
import random
import os
import pickle
import numpy as np
import sys
import inspect
try:
    import pygame as pg
    from pygame.locals import *
except:
    # ohne PyGame läuft gar nichts.
    raise SystemExit("PyGame nicht verfügbar. Programm wird beendet.")
try:
    import sklearn
    from sklearn.neural_network import MLPClassifier
    skl_avail = True
except:
    print("Scikit-Learn nicht verfügbar.")
    skl_avail = False
try:
    import Orange
    orange_avail = True
except:
    print("Orange nicht verfügbar.")
    orange_avail = False

if (skl_avail == False and orange_avail == False):
    # ohne mindestens eine der beiden KI-Bibliotheken läuft gar nichts.
    raise SystemExit("Weder Scikit-Learn noch Orange verfügbar. Programm wird beendet.")

# Initialisierung Anzeigegröße und Ausführungspfad
SCREENRECT = pg.Rect(0, 0, 865, 803)
main_dir = os.path.split(os.path.abspath(__file__))[0]

# Initialisierung der Spielobjekte ("Sprites") des Autorennspiels.
# Player = das eigene Auto - erhält auch eine move Funktion
# Car1 bis Car5 = die zu überholenden Autos auf den fünf Spuren der Autobahn

# Das eigene Auto in der untersten Zeile des Calliope-Displays
class Player(pg.sprite.Sprite):

    # Initialisierung der Positionen (X von 1 bis 5)
    playerx = 2
    # Initialisierung der Anzeigepositionen des Sprites
    spritex = [349, 389, 427, 465, 504]
    spritey = [201, 239, 277, 315, 353]
    image = None

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.image
        self.playerx = self.playerx
        self.spritex = self.spritex
        self.spritey = self.spritey
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.rect.x = self.spritex[self.playerx]
        self.rect.y = self.spritey[4] # always in bottom row

    def move(self, direction):
        if direction == 1: # right
            if self.playerx < 4:
                self.playerx += 1
                self.rect.x = self.spritex[self.playerx]
        elif direction == -1: # left
            if self.playerx > 0:
                self.playerx -= 1
                self.rect.x = self.spritex[self.playerx]

# Auto auf "Spur 1" des Calliope-Displays
class Car1(pg.sprite.Sprite):

    # zufällige Wartezeit bis Start des Fahrens
    random = random.randint(1,40)
    car1y = -1
    spritex = [349, 389, 427, 465, 504]
    spritey = [201, 239, 277, 315, 353]
    moving = False
    toggle = False # only move every second 250ms block
    image = None

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.image
        self.car1y = self.car1y
        self.spritex = self.spritex
        self.spritey = self.spritey
        self.random = self.random
        self.moving = self.moving
        self.toggle = self.toggle
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.rect.x = self.spritex[0] # immer in Spur 1
        self.rect.y = self.spritey[self.car1y]+1000 # initially draw offscreen

    def move(self):
        global score
        if self.moving == False:
            self.random -= 1
        if self.random == 0: # start moving down
            self.moving = True
            if self.car1y < 4: # moving down
                if self.toggle == False:
                    self.toggle = True
                elif self.toggle == True:
                    self.car1y +=1
                    self.rect.y = self.spritey[self.car1y]
                    self.toggle = False
            elif self.car1y == 4:              # leaving bottom row --> reset car to top
                score += 1
                self.car1y = -1
                self.rect.y = self.spritey[self.car1y]+1000
                self.random = random.randint(1,40)
                self.moving = False

# Auto auf "Spur 2" des Calliope-Displays
class Car2(pg.sprite.Sprite):

    random = random.randint(1,40)
    car2y = -1
    spritex = [349, 389, 427, 465, 504]
    spritey = [201, 239, 277, 315, 353]
    moving = False
    toggle = False # only move every second 250ms block
    image = None

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.image
        self.car2y = self.car2y
        self.spritex = self.spritex
        self.spritey = self.spritey
        self.random = self.random
        self.moving = self.moving
        self.toggle = self.toggle
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.rect.x = self.spritex[1] # immer in Spur 2
        self.rect.y = self.spritey[self.car2y]+1000 # initially draw offscreen

    def move(self):
        global score
        if self.moving == False:
            self.random -= 1
        if self.random == 0: # start moving down
            self.moving = True
            if self.car2y < 4: # moving down
                if self.toggle == False:
                    self.toggle = True
                elif self.toggle == True:
                    self.car2y +=1
                    self.rect.y = self.spritey[self.car2y]
                    self.toggle = False
            elif self.car2y == 4:              # leaving bottom row --> reset car to top
                score += 1
                self.car2y = -1
                self.rect.y = self.spritey[self.car2y]+1000
                self.random = random.randint(1,40)
                self.moving = False

# Auto auf "Spur 3" des Calliope-Displays
class Car3(pg.sprite.Sprite):

    random = random.randint(1,40)
    car3y = -1
    spritex = [349, 389, 427, 465, 504]
    spritey = [201, 239, 277, 315, 353]
    moving = False
    toggle = False # only move every second 250ms block
    image = None

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.image
        self.car3y = self.car3y
        self.spritex = self.spritex
        self.spritey = self.spritey
        self.random = self.random
        self.moving = self.moving
        self.toggle = self.toggle
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.rect.x = self.spritex[2] # always in third lane
        self.rect.y = self.spritey[self.car3y]+1000 # initially draw offscreen

    def move(self):
        global score
        if self.moving == False:
            self.random -= 1
        if self.random == 0: # start moving down
            self.moving = True
            if self.car3y < 4: # moving down
                if self.toggle == False:
                    self.toggle = True
                elif self.toggle == True:
                    self.car3y +=1
                    self.rect.y = self.spritey[self.car3y]
                    self.toggle = False
            elif self.car3y == 4:              # leaving bottom row --> reset car to top
                score += 1
                self.car3y = -1
                self.rect.y = self.spritey[self.car3y]+1000
                self.random = random.randint(1,40)
                self.moving = False

# Auto auf "Spur 4" des Calliope-Displays
class Car4(pg.sprite.Sprite):

    random = random.randint(1,40)
    car4y = -1
    spritex = [349, 389, 427, 465, 504]
    spritey = [201, 239, 277, 315, 353]
    moving = False
    toggle = False # only move every second 250ms block
    image = None

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.image
        self.car4y = self.car4y
        self.spritex = self.spritex
        self.spritey = self.spritey
        self.random = self.random
        self.moving = self.moving
        self.toggle = self.toggle
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.rect.x = self.spritex[3] # always in fourth lane
        self.rect.y = self.spritey[self.car4y]+1000 # initially draw offscreen

    def move(self):
        global score
        if self.moving == False:
            self.random -= 1
        if self.random == 0: # start moving down
            self.moving = True
            if self.car4y < 4: # moving down
                if self.toggle == False:
                    self.toggle = True
                elif self.toggle == True:
                    self.car4y +=1
                    self.rect.y = self.spritey[self.car4y]
                    self.toggle = False
            elif self.car4y == 4:              # leaving bottom row --> reset car to top
                score +=1
                self.car4y = -1
                self.rect.y = self.spritey[self.car4y]+1000
                self.random = random.randint(1,40)
                self.moving = False

# Auto auf "Spur 5" des Calliope-Displays
class Car5(pg.sprite.Sprite):

    random = random.randint(1,40)
    car5y = -1
    spritex = [349, 389, 427, 465, 504]
    spritey = [201, 239, 277, 315, 353]
    moving = False
    toggle = False # only move every second 250ms block
    image = None

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.image
        self.car5y = self.car5y
        self.spritex = self.spritex
        self.spritey = self.spritey
        self.random = self.random
        self.moving = self.moving
        self.toggle = self.toggle
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.rect.x = self.spritex[4] # always in fifth lane
        self.rect.y = self.spritey[self.car5y]+1000 # initially draw offscreen

    def move(self):
        global score
        if self.moving == False:
            self.random -= 1
        if self.random == 0: # start moving down
            self.moving = True
            if self.car5y < 4: # moving down
                if self.toggle == False:
                    self.toggle = True
                elif self.toggle == True:
                    self.car5y +=1
                    self.rect.y = self.spritey[self.car5y]
                    self.toggle = False
            elif self.car5y == 4:              # leaving bottom row --> reset car to top
                score += 1
                self.car5y = -1
                self.rect.y = self.spritey[self.car5y]+1000
                self.random = random.randint(1,40)
                self.moving = False

# Punktzahl anzeigen
class Score(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(None, 30)
        self.color = pg.Color("black")
        self.update()
        self.rect = self.image.get_rect().move(690, 45)

    def update(self):
        msg = "Punkte: %d" % score
        self.image = self.font.render(msg, True, self.color)

# Episode anzeigen
class Episode(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.font = pg.font.Font(None, 30)
        self.color = pg.Color("black")
        self.update()
        self.rect = self.image.get_rect().move(10, 45)

    def update(self):
        msg = "Episode: %d" % episode
        self.image = self.font.render(msg, True, self.color)


# Hilfsfunktion für Hintergrundbild
def load_image(file):
    file = os.path.join(main_dir, "", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Bild konnte nicht geladen werden: "%s" %s' % (file, pg.get_error()))
    return surface.convert()

# Hilfsfunktion für Textanzeige
def text_to_screen(screen, text, x, y, size = 30, color = (000, 000, 000) ):

    try:
        text = str(text)
        font = pg.font.Font(None, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except(Exception, e):
        print("Fehler bei Schriftart")
        raise e

# Hilfsfunktion zur Berechnung der KI-Aktion
def calculate_direction(player,car1,car2,car3,car4,car5):

	global ai

	p = 0
	c1 = 0
	c2 = 0
	c3 = 0
	c4 = 0
	c5 = 0

    # Normalisieren der X/Y-Werte
	for x in range(0,5):
		if player.playerx == x:
			p = 0.25 * player.playerx
		if car1.car1y == x:
			c1 = 0.2 * car1.car1y
		if car2.car2y == x:
			c2 = 0.2 * car2.car2y
		if car3.car3y == x:
			c3 = 0.2 * car3.car3y
		if car4.car4y == x:
			c4 = 0.2 * car4.car4y
		if car5.car5y == x:
			c5 = 0.2 * car5.car5y

	# Lenkaktion durch das neuronale Netzwerk berechnen lassen
	predinput = np.array([p,c1,c2,c3,c4,c5])
	pred = ai.predict(predinput.reshape(1,-1))

	direction = 0

    # Code für sklearn
	if sys.argv[1] == "sklearn":
		if np.array_str(pred).startswith("['B"):
            #print("KI: Nach rechts!")
			direction = 1
		elif np.array_str(pred).startswith("['A"):
            #print("KI: Nach links!")
			direction = -1
		else:
			direction = 0
            #print("KI: Däumchendrehen")

    # Code für Orange
	elif sys.argv[1] == "orange3":

		if pred[0] == 1: # äquivalent zu "B" drücken
            #print("KI: Nach rechts!")
			direction = 1
		elif pred[0] == 0: # äquivalent zu "A" drücken
            #print("KI: Nach links!")
			direction = -1
		else:
			direction = 0
            #print("KI: Däumchendrehen")

	return direction

#
# Hauptprogramm
#

def main(winstyle=0):

    # Info zur Nutzung ausgeben, falls keine Parameter übergeben
	if len(sys.argv)<2:
		print("Calliope Rennspiel mit KI. Modul: IQ-Test\n")
		if skl_avail:
			print('Scikit-Learn version: {}.'.format(sklearn.__version__))
		else:
			print('Scikit-Learn nicht installiert. Nur Orange Backend möglich!')
		if orange_avail:
			print('Orange version: {}.'.format(Orange.__version__))
		else:
			print('Orange nicht installiert. Nur Scikit-Learn Backend möglich!')
		print("Nutzung:\n")
		print("python ./ki-rennspiel.py <Backend-Option> <Modell-Datei>\n")
		print("     <Backend-Option>: 'sklearn' für Scikit-Learn oder 'orange3' für Orange3")
		print("     <Modell-Datei>  : Name der Datei des trainierten KI-Modells\n")
		raise SystemExit()

    # Laden des trainierten neuronalen Netzwerks
	if sys.argv[1] == "sklearn":
		print('SciKit-Learn Backend, lade ML-Modell '+sys.argv[2])
		file = open(sys.argv[2], 'rb')
	elif sys.argv[1] == "orange3":
		print('Orange3 Backend, lade ML-Modell '+sys.argv[2])
		file = open(sys.argv[2], 'rb')

	# Initialisieren der globalen Variablen
	global ai
	ai = pickle.load(file)
	global score
	score = 0
	global episode
	episode = 0

    # Initialisierung von PyGame
	pg.init()
	fullscreen = False
	winstyle = 0
	bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
	screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # Laden der Bilddateien, initialisieren der Sprites
	img = load_image("./ressourcen/sprite.png")
	Player.image = img
	Car1.image = img
	Car2.image = img
	Car3.image = img
	Car4.image = img
	Car5.image = img

	# Dekorieren des Spielfensters
	icon = pg.transform.scale(Car1.image, (32, 32))
	pg.display.set_icon(icon)
	pg.display.set_caption("Künstliche Intelligenz spielerisch in die Schule bringen")

	# Hintergrundbild setzen
	bgdtile = load_image("./ressourcen/surface.png")
	background = pg.Surface(SCREENRECT.size)
	for x in range(0, SCREENRECT.width, bgdtile.get_width()):
		background.blit(bgdtile, (x, 0))
	screen.blit(background, (0, 0))
	pg.display.flip()

	# Hauptmenü initialisieren
	pg.font.init()
	text_to_screen(screen, "Drücke", 10, 10)
	text_to_screen(screen, "(1) für Mensch", 10, 50)
	text_to_screen(screen, "(2) für KI", 10, 90)
	text_to_screen(screen, "(T)urbo AUS", 10, 130)
	pg.display.flip()

	# Startvariablen setzen
	gameOn = False
	gameMode = 0
	turbo = False
	clock = pg.time.Clock()

	# Hauptmenü - Auswahl manuelle oder KI Steuerung
	cont = False
	while cont==False:

		pg.event.clear()
		event = pg.event.wait()
		if event.type == pg.QUIT:
			return
		if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
			return
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_1:
				print("Selbst spielen")
				gameMode = 0
				cont = True
			elif event.key == pg.K_2:
				print("KI spielen lassen")
				gameMode = 1
				cont = True
			elif event.key == pg.K_t:
				if turbo:
					turbo = False
					print("Turbo eingeschaltet")
					for x in range(0, SCREENRECT.width, bgdtile.get_width()):
						background.blit(bgdtile, (x, 0))
					screen.blit(background, (0, 0))
					text_to_screen(screen, "Drücke", 10, 10)
					text_to_screen(screen, "(1) für Mensch", 10, 50)
					text_to_screen(screen, "(2) für KI", 10, 90)
					text_to_screen(screen, "(T)urbo AUS", 10, 130)
					pg.display.flip()
				else:
					turbo = True
					print("Turbo ausgeschaltet")
					for x in range(0, SCREENRECT.width, bgdtile.get_width()):
						background.blit(bgdtile, (x, 0))
					screen.blit(background, (0, 0))
					text_to_screen(screen, "Drücke", 10, 10)
					text_to_screen(screen, "(1) für Mensch", 10, 50)
					text_to_screen(screen, "(2) für KI", 10, 90)
					text_to_screen(screen, "(T)urbo AN ", 10, 130)
					pg.display.flip()

	scorelist = []

	for i in range(50):

		score = 0
		print("Episode: ",i)
		episode = i+1

		# Sprite-Gruppen und Sprites initialisieren
		all = pg.sprite.RenderUpdates()
		cars = pg.sprite.Group()
		Player.containers = all
		Car1.containers = cars, all
		Car2.containers = cars, all
		Car3.containers = cars, all
		Car4.containers = cars, all
		Car5.containers = cars, all
		Score.containers = all
		Episode.containers = all

		player = Player()
		car1 = Car1()
		car2 = Car2()
		car3 = Car3()
		car4 = Car4()
		car5 = Car5()

		if pg.font:
			all.add(Score())
			all.add(Episode())

		background = pg.Surface(SCREENRECT.size)
		for x in range(0, SCREENRECT.width, bgdtile.get_width()):
			background.blit(bgdtile, (x, 0))
		screen.blit(background, (0, 0))
		pg.display.flip()

		# Bildschirm zeichnen
		all.clear(screen, background)
		all.update()
		dirty = all.draw(screen)
		pg.display.update(dirty)

		# Hauptschleife für laufendes Spiel
		while player.alive():

			# Bewegen der Autos
			car1.move()
			car2.move()
			car3.move()
			car4.move()
			car5.move()

			# Abfrage menschliche Steuerung
			for event in pg.event.get():
				if event.type == pg.QUIT:
					return
				if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
					return
			keystate = pg.key.get_pressed()

			# Auto bewegen, falls menschliche Steuerung
			if gameMode == 0:
				direction = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]
				player.move(direction)

			# Auto durch KI bewegen lassen, falls KI-Steuerung
			elif gameMode == 1:
				direction = calculate_direction(player,car1,car2,car3,car4,car5)
				if direction != 0:
					player.move(direction)

			# Kollisionsabfrage - gibt es einen Crash?
			for car in pg.sprite.spritecollide(player, cars, 1):
				print ("collision!")
				player.kill()

			# Bildschirm zeichnen
			all.clear(screen, background)
			all.update()
			dirty = all.draw(screen)
			pg.display.update(dirty)

			# Bildrate setzen - 4 Bilder pro Sekunde
			if gameMode == 0: # im manuellen Modus kein Turbo
				clock.tick(4)
			elif gameMode == 1: # aktiviere KI-Turbo
				if turbo:
					clock.tick(1000000000)
				else:
					clock.tick(4)

		print("Episode Score: ",score)
		scorelist.append(score)

		# Abschlussbildschirm zeichnen,
		text_to_screen(screen, "KOLLISION! :-(", 150, 250, 100, (255, 0, 0))
		text_to_screen(screen, "PUNKTE: "+np.median(scorelist).astype('str'), 150, 350, 100, (255, 0, 0))
		text_to_screen(screen, "Drücke Q für Ende", 100, 450, 100, (255, 0, 0))
		pg.display.flip()


		if turbo == False:
			break

	print("Ende.")
	print("Average over episodes: ",np.median(scorelist))

	#  warten auf Beenden des Programms mit Q
	cont = False
	while cont==False:

		pg.event.clear()
		event = pg.event.wait()
		if event.type == pg.QUIT:
			return
		if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
			return
		elif event.type == pg.KEYDOWN:
			if event.key == pg.K_q:
				print("Ende")
				cont = True

	pg.quit()

# Wenn das Script aufgerufen wird, die Main Funktion aufrufen.
if __name__ == "__main__":
	main()
