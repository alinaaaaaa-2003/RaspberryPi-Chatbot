# RaspberryPi-Chatbot
## Overview
**Raspberry Pi AI Chatbot** is a voice-enabled question-answering system designed to run on Raspberry Pi devices. Powered by the **FLAN-T5 base model** from Hugging Face, this AI chatbot can understand spoken questions and provide full-sentence answers using text-to-speech output. It is optimized to integrate with drone or aviation technologies, allowing for hands-free, interactive AI responses in real-time.

## Features
- **Voice Recognition**: Uses the microphone to listen to spoken questions.
- **Natural Language Answers**: Generates full, contextual answers using a state-of-the-art T5 transformer model.
- **Text-to-Speech Output**: Responds audibly through speakers or Bluetooth headphones.
- **Cross-Platform Audio Support**: Works with any audio device connected to the Raspberry Pi.
- **Stop/Exit Command**: Say "stop", "exit", or "quit" to end the session safely.
- **Lightweight & Raspberry Pi Compatible**: Optimized to run efficiently on Raspberry Pi CPU.

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/alinaaaaaa-2003/RaspberryPi-Chatbot.git
cd RaspberryPi-Chatbot

## Set up Python environment

```bash
python3 -m venv venv
# Activate virtual environment
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

#Install Dependencies

pip install -r requirements.txt

## Usage

1. Run the main script.
2. The chatbot will start listening.
3. Ask a question aloud.
4. The AI will respond both in the console and via audio.
5. Say "stop", "exit", or "quit" to terminate the program.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
