import os
import requests
import tarfile

def download_and_extract_ffmpeg(dest_folder='/workspaces/Translator'):
    url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-i686-static.tar.xz"  # or another safe mirror
    archive_path = "ffmpeg.tar.xz"

    # Download ffmpeg tar.xz
    print("Downloading ffmpeg...")
    r = requests.get(url, stream=True)
    with open(archive_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

    # Extract
    print("Extracting ffmpeg...")
    with tarfile.open(archive_path, 'r:xz') as tar:
        tar.extractall(dest_folder)

    # Cleanup
    os.remove(archive_path)
    print(f"FFmpeg is ready in {dest_folder}/")

# Usage
download_and_extract_ffmpeg()
