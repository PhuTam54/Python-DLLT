
import pygame
import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link 
	def open(self):
		print("Opening " + self.title.rstrip() + "...")
		webbrowser.open(self.link)	

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name 
		self.description = description
		self.rating = rating
		self.videos = videos

class TextButton:
	def __init__(self, text, position):
		self.text = text
		self.position = position

	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if ((mouse_x > self.position[0]) and (mouse_x < self.position[0] + self.text_box[2]) and (mouse_y > self.position[1]) and (mouse_y < self.position[1] + self.text_box[3])):
			return True
		else:
			return False

	def draw(self):
		font = pygame.font.SysFont('sans', 20)
		text_render = font.render( self.text , True, BLACK)
		self.text_box = text_render.get_rect()

		if self.is_mouse_on_text():
			text_render = font.render( self.text , True, BLUE)
			pygame.draw.line(screen, BLUE, (self.position[0], self.position[1] + self.text_box[3]),(self.position[0]+self.text_box[2], self.position[1] + self.text_box[3]))
		else:
			text_render = font.render( self.text, True, BLACK)

		screen.blit(text_render, self.position)

def read_playlist_from_txt(file):
	playlist_name = file.readline()
	playlist_description = file.readline()
	playlist_rating = file.readline()
	playlist_videos = read_videos_txt(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating,playlist_videos)
	return playlist

def read_playlists_from_txt():
	playlists = []
	with open("data.txt", "r") as file:
		total = file.readline() 
		for i in range(int(total)):
			playlist = read_playlist_from_txt(file)
			playlists.append(playlist)
	return playlists

def read_video_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video 

def read_videos_txt(file):
	videos = []
	total = file.readline() 
	for i in range(int(total)):
		video = read_video_txt(file)
		videos.append(video)
	return videos

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Flappy Bird')
running = True
WHITE = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)
clock = pygame.time.Clock()

# Load data
playlists = read_playlists_from_txt()

playlists_btn_list = []
videos_btn_list = []
margin = 50

for i in range(len(playlists)):
	playlist_btn = TextButton(playlists[i].name.rstrip(), (30, 50 + margin*i))
	playlists_btn_list.append(playlist_btn)

# pygame runnig 
while running:		
	clock.tick(60)
	screen.fill(WHITE)

	for playlist_btn in playlists_btn_list:
		playlist_btn.draw()

	for video_btn in videos_btn_list:
		video_btn.draw()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for i in range(len(playlists_btn_list)):
					if playlists_btn_list[i].is_mouse_on_text():
						videos_btn_list = []
						playlist_choice = i
						for j in range(len(playlists[i].videos)):
							video_btn = TextButton(str(j+1) + ". " + playlists[i].videos[j].title.rstrip(), (150, 50 + margin*j))
							videos_btn_list.append(video_btn)

				for k in range(len(videos_btn_list)):
					if videos_btn_list[k].is_mouse_on_text():
						playlists[playlist_choice].videos[k].open()

		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()