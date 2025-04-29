# YouTube Video Downloader 🎥

A simple Python script to download any YouTube video directly to your computer.

## Features
- Download videos from YouTube using just the video URL.
- Save videos in high quality (depending on availability).

## Requirements
- Python 3.8+
- yt_dlp

Install dependencies:
```bash
pip install -r requirements.txt
```
## How to Run
- Clone this repository or download the script.
- Open a terminal and navigate to the project directory.
- Run the script:
```bash
python youtube_video_download.py
```
- Enter the YouTube video URL when prompted.

```mathematica
Enter the YouTube URL: https://youtu.be/D8rgjDF3Grc?si=nH6Hu70_ICmlYHQv
Downloading...
[youtube] Extracting URL: https://youtu.be/D8rgjDF3Grc?si=nH6Hu70_ICmlYHQv 
[youtube] D8rgjDF3Grc: Downloading webpage 
[youtube] D8rgjDF3Grc: Downloading tv client config 
[youtube] D8rgjDF3Grc: Downloading player 8102da6c-main 
[youtube] D8rgjDF3Grc: Downloading tv player API JSON 
[youtube] D8rgjDF3Grc: Downloading ios player API JSON 
[youtube] D8rgjDF3Grc: Downloading m3u8 information 
[info] D8rgjDF3Grc: Downloading 1 format(s): 135+251 
[download] Destination: C:\Users\goura\Desktop\Videoes\NA.f135.mp4 
[download] 100% of  220.61KiB in 00:00:02 at 100.44KiB/s
[download] Destination: C:\Users\goura\Desktop\Videoes\NA.f251.webm 
[download] 100% of   72.31KiB in 00:00:01 at 67.31KiB/s
[Merger] Merging formats into "C:\Users\goura\Desktop\Videoes\NA.mkv" 
Deleting original file C:\Users\goura\Desktop\Videoes\NA.f251.webm (pass -k to keep) 
Deleting original file C:\Users\goura\Desktop\Videoes\NA.f135.mp4 (pass -k to keep) 
Download Complete.
```

## License
This project is licensed under the MIT License.