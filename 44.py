class Video:
	def __init__(self, title,link):
		self.title = title
		self.link = link

def read_video():
	title = input("Nhap tieu de cua video: ")
	link = input("Nhap link cua video: ")
	video = Video(title, link)
	return video

def print_video(video):
	print("Video title: ",video.title)
	print("Video link: ",video.link)

def read_videos():
	total = int(input("Nhap so video ban muon: "))
	videos = []
	for i in range(total):
		print("Nhap video ", i+1,":")
		video=read_video()
		videos.append(video)
	return videos

def print_videos(videos):
	print("\n")
	for i in range(10):
		print("- ", end ="")
	print("\n")
	for i in range(len(videos)):
		print_video(videos[i])	

def write_video_txt(videos, file):
	file.write(videos.title +"\n")
	file.write(videos.link +"\n")

def write_to_text(videos):
	total = len(videos)
	with open("data.txt", "w") as file:
		file.write(str(total)+"\n")
		for i in range(total):
			write_video_txt(videos[i], file)

def main():
	videos =read_videos()
	write_to_text(videos)
	
	print_videos(videos)

main()
