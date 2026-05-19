"""audio functions"""
import asyncio
import edge_tts

def generate_audio(text: str, audio: str, file: str) -> None:
	"""
	Genera el mp3 amb l'idioma especificat.

	Arguments:
	-text (str): text content
	-audio (str): idioma (es, ca, en)
	-file (str): audio filename (mp3)

	Returns:
	None
	"""

	async def generar_tts(text, lang, output_file):
			voice = VOICES[lang]

			communicate = edge_tts.Communicate(
					text=text,
					voice=voice
			)

			await communicate.save(output_file)

	VOICES = {
			"ca": "ca-ES-EnricNeural",
			"es": "es-ES-AlvaroNeural",
			"en": "en-GB-RyanNeural",
	}

	asyncio.run(
			generar_tts(
					text=text,
					lang=audio,
					output_file=file
			)
	)