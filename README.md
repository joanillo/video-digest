# video-digest

Summarize videos with AI (generates txt, md and pdf). Export the summary to mp3 audio file.
We made this project thinking in video summarization, but you can summarize any text file. In this case, a prompt example file is provided in *input/* folder.

## Getting Started

1. Clone the repository to you local machine:

```bash
git clone https://github.com/joanillo/video-digest.git
```

2. Change to the project folder:

```bash
cd video-digest
```

3. Create a virtual environment to execute the project:

```bash
python -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
(venv) $ pip install -r requirements.txt
```

This project uses **pandoc** app in order to convert markdown files to pdf. In this case we dont't use de related python library (*pypandoc*). In a Linux machine:

```bash
sudo apt install pandoc
sudo apt install texlive-latex-base
sudo apt install texlive-latex-recommended texlive-fonts-recommended
```

You can test that pandoc works as expected:

```bash
$ pandoc document.md -o document.pdf
```


5. Configuring the API KEYs. You should put your api keys in a hidden file *.env*:

```bash
OPENAI_API_KEY=sk-proj-...
ANTHROPIC_API_KEY=sk-ant-...
DEEPSEEK_API_KEY=sk-...
XAI_API_KEY=xai-...
GEMINI_API_KEY=...
```

6. Execution of the project:

```bash
$ python main.py --help
```

```
$ python main.py --prompt_file=input/prompt_en.txt --context_file=input/context_file_en.txt --transcript_file=input/transcript_video.txt --api=openai --audio=en
```

If you don't specify *--audio* argument, the mp3 is not generatd. You can use *en* (English), *ca* (Catalan) or *es* (Spanish), but you can extend languages esasily changing the source code.
We use *edge-tts* to genertate the audio file.

## Projecte structure

This project has the following structure:

- `src/`: source code
    - `main.py`: main script and starting poing
    - `modules/`: functionalities
    - `modules/audio.py`
    - `modules/models.py`: definition of the several LLM models
    - `modules/prompt.py`: generates the prompt that we send to the LLM.
    - `modules/response_test.py`: test mode in development phase (doesn't consume tokens)
    - `modules/summarize.py`: logic to summarize the video transcriptions.
    - `modules/utils.py`: 
    - `input/`: input files (transcription files, context files, prompt model files)
    - `output/`: output files (content of the summary): text, markdown and pdf summary, mp3 audio file. 
- `doc/`: documentation
- `requirements.txt`: A text file specifying the Python dependencies required for the project.
- `README.md`: This file, providing an overview of the repository and instructions for usage.
- `LICENSE`

## Results

We provide the result to summarize this [youtube video](https://www.youtube.com/watch?v=WAXV41-WmLQ&t=615s).
You can see in the *output/* folder the achieved results.

## License

The code in this repository is licensed under the GNU GENERAL PUBLIC LICENSE. Feel free to use and modify the code for your own purposes.

