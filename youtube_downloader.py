# yt/youtube_downloader.py
import os
import sys
import shutil
import tempfile
import subprocess


def download_youtube_cc(video_url):
    try:
        # Find the location of the dl-youtube-cc executable
        dl_youtube_cc_path = shutil.which("dl-youtube-cc")

        # Create a temporary directory to store the downloaded text file
        with tempfile.TemporaryDirectory() as temp_dir:
            # Change the current working directory to the temporary directory
            os.chdir(temp_dir)

            # Construct the command using the dynamic path
            command = f"{dl_youtube_cc_path} {video_url}"
            subprocess.run(command, shell=True, check=True)

            # Find the generated text file in the current directory
            file_name = next(filename for filename in os.listdir() if filename.endswith(".txt"))

            # Display the entire transcript of the downloaded text file
            with open(file_name, 'r', encoding='utf-8') as file:
                transcript = file.read()

            # st.markdown(transcript)
            print(transcript)
            # st.success("Closed captions downloaded and displayed successfully.")

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error: {e}")
    except RecursionError:
        sys.exit()
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
