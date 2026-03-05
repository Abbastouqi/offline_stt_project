import wave
import time

class MockAudioInjector:
    def __init__(self, audio_queue):
        self.audio_queue = audio_queue

    def inject_file(self, file_path):
        """Simulates a microphone by feeding a WAV file into the queue"""
        print(f"Injecting mock audio from: {file_path}")
        try:
            with wave.open(file_path, 'rb') as wf:
                # Read 1024 frames at a time to match CHUNK_SIZE
                data = wf.readframes(1024)
                while data:
                    self.audio_queue.put(data)
                    data = wf.readframes(1024)
                    # Small sleep to simulate real-time recording speed
                    time.sleep(0.01) 
            print("Mock injection complete.")
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")