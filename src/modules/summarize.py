"""function summarize()"""
import os
import subprocess

from dotenv import load_dotenv
from datetime import datetime

from modules.prompt import get_prompt
from modules.response_test import get_response_test
from modules.models import get_models
from modules.utils import clean_markdown
from modules.audio import generate_audio

def summarize(prompt_file: str, context_file: str, transcript_file: str, api: str, audio: str) -> None:
	"""
	Summarizes transcript_file asking to an LLM with a prompt.

	Arguments:
	-prompt_file (str)
	-context_file (str)
	-transcript_file (str)
	-api (str)
	-audio (str): language of the audio file (related with the language of the prompt)

	Returns:
	None
	"""
	load_dotenv()

	prompt = get_prompt(prompt_file, context_file, transcript_file)
	timestamp = datetime.now().strftime("%y%m%d_%H%M%S")

	print(f"======= {api} ================")

	client = None

	if api == "openai":
		# OpenAI
		try:

			api_key = os.getenv("OPENAI_API_KEY")
			if not api_key:
				raise ValueError(f"Falta la variable d'entorn de {api}")
			try:
				from openai import OpenAI
			except ImportError:
				raise ImportError(
					"Falta el paquet OpenAI"
				)

			client = OpenAI(api_key=api_key)
			response = client.chat.completions.create(
					model=get_models(api), # gpt-4o, gpt-4o-mini
					messages=[
							{"role": "user", "content": f"{prompt}"}
					]
			)

			content = response.choices[0].message.content

		except Exception as e:
			print(f"Error inesperat: {e}")
			content = None

	elif api == "anthropic":
		# Claude (Anthropic)
		try:
			api_key = os.getenv("ANTHROPIC_API_KEY")
			if not api_key:
				raise ValueError(f"Falta la variable d'entorn de {api}")
			try:
				from anthropic import Anthropic
			except ImportError:
				raise ImportError(
					"Falta el paquet Anthropic"
				)

			client = Anthropic(api_key=api_key)
			response = client.messages.create(
					model=get_models(api), # claude-opus-4-7
					max_tokens=2000,
					messages=[
							{"role": "user", "content": f"{prompt}"}
					]
			)

			content = response.content[0].text

		except Exception as e:
			print(f"Error inesperat: {e}")
			content = None

	elif api == "xai":
		# XAI (Grok)
		try:
			api_key = os.getenv("XAI_API_KEY")
			if not api_key:
				raise ValueError(f"Falta la variable d'entorn de {api}")
			try:
				from openai import OpenAI
			except ImportError:
				raise ImportError(
					"Falta el paquet OpenAI"
				)
			client = OpenAI(
					api_key=api_key,
					base_url="https://api.x.ai/v1"
			)

			response = client.chat.completions.create(
					model=get_models(api),
					messages=[
							{
									"role": "user",
									"content": f"{prompt}"
							}
					]
			)

			content = response.choices[0].message.content

		except Exception as e:
			print(f"Error inesperat: {e}")
			content = None

	elif api == "deepseek":
		# DeepSeek
		try:
			api_key = os.getenv("DEEPSEEK_API_KEY")
			if not api_key:
				raise ValueError(f"Falta la variable d'entorn de {api}")
			try:
				from openai import OpenAI
			except ImportError:
				raise ImportError(
					"Falta el paquet OpenAI"
				)

			client = OpenAI(
					api_key=api_key,
					base_url="https://api.deepseek.com"
			)

			response = client.chat.completions.create(
					model=get_models(api), # deepseek-reasoner
					messages=[
							{
									"role": "user",
									"content": f"{prompt}"
							}
					]
			)

			content = response.choices[0].message.content

		except Exception as e:
			print(f"Error inesperat: {e}")
			content = None

	elif api == "gemini":
		# Gemini
		try:
			api_key = os.getenv("GEMINI_API_KEY")
			if not api_key:
				raise ValueError(f"Falta la variable d'entorn de {api}")
			try:
				from google import genai
			except ImportError:
				raise ImportError(
					"Falta el paquet genai de Google Gemini"
				)

			client = genai.Client(api_key=api_key)

			response = client.models.generate_content(
				model=get_models(api),
				contents=prompt
			)
			content = response.text

		except Exception as e:
			print(f"Error inesperat: {e}")
			content = None

	else: # test

		content = get_response_test()

	# ------------------

	if content:
		with open(f"output/output_{timestamp}_{api}.md", "w", encoding="utf-8") as f:
			f.write(content)
		
		text = clean_markdown(content)
		print(text)

		with open(f"output/output_{timestamp}_{api}.txt", "w", encoding="utf-8") as f:
			f.write(text)

		# $ pandoc output_anthropic.md -o output_anthropic.pdf --template template.tex --pdf-engine xelatex
		subprocess.run(
				["/usr/bin/pandoc", f"output/output_{timestamp}_{api}.md", "-o", f"output/output_{timestamp}_{api}.pdf", "--template", "template.tex", "--pdf-engine", "xelatex"],
				check=True
		)

		if audio:
			print("\ngenerating mp3 audio file...")
			generate_audio(text, audio, f"output/output_{timestamp}_{api}.mp3")
