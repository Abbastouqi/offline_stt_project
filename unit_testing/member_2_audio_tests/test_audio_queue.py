import unittest
import sys
import os

# Adjust path to find the src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.member_2_audio.audio_queue import AudioQueue

class TestAudioQueue(unittest.TestCase):
    def setUp(self):
        self.audio_q = AudioQueue()

    def test_put_and_get(self):
        """Test if data can be added and retrieved"""
        test_data = b"test_pcm_data"
        self.audio_q.put(test_data)
        self.assertEqual(self.audio_q.get(), test_data)

    def test_empty_queue(self):
        """Test if getting from empty queue returns None"""
        self.assertIsNone(self.audio_q.get())

if __name__ == "__main__":
    unittest.main()