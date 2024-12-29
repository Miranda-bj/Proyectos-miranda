# Download video using python

from pytube import YouTube

link = input("Enter the link of the video you want to download: ")

video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()
print("Download completed!!")

