from flask import Flask, render_template, request, redirect, url_for
import os
import pygame
from flask import Flask, request, jsonify, render_template_string
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
app = Flask(__name__)

def get_audio_endpoint_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    return cast(interface, POINTER(IAudioEndpointVolume))
# Set up the music directory
music_directory = "music"

# Get the list of music files
music_files = os.listdir(music_directory)

# Set up the Pygame mixer
pygame.mixer.init()


@app.route('/')
def index():
    return render_template('index.html', music_files=music_files)


@app.route('/play')
def play():
    # Get the name of the selected track from the request
    track_name = request.args.get('track')

    # Load and play the selected track
    pygame.mixer.music.load(os.path.join(music_directory, track_name))
    pygame.mixer.music.play()

    return f"Now playing: {track_name}"


@app.route('/stop')
def stop():
    # Stop the music
    pygame.mixer.music.stop()

    return "Music stopped."


@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file
    uploaded_file = request.files['file']

    # Save the file to the music directory
    uploaded_file.save(os.path.join(music_directory, uploaded_file.filename))

    # Reload the list of music files
    global music_files
    music_files = os.listdir(music_directory)

    # Redirect to the index page
    return redirect(url_for('index'))
@app.route('/volume', methods=['GET', 'POST'])




def volume():
    volume_control = get_audio_endpoint_volume()
    if request.method == 'POST':
        try:
            new_volume = float(request.form.get('volume'))
            if 0 <= new_volume <= 100:
                volume_control.SetMasterVolumeLevelScalar(new_volume / 100, None)
                return jsonify(success=True, volume=new_volume)
            else:
                return jsonify(success=False, error='Invalid volume level')
        except (ValueError, TypeError):
            return jsonify(success=False, error='Invalid volume value')
    else:
        current_volume = volume_control.GetMasterVolumeLevelScalar() * 100
        return jsonify(success=True, volume=current_volume)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
