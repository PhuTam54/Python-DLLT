class Video():
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
	print("---")
	for i in range(len(videos)):
		print("Video", i+1)
		print_video(videos[i])

def write_video_txt(video, file):
	file.write("Video title: "  + video.title + "\n")
	file.write("Video link: " + video.link + "\n")

def write_videos_txt(videos):
	total_video = len(videos)
	with open("data.txt", "w") as file:
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

def read_videos_txt():
	videos = []
	with open("data.txt", "r") as file:
		total = file.readline() 
		for i in range(int(total)):
			video = read_video_txt(file)
			videos.append(video)
		return videos

def main():
	videos = read_videos()
	write_videos_txt(videos)
	videos = read_videos_txt()
	print_videos(videos)
main()
