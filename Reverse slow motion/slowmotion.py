import cv2

# Load a video file
video_path = 'test_vid_2.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error opening video file.")
    exit()

# Get the frames per second (fps) and frame size
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create an output video writer
output_path = 'output_slow_motion_reverse.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Read and duplicate frames to create the slow-motion effect in reverse
frame_list = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_list.append(frame)

# Write frames in reverse order with slow-motion effect
for frame in frame_list[::-1]:
    out.write(frame)
    out.write(frame)  # Duplicate frame for slow-motion effect

    cv2.imshow('Slow Motion Reverse', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and writer, and close the OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()
