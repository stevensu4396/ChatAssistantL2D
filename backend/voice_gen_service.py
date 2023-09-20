import whisper
voice_model = whisper.load_model("base")


def tts():
    result = voice_model.transcribe("recorder.mp3")
    print(result)
    return result["text"]