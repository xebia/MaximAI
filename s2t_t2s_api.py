from fastapi import FastAPI, UploadFile, File, Response
from google.cloud import speech as speech, texttospeech
# from google.cloud.speech import enums
from google.cloud.speech import types

app = FastAPI()
speech_client = speech.SpeechClient()
tts_client = texttospeech.TextToSpeechClient()

@app.post("/transcribe/")
async def transcribe_and_synthesize_audio(file: UploadFile = File(...)):
    content = await file.read()
    audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        # encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        # sample_rate_hertz=16000,
        # language_code='en-US'
    )

    response = speech_client.recognize(config=config, audio=audio)

    transcriptions = []
    for result in response.results:
        transcriptions.append(result.alternatives[0].transcript)

    text = " ".join(transcriptions)

    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

    response = tts_client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    return Response(content=response.audio_content, media_type="audio/wav")
