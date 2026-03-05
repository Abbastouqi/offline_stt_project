import sounddevice as sd
import numpy as np
# Dot (.) hata kar absolute import use karein taake path ka masla na ho
from src.member_2_audio.config import SAMPLING_RATE, CHANNELS, DTYPE, CHUNK_SIZE

class AudioCapture: 
    def __init__(self, audio_queue):
        self.audio_queue = audio_queue
        self.stream = None

    def _callback(self, indata, frames, time, status):
        """Callback function called for every audio block"""
        if status:
            print(f"Stream Error: {status}")
        # Convert NumPy array to bytes and put in queue
        self.audio_queue.put(indata.copy().tobytes())

    def start_stream(self):
        """Initialize and start the microphone stream"""
        print(f"Microphone Started at {SAMPLING_RATE}Hz...")
        self.stream = sd.InputStream(
            samplerate=SAMPLING_RATE,
            channels=CHANNELS,
            dtype=DTYPE,
            blocksize=CHUNK_SIZE,
            callback=self._callback
        )
        self.stream.start()

    def stop_stream(self):
        """Stop and close the microphone stream"""
        if self.stream:
            self.stream.stop()
            self.stream.close()
            print("Microphone Stopped.")