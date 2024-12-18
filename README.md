# Video and Audio Downloader
This project is a Streamlit application that allows users to search for videos on YouTube, download them, convert them into audio files, trim the audio, and combine multiple audio files into a single output. The app leverages `yt_dlp` for video and audio downloading and `ffmpeg` for audio processing.

## Features
1. **Video Download**:
   - Search for videos on YouTube using a query.
   - Download a specified number of videos.
     
2. **Audio Conversion**:
   - Convert downloaded videos into MP3 audio files.

3. **Audio Trimming**:
   - Trim a specified number of seconds from the beginning of each audio file.

4. **Audio Merging**:
   - Combine trimmed audio files into a single MP3 file.

5. **Interactive UI**:
   - User-friendly interface built with Streamlit for seamless interaction.

## How It Works
1. User inputs:
   - **Search Term**: The query for the videos (e.g., "machine learning course").
   - **Number of Videos**: The number of videos to download.
   - **Trim Audio**: The number of seconds to trim from the beginning of each audio file.

2. The application:
   - Searches and downloads videos using `yt_dlp`.
   - Converts the videos to MP3 audio files.
   - Trims the specified seconds from the beginning of each audio file.
   - Combines all trimmed audio files into a single output file.

## Requirements
### Prerequisites
- Python 3.7 or later
- `yt_dlp`
- `streamlit`
- `ffmpeg`

## File Structure
├── app.py                  
├── requirements.txt        
├── README.md              


## Usage
1. Launch the Streamlit app.
2. Enter the search term, number of videos to download, and the trim duration.
3. Click on **"Download and Convert"**.
4. The application will:
   - Download the specified videos.
   - Convert them into audio files.
   - Trim the audio as specified.
   - Merge the audio files into a single MP3 file.

The downloaded videos and audio files will be saved in the following directories:
- **Videos**: `~/Desktop/ML-course-downloads`
- **Audio Files**: `~/Desktop/ML-course-audiofiles`

## Configuration
### FFmpeg Setup
- Update the `ffmpeg_path` variable with the correct path to the `ffmpeg.exe` file.
- Ensure `ffmpeg` is installed and added to your system's PATH.

### Output Directories
- Videos are saved in `~/Desktop/ML-course-downloads`.
- Audio files are saved in `~/Desktop/ML-course-audiofiles`.

## Limitations
- The application relies on `yt_dlp` for video downloads and may be subject to YouTube's rate limits.
- The provided `ffmpeg` path must be correctly configured for audio processing.

## Future Enhancements
- Add support for downloading playlists.
- Allow users to specify audio quality and format.
- Add progress tracking for downloads and conversions.

## Collaboration
This project was done in collaboration with https://github.com/arnavtiet.

## Acknowledgments
- **yt_dlp** for simplifying YouTube video and audio downloads.
- **Streamlit** for creating a seamless and interactive user interface.

