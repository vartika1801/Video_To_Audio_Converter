import streamlit as st
import os
import yt_dlp
import subprocess

# Set paths for the download
desktop_directory = os.path.join(os.path.expanduser("~"), "Desktop")
video_output_folder = os.path.join(desktop_directory, "ML-course-downloads")
audio_output_folder = os.path.join(desktop_directory, "ML-course-audiofiles")
os.makedirs(video_output_folder, exist_ok=True)
os.makedirs(audio_output_folder, exist_ok=True)
ffmpeg_path = "C:/ffmpeg-2024-10-10-git-0f5592cfc7-full_build/bin/ffmpeg.exe"

# Video download settings
video_dl_options = {
    '--ffmpeg-location': ffmpeg_path,
    'format': 'best',
    'outtmpl': os.path.join(video_output_folder, '%(title)s.%(ext)s'),
}

# Audio conversion settings
audio_dl_options = {
    '--ffmpeg-location': ffmpeg_path,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': os.path.join(audio_output_folder, '%(title)s.%(ext)s'),
}

# Streamlit app layout
st.title("Video and Audio Downloader")
st.write("Enter your search query to download videos and convert them to audio.")

# Input from the user
search_term = st.text_input("Search Term", "machine learning course")
num_videos = st.number_input("Number of Videos", min_value=1, max_value=10, value=3)
trim_seconds = st.number_input("Trim audio from the first (seconds)", min_value=20, value=30)

# Button to start download and conversion
if st.button("Download and Convert"):
    # Function to download videos based on search query
    def fetch_videos(search_term, num_videos):
        try:
            with yt_dlp.YoutubeDL(video_dl_options) as ydl:
                search_results = ydl.extract_info(f"ytsearch{num_videos}:{search_term}", download=False)['entries']
                urls = [result['webpage_url'] for result in search_results]
                ydl.download(urls)
                st.write(f"Downloaded {len(urls)} videos for the search term: '{search_term}'")
                return urls
        except Exception as error:
            st.write(f"Error while downloading: {error}")
            return []

    # Convert videos to audio
    def convert_videos_to_audio(video_links):
        try:
            with yt_dlp.YoutubeDL(audio_dl_options) as ydl:
                ydl.download(video_links)
                st.write("Converted video files to audio.")
        except Exception as error:
            st.write(f"Error during audio conversion: {error}")

    # Trim the first 'y' seconds from each audio file
    def trim_audio(start_seconds):
        try:
            audio_files = [os.path.join(audio_output_folder, f) for f in os.listdir(audio_output_folder) if f.endswith('.mp3')]
            for audio_file in audio_files:
                trimmed_audio = audio_file.replace('.mp3', '_short.mp3')
                subprocess.run([
                    ffmpeg_path, '-i', audio_file, '-ss', str(start_seconds), '-acodec', 'copy', trimmed_audio
                ])
            st.write(f"Trimmed first {start_seconds} seconds from each audio file.")
        except Exception as error:
            st.write(f"Error while trimming audio: {error}")

    # Merge all trimmed audio files
    def combine_audio(output_filename):
        try:
            trimmed_audio_files = [os.path.join(audio_output_folder, f) for f in os.listdir(audio_output_folder) if '_short.mp3' in f]
            if trimmed_audio_files:
                with open("audio_file_list.txt", "w") as file_list:
                    for audio in trimmed_audio_files:
                        file_list.write(f"file '{audio}'\n")

                subprocess.run([ffmpeg_path, '-f', 'concat', '-safe', '0', '-i', 'audio_file_list.txt', '-c', 'copy', output_filename])
                st.write(f"Combined audio files into {output_filename}")
            else:
                st.write("No trimmed audio files found to merge.")
        except Exception as error:
            st.write(f"Error during audio merging: {error}")

    # Process
    video_links = fetch_videos(search_term, num_videos)
    if video_links:
        convert_videos_to_audio(video_links)
        trim_audio(trim_seconds)
        combine_audio(os.path.join(audio_output_folder, 'final_audio_output.mp3'))