import cv2
import os
from natsort import natsorted  # ensures correct numerical order (e.g., 1.png, 2.png, ..., 76.png)
import argparse

def images_to_video(image_folder, output_path="output_video.mp4", fps=20):
    # Get list of image files, sorted naturally
    image_files = [f for f in os.listdir(image_folder) if f.endswith(".png")]
    image_files = natsorted(image_files)  # sort like 00001.png, 00002.png ...

    if not image_files:
        raise ValueError("No PNG images found in the specified folder.")

    # Load the first image to get frame size
    first_frame_path = os.path.join(image_folder, image_files[0])
    frame = cv2.imread(first_frame_path)
    height, width, layers = frame.shape
    size = (width, height)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'XVID' for .avi
    out = cv2.VideoWriter(output_path, fourcc, fps, size)

    for filename in image_files:
        frame_path = os.path.join(image_folder, filename)
        frame = cv2.imread(frame_path)
        out.write(frame)

    out.release()
    print(f"Video saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file_path")
    parser.add_argument("-o", "--output_file_name")
    args = parser.parse_args()
    input_file = "/Users/leahheil/Desktop/phd/Vessel_segmentation/denver-master" + args.input_file_path
    images_to_video(input_file, args.output_file_name)

