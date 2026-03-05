import json
import wave

from src.member_1_model.model_loader import ModelLoader


with open("config/model_config.json") as f:
    config = json.load(f)


loader = ModelLoader()

loader.loadModel(config)


audio_file = "unit_testing/member_1_model_tests/benchmark_audio/sample_ur_01.wav"

wf = wave.open(audio_file, "rb")

while True:

    data = wf.readframes(4000)

    if len(data) == 0:
        break

    result = loader.recognize(data)

    if result["final"]:
        print("Recognized:", result["final"])