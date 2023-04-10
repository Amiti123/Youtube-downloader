from pytube import YouTube

link = "https://youtu.be/MT0A5bajA6Q"

youtube_1 = YouTube(link)

# print(youtube_1.title)
# print(youtube_1.thumbnail_url)
# only for audio
# videos = youtube_1.streams.filter(only_audio=true)
# and remove videos = youtube_1.strams.all() it is for all format
videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)

print()
strm = int(input("enter: "))
videos[strm].download()
print("sucessfullly downloaded")

