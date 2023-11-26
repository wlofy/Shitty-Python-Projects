from pytube import YouTube

url = input("Enter the URL Nigga \n")

video = YouTube(url)

print("Video Title:")
print(video.title)

videos = video.streams.filter(file_extension= 'mp4')
vid = list(enumerate(videos))
for i in vid:
    print(i)
strm = int(input("Enter the index at the starting of every tag to download that shit\n"))
videos[strm].download()
print("Downloaded, check folder :)")