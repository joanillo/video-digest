"""funcions get_prompt()"""
from typing import List

def get_prompt(prompt_file: str, context_file: str, transcript_file: str) -> str:
	"""
	Genera i retorna un prompt que farem servir per analitzar les diferents APIs

	Arguments:
	-prompt_file (str)
	-context_file (str)
	-transcript_file (str)

	Returns:
	str: el prompt
	"""
	with open(prompt_file, "r", encoding="utf-8") as f:
			prompt = f.read()

	with open(context_file, "r", encoding="utf-8") as f:
			context = f.read()

	with open(transcript_file, "r", encoding="utf-8") as f:
			transcript = f.read()

	prompt = prompt.replace("{context}", context).replace("{transcript}", transcript)

	return prompt
