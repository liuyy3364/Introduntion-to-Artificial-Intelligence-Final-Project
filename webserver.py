from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('stream.html')

cam_wrapper = []
frame_wrapper = [bytes()]
def gen():
    while 1:
        frame = frame_wrapper[0]
        ret , jpg = cv2.imencode(".jpg", frame)
        jpg = jpg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
        mimetype='multipart/x-mixed-replace; boundary=frame')

def web_server():
    app.run(host='0.0.0.0', port=80, debug=False)