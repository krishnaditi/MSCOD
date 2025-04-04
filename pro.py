import os
import cv2
import yt_dlp

# Function to download video
def download_video(url, output_path="video.mp4"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_path,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    return output_path

# Function to extract frames
def extract_frames(video_path, output_folder="test", frame_rate=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = max(1, fps // frame_rate)  # Extract frames per second

    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_count} frames to '{output_folder}'.")

# Main Execution
if __name__ == "__main__":
    video_url = "https://youtu.be/0whIzsNWTn4"
    video_file = download_video(video_url)
    extract_frames(video_file)