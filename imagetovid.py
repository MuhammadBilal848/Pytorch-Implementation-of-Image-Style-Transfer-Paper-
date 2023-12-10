import cv2
import os 


def create_video(images_path, output_video_path, fps):
  """
  Creates a video from a sequence of images.

  Args:
    images_path: Path to the folder containing the images.
    output_video_path: Path to the output video.
    fps: Frames per second for the video.
  """

  # Get all images from the folder
  images = []
  for filename in os.listdir(images_path):
    if filename.endswith((".jpg", ".png")):
      images.append(cv2.imread(os.path.join(images_path, filename)))

  # Get the size of the first image
  height, width, layers = images[0].shape

  # Define the video writer object
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for h.264 codec
  video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

  # Write each image to the video
  for image in images:
    video_writer.write(image)

  # Release the video writer object
  video_writer.release()

# Example usage
images_path = "C:/Users/Muhammad Bilal/Downloads/cat to art"
output_video_path = "output.mp4"
fps = 24

create_video(images_path, output_video_path, fps)

print("Video created successfully!")
