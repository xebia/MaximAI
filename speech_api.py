from fastapi import FastAPI, UploadFile, File, Response
from google.cloud import speech, texttospeech
from google.cloud.speech_v1 import enums as speech_enums
from google.cloud.texttospeech_v1 import enums as tts_enums
from google.cloud.speech_v1 import types as speech_types
from google.cloud.texttospeech_v1 import types as tts_types

app = FastAPI()
speech_client = speech.SpeechClient()
tts_client = texttospeech.TextToSpeechClient()

@app.post("/transcribe-and-synthesize/")
async def transcribe_and_synthesize_audio(file: UploadFile = File(...)):
    content = await file.read()
    audio = speech_types.RecognitionAudio(content=content)

    config = speech_types.RecognitionConfig(
        encoding=speech_enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US'
    )

    speech_response = speech_client.recognize(config=config, audio=audio)

    transcriptions = []
    for result in speech_response.results:
        transcriptions.append(result.alternatives[0].transcript)

    text = " ".join(transcriptions)

    synthesis_input = tts_types.SynthesisInput(text=text)
    voice = tts_types.VoiceSelectionParams(
        language_code="en-US", ssml_gender=tts_enums.SsmlVoiceGender.NEUTRAL
    )
    audio_config = tts_types.AudioConfig(audio_encoding=tts_enums.AudioEncoding.LINEAR16)

    tts_response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    return Response(content=tts_response.audio_content, media_type="audio/wav")