"""
transcript-digest
Programa principal per testejar diferents LLM i generar resums de videos
"""
import sys
import argparse

from modules.summarize import summarize

if __name__ == "__main__":

	parser = argparse.ArgumentParser(
		description="transcript-digest",
		formatter_class=argparse.RawTextHelpFormatter
	)

	parser.add_argument(
		"--prompt_file",
		type=str,
		required=True,
		help=(
				"prompt file."
		)
	)

	parser.add_argument(
		"--context_file",
		type=str,
		required=True,
		help=(
				"context file.\n"
				"Context of the video author\n"
		)
	)

	parser.add_argument(
		"--transcript_file",
		type=str,
		required=True,
		help=(
				"transcript file.\n"
				"Transcription of the video\n"
		)
	)

	parser.add_argument(
		"--api",
		type=str,
		required=True,
		choices=["openai", "anthropic", "xai", "deepseek", "gemini", "test"],
		help=(
				"IA API"
		)
	)

	parser.add_argument(
		"--audio",
		type=str,
		choices=["es", "ca", "en"],
		help=(
				"Audio generation via edge-tts"
		)
	)

	if len(sys.argv) == 1:
			parser.print_help()
			sys.exit(1)

	args = parser.parse_args()


	summarize(args.prompt_file, args.context_file, args.transcript_file, args.api, args.audio)
