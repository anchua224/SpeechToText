# Speech To Text

## Description
Due to the problems encountered using the previous STT program, we opted to develop a new program using new Python libraries that have developed in the recent years. We decided to use the OpenAI Whisper library, which is a speech-recognition library whose open-source models are trained on thousands of hours of multi-lingual data. The library offers the ability to transcribe text from audio, as well as translate transcriptions into other languages. More information about Whisper can be found on [OpenAI](https://openai.com/research/whisper).

## Requirements

This program currently uses Python version 3.10.4.

The library requirements needed for this python program are in requirements.txt. To install these libraries, use the following command:
```bash
$ pip install -r requirements.txt
```
The whisper library must be installed specifically from the OpenAI Whisper Git repository. This is specified in requirements.txt.

## Usage
Pass the file path for the audio file though the command line. 
```bash
$ python stt.py path/to/audiofile
```
The generated text transcriptions are sent to /text.

## Contributing Authors
Lehigh - Fall 2023
* Ala Chua (anc224@lehigh.edu)
* Jie Yao (jiy921@lehigh.edu)
* Chris Wells (czw224@lehigh.edu)
* Brad Keiser (bdk223@lehigh.edu)
