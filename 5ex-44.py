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
	print("Video title:", video.title)
	print("Video link:", video.link)

#user_input = input("How many video you want?: ")

def main():
	video = read_video()
	print("---")
	print_video(video)
main()