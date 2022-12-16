import webbrowser

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link 
	def open(self):
		webbrowser.open(self.link)	

def read_video():
	title = input("Title of video: ") + "\n" 
	link = input("Link of video: ") + "\n"
	video = Video(title, link)
	return video

def print_video(video):
	print("Video title: "  + video.title , end = "")
	print("Video link: " + video.link , end = "")

def read_videos():
	total_video = input("How many video you want?: ")
	videos = []
	for i in range(int(total_video)):
		print("Enter video", i+1)
		video = read_video()
		videos.append(video)
	return videos

def print_videos(videos):
	for i in range(len(videos)):
		print("Video", i+1)
		print_video(videos[i])

def write_video_txt(video, file):
	file.write(video.title)
	file.write(video.link)

def write_videos_txt(videos, file):
	total_video = len(videos)
	#file.write("Number of video: ")
	file.write(str(total_video) + "\n")
	for i in range(total_video):
		#file.write("Video " + str(i+1))
		write_video_txt(videos[i], file)

def read_video_txt(file):
	#number = file.readline()
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

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name 
		self.description = description
		self.rating = rating
		self.videos = videos

def read_playlist():
	name = input("Enter name of playlist: ") + "\n"
	description = input("Enter description of playlist: ") + "\n"
	rating = input("Enter rating vote for playlist (1-5): ") + "\n"
	videos = read_videos()
	playlist = Playlist(name, description, rating, videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name)
		file.write(playlist.description)
		file.write(playlist.rating)
		write_videos_txt(playlist.videos, file)
		#print("---\n" +"Succesfully enter playlist!!!")

def read_playlist_from_txt():
	with open("data.txt", "r") as file:
		playlist_name = file.readline()
		playlist_description = file.readline()
		playlist_rating = file.readline()
		playlist_videos = read_videos_txt(file)
		playlist = Playlist(playlist_name, playlist_description, playlist_rating,playlist_videos)
	return playlist

def print_playlist(playlist):
	print("-----")
	print("Playlist name: " + playlist.name, end ="")
	print("Playlist description: " + playlist.description, end ="")
	print("Playlist rating: " + playlist.rating, end ="")
	print_videos(playlist.videos)

def show_menu():
	print("Main menu: \n------------------------------")
	print("| Option 1 | Create playlist |")
	print("------------------------------")
	print("| Option 2 | Show playlist   |")
	print("------------------------------")
	print("| Option 3 | Play a video    |")
	print("------------------------------")
	print("| Option 4 | Add a video     |")
	print("------------------------------")
	print("| Option 5 | Remake a video  |")
	print("------------------------------")
	print("| Option 6 | Delete a video  |")
	print("------------------------------")
	print("| Option 7 | Save and Exit   |")
	print("------------------------------")

def select_in_range(prompt, min , max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max :
		choice = input(prompt)

	choice = int(choice)
	return choice

def play_video(playlist):
	print_videos(playlist.videos)
	total = len(playlist.videos)
	#print("Choose an video (1-" + str(total) +"): ")
	choice = select_in_range("Select an video (1-" + str(total) +"): ", 1, total)
	print("\nOpen video: " + playlist.videos[choice-1].title + "\nLink: " + playlist.videos[choice-1].link, end = "")
	playlist.videos[choice-1].open()

def add_video(playlist):
	print("Enter new video information")
	new_video_title = input("Enter new video title: ") + "\n"
	new_video_link = input("Enter new video link: ") + "\n"
	print("\nSuccesfully enter new video information!!! ")
	new_video = Video(new_video_title, new_video_link)
	playlist.videos.append(new_video)
	return playlist

def main():
	try:
		playlist = read_playlist_from_txt()
		print("Succesfully loaded data !!!")
	except:
		print("Welcome first user !!!")

	while True:
		show_menu()
		choice = select_in_range("Enter one option (1-7): ",1,7)
		if choice == 1:
			playlist = read_playlist()
			print("\nSuccesfully Create playlist !!!")
			input("\nPress Enter to continue.\n")	
		elif choice == 2:
			print_playlist(playlist)
			input("\nPress Enter to continue.\n")	
		elif choice == 3:
			play_video(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 4:
			playlist = add_video(playlist)
			input("\nPress Enter to continue.\n")	
		elif choice == 7:
			write_playlist_txt(playlist)
			print("Saved, exist.")
			break
		else:
			print("Wrong input, try again!")
			break
main()