from fastapi import FastAPI, UploadFile, File, Response

from maximai.context import get_full_patient_context
from maximai.langchain import create_context_aware_chatbot
from maximai.schemas import Prompt
from maximai.text_processing import transform_numbers_to_text

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

# from fastapi import FastAPI, Response
from google.cloud import texttospeech

app = FastAPI(title="MaximAI Chat App")

# et_debug(True)

chatbot = create_context_aware_chatbot()


# Define a route to handle API calls
@app.post("/chat")
async def root(prompt: Prompt):
    context = get_full_patient_context(prompt.user_id)
    print(context)
    output = chatbot.invoke(
        {"input": prompt.text, "context": context},
        config={"configurable": {"user_id": prompt.user_id}},
    )
    # output = output["content"]
    return {
        "input_message": prompt.text,
        "output_message": transform_numbers_to_text(output.content), # TODO transform "8" into eight
        "user_id": prompt.user_id,
    }

@app.post("/audio")
async def audio(file: UploadFile = File(...)):
    client = SpeechClient()
    model="latest_long"
    project_id="qwiklabs-gcp-02-c86bd22dbd03"

    content = await file.read()

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        language_codes=["en-US"],
        model=model,
    )

    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{project_id}/locations/global/recognizers/_",
        config=config,
        content=content,
    )

    # Transcribes the audio into text
    response = client.recognize(request=request)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

    # TODO: pass transcript to langchain
    chain_output = root(result.alternatives[0].transcript)
    print(f"chain_output: {chain_output}")

    # TODO: pass output of langchain 
    # chain_output["output_message"]

    return {
        "text": result.alternatives[0].transcript
    }


@app.post("/text_audio")
async def text_audio(prompt: Prompt):
    context = get_full_patient_context(prompt.user_id)
    print(context)
    output = chatbot.invoke(
        {"input": prompt.text, "context": context},
        config={"configurable": {"user_id": prompt.user_id}},
    )

    text = transform_numbers_to_text(output.content)

    # return {
    #     "input_message": prompt.text,
    #     "output_message": transform_numbers_to_text(output.content), # TODO transform "8" into eight
    #     "user_id": prompt.user_id,
    # }

    ##################
    # text to speech #
    ##################

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Set the content type of the response to audio/mpeg
    headers = {
        "Content-Disposition": "attachment; filename=output.mp3",
        "Content-Type": "audio/mpeg",
    }


    return Response(content=response.audio_content, media_type="audio/mpeg", headers=headers)



@app.get("/synthesize_audio")
async def synthesize_audio():
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text="Hello, World!")

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # Set the content type of the response to audio/mpeg
    headers = {
        "Content-Disposition": "attachment; filename=output.mp3",
        "Content-Type": "audio/mpeg",
    }

    # Return the audio content as a response
    return Response(content=response.audio_content, media_type="audio/mpeg", headers=headers)