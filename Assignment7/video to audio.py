from moviepy import editor
video = editor.VideoFileClip('Garsha-Rezaei-Sharm.mp4')
video.audio.write_audiofile('Garsha-Rezaei-Sharm.mp3')  