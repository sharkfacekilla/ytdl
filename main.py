from pytube import YouTube
from pytube.cli import on_progress
import os

def download(link, output):
    print("Download starting...")
    vid = YouTube(link, on_progress_callback=on_progress)
    video = vid.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    output_file = os.path.join(output, video.title + ".mp4")

    if os.path.exists(output_file):
        print(f"{video.title}.mp4 already exists.")
    else:
        try:
            print("Download started")
            video.download(output)
            print("\nDownload is completed and saved to: " + output)
        except:
            print("An error has occurred during downloading. Try again.")


link = input("Enter the Link: ")
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
download(link, desktop)