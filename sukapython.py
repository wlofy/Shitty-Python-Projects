from pytube import YouTube
import os

yt = YouTube(str(input("Enter URL MY NIGGA: \n")))

video = yt.streams.filter(only_audio =True).first()

print("Enter where you wanna save this file (leave blank for this folder)")
destination = str(input(">>")) or '.'

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)

print(yt.title + " downloaded successfuly bitch.")



