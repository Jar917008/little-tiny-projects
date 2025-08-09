import pyaudio
import wave
   
from pydub import AudioSegment

from pynput.keyboard import Key, Controller
import keyboard
         



while True:
 CHUNK=1024
 FORMAT=pyaudio.paInt16
 CHANNELS=1
 RATE=44100
 p=pyaudio.PyAudio()
 stream=p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
 print("start ")
 frames=[]
 seconds=1

 for i in range(0,int(RATE/CHUNK*seconds)):
      data=stream.read(CHUNK)
      frames.append(data)


 print("stop")

 stream.stop_stream()
 stream.close()
 p.terminate()

 wf=wave.open("output.wav",'wb')
 wf.setnchannels(CHANNELS)
 wf.setsampwidth(p.get_sample_size(FORMAT))
 wf.setframerate(RATE)
 wf.writeframes(b''.join(frames))
 wf.close()

 audio=AudioSegment.from_file("output.wav", format="wav")
 print (audio[100:800].dBFS)

 keyboard_controller = Controller()


 if audio.dBFS > -60:
      print("pressing button")
      
      keyboard_controller.press(Key.space)
      keyboard_controller.release(Key.space) 

 if keyboard.is_pressed("p"):
     break
     