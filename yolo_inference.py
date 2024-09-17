
from ultralytics import YOLO

model = YOLO('yolov8x')

try:
    results = model.predict('./input_videos/08fd33_4.mp4')
    results.save('./output_videos/08fd33_4.mp4')
    print("Video saved successfully!")
    print(results[0])
    print('==================================')
    #for box in results[0].boxes:
        #print(box)
except Exception as e:
    print("Error saving video:", str(e))

