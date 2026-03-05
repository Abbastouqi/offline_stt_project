import unittest
import time
import sys
import os

# Path setup to find the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.member_2_audio.audio_queue import AudioQueue
from src.member_2_audio.audio_capture import AudioCapture

class TestAudioCapture(unittest.TestCase):
    
    def test_mic_fills_queue(self):  # Must start with 'test_'
        """Verifies that the microphone captures data and fills the queue"""
        q = AudioQueue()
        cap = AudioCapture(q)
        
        print("\n--- Testing Microphone (Please speak for 3 seconds) ---")
        cap.start_stream()
        time.sleep(3)
        cap.stop_stream()
        
        # Verify the queue is not empty after recording
        self.assertFalse(q.is_empty(), "Failed: No audio data was captured in the queue.")
        print(f"Success: Queue is not empty. Captured data found.")

if __name__ == "__main__":
    unittest.main()