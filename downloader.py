from pytube import YouTube

print("YouTube Video Downloader")

url = input("Enter YouTube video URL: ")

try:
    yt = YouTube(url)

    print("Title:", yt.title)

    video = yt.streams.get_highest_resolution()

    print("Downloading...")

    video.download()

    print("Download completed.")

except Exception as e:
    print("Error:", e)