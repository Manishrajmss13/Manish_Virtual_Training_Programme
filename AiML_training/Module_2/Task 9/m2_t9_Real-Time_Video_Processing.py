import cv2
import os

# Load Input Video
video_path = "vid.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Unable to open video.")
    exit()

print("Video loaded successfully.")

# Read Video Properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Width  : {frame_width}")
print(f"Height : {frame_height}")
print(f"FPS    : {fps}")

# Create Output Folder
os.makedirs("output", exist_ok=True)

output_path = "output/edge_output.mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (frame_width, frame_height)
)

print("VideoWriter initialized.")

print("\nPress 'Q' to stop processing...\n")

# Frame-by-Frame Processing
while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Convert to Grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Convert back to BGR before saving
    edge_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Save frame
    out.write(edge_bgr)

    # Display frame
    cv2.imshow("Real-Time Edge Detection", edges)

    # Press Q to Quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()

print("\nVideo processing completed successfully.")
print(f"Processed video saved to:\n{output_path}")


# Observation

#- The input video was processed frame by frame using OpenCV.
#- Canny Edge Detection successfully detected the boundaries of the objects and the person in the video.
#- The processed frames were displayed in real time and saved into a new video using `cv2.VideoWriter`.
#- The output video maintained the same frame size and frame rate as the original video.

# Bug Encountered
#Initially, the output video could not be saved correctly because the processed edge image was a single-channel grayscale image, while `cv2.VideoWriter` expects a three-channel BGR image.
#The edge image was converted back to BGR using:

```python
edge_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
```

#After this change, the output video was saved successfully.

