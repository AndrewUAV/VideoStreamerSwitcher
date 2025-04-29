from flask import Flask, render_template, Response, redirect, url_for
import cv2
import time

app = Flask(__name__)

camera_indices = ['/dev/video0',
                  '/dev/video2']
current_index = 0
cap = cv2.VideoCapture(camera_indices[current_index])


def switch_camera():
    global cap, current_index

    if cap.isOpened():
        cap.release()
        print("Stop Camera")

    time.sleep(1)

    current_index = (current_index + 1) % len(camera_indices)
    cap = cv2.VideoCapture(camera_indices[current_index])
    print(f"Connect to camera : {camera_indices[current_index]}")


def generate_frames():
    global cap
    while True:
        if cap.isOpened():
            success, frame = cap.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/switch')
def switch():
    switch_camera()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
