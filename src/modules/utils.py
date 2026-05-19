"""util funcions"""
import re

def clean_markdown(text):
	"""
	cleans markdown format to plain text

	Arguments:
	-text (str): text in markdown format

	Returns:
	plain text (str)
	"""
	# Elimina blocs de codi ```...```
	text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

	# Elimina codi inline `...`
	text = re.sub(r"`([^`]*)`", r"\1", text)

	# Links [text](url) -> text
	text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)

	# Imatges ![alt](url) -> alt
	text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)

	# Negreta i cursiva
	text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
	text = re.sub(r"\*(.*?)\*", r"\1", text)
	text = re.sub(r"__(.*?)__", r"\1", text)
	text = re.sub(r"_(.*?)_", r"\1", text)

	# Headers (# Títol -> Títol)
	text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)

	# Blockquotes
	text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)

	# Llistes (- item, * item)
	text = re.sub(r"^[\-\*\+]\s+", "", text, flags=re.MULTILINE)

	# Numeració (1. item)
	text = re.sub(r"^\d+\.\s+", "", text, flags=re.MULTILINE)

	# Línies horitzontals --- ***
	text = re.sub(r"^[-*_]{3,}$", "", text, flags=re.MULTILINE)

	# Espais múltiples
	text = re.sub(r"\n\s*\n", "\n\n", text)
	text = re.sub(r"[ \t]+", " ", text)

	return text.strip()