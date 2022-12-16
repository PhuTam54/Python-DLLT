class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link 

def read_video():
	title = input("Title of video: ") 
	link = input("Link of video: ")
	video = Video(title, link)
	return video

def print_video(video):
	print(video.title, end = "")
	print(video.link, end = "")

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
	file.write("Video title: "  + video.title + "\n")
	file.write("Video link: " + video.link + "\n")

def write_videos_txt(videos, file):
	total_video = len(videos)
	#file.write("Number of video: ")
	file.write(str(total_video) + "\n")
	for i in range(total_video):
		file.write("Video " + str(i+1) +"\n")
		write_video_txt(videos[i], file)

def read_video_txt(file):
	number = file.readline()
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
	name = input("Enter name of playlist: ")
	description = input("Enter description of playlist: ")
	rating = input("Enter rating vote for playlist (1-5): ")
	videos = read_videos()
	playlist = Playlist(name, description, rating, videos)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt", "w") as file:
		file.write("Playlist name: " + playlist.name + "\n")
		file.write("Playlist description: " + playlist.description +"\n")
		file.write("Playlist rating: " + playlist.rating + "\n")
		write_videos_txt(playlist.videos, file)
		print("---\n" +"Succesfully enter playlist!!!")

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
	print(playlist.name, end ="")
	print(playlist.description, end ="")
	print(playlist.rating, end ="")
	print_videos(playlist.videos)

def main():
#	videos = read_videos()
#	write_videos_txt(videos)
#	videos = read_videos_txt()
#	print_videos(videos)

	playlist = read_playlist()
	write_playlist_txt(playlist)
	playlist = read_playlist_from_txt()
	print_playlist(playlist)
main()
