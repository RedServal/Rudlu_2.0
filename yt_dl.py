from pytube import YouTube
from pydub import AudioSegment

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

def nightcore(path, spood=2.0) :
    yt = YouTube(path)
    yt.streams.filter(type='audio').order_by('abr')[-1].download(filename='audio')
    sound = AudioSegment.from_file("audio.webm")
    speed_change(sound, speed=spood).export('audio_' + str(spood) + '.mp3', format="mp3")
