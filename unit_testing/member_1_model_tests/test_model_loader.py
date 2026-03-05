import json
import unittest
import sys
import os

# Path setup
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.member_1_model.model_loader import ModelLoader

class TestModelLoader(unittest.TestCase):

    def test_model_loading(self):
        # Config path fix
        config_path = os.path.join(os.getcwd(), "config", "config.json") 
        
        with open(config_path, "r") as f:
            config = json.load(f)

        loader = ModelLoader()
        result = loader.loadModel(config) 
        self.assertTrue(result, "Model load nahi ho saka!")

    def test_transcription(self):
        loader = ModelLoader()
        # Pehle model load karein
        loader.loadModel({"model_name": "base", "language": "ur"})
        model = loader.model 

        # --- Dono Files ki List ---
        audio_files = ["sample_ur_01.wav", "sample_ur_02.wav"]
        base_path = os.path.join("unit_testing", "member_1_model_tests", "benchmark_audio")

        for file_name in audio_files:
            audio_path = os.path.join(base_path, file_name)
            
            if not os.path.exists(audio_path):
                print(f"\n[!] Error: {file_name} nahi mili!")
                continue

            print(f"\n======================================")
            print(f" TESTING FILE: {file_name} ")
            print(f"======================================")

            # Urdu Transcription
            print("\n--- Urdu Result ---")
            res_ur = model.transcribe(audio_path)
            print(res_ur["text"])
            
            # English Translation
            print("\n--- English Translation ---")
            res_en = model.transcribe(audio_path, task="translate")
            print(res_en["text"])

            self.assertIsNotNone(res_ur["text"])

if __name__ == "__main__":
    unittest.main()