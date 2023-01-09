import cv2
import os

def build_video_from_pngs(image_folder: str, video_name: str = "output.mp4"):

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    
    print("Video saved to:", os.getcwd())

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_name, fourcc, 5, frameSize=(width,height))
    
    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
    
    cv2.destroyAllWindows()
    video.release()
