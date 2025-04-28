from yt_dlp import YoutubeDL
path_to_save = "C:\\Users\\goura\\Desktop\\Videoes"
video_url = "https://youtube.com/shorts/Hcg7VALR4Jk?si=Gi3SqdqbS_oyeyst"    # Give the url of the video
with YoutubeDL({"outtmpl": "C:/Users/goura/Desktop/Videoes/%(funny)s.%(ext)s"}) as ydl:
    ydl.download([video_url])
