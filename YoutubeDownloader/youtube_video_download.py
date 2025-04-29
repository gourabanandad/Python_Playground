from yt_dlp import YoutubeDL
path_to_save = "C:\\Users\\goura\\Desktop\\Videoes"
video_url = input("Enter the YouTube URL: ")    # Give the url of the video
with YoutubeDL({"outtmpl": "C:/Users/goura/Desktop/Videoes/%(funny)s.%(ext)s"}) as ydl:
    print("Downloading...")
    ydl.download([video_url])
print("Download Complete.")