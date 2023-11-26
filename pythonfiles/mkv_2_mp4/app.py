from moviepy.editor import VideoFileClip

def convert_video(input_file, output_file):
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, codec="libx264", audio_codec="aac", temp_audiofile="temp.m4a", remove_temp=True, threads=4)
    print(f"Conversion complete. Output file: {output_file}")

if __name__ == "__main__":
    # Specify input and output file names
    input_file = "input.mkv"
    output_file = "output.mp4"

    
    convert_video(input_file, output_file)
