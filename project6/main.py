import tkinter as tk
from tkinter import filedialog
import yt_dlp  # Make sure you install this via `pip install yt-dlp`

def download_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'best',  # Downloads the best video quality available
            'outtmpl': f'{save_path}/%(title)s.%(ext)s'  # Saves the file in the selected folder
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video Downloaded Successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected Folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hides the tkinter root window

    video_url = input("Please Enter a YouTube URL: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid Save location.")
