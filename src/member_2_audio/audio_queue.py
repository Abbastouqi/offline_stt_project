import queue

class AudioQueue:
    def __init__(self):
        self._queue = queue.Queue()

    def put(self, audio_chunk):
        """Add audio data to the queue (Producer)"""
        self._queue.put(audio_chunk)

    def get(self):
        """Retrieve audio data from the queue (Consumer)"""
        try:
            return self._queue.get(block=False)
        except queue.Empty:
            return None

    def is_empty(self):
        """Check if the queue has no data"""
        return self._queue.empty()