# lpcb2
language de programmation
# LPCB Chatbot Project

This project is designed to create a chatbot using the LPCB programming language. It includes the core algorithm, conversation modules, and package information necessary for the chatbot's operation.

## Project Structure

- **algorithme/**
  - `main.lpcb`: Contains the main algorithm for the chatbot, defining the core logic and flow of the conversation.
  - `tokenizer.lpcb`: Tokenizes the input text.
  - `parser.lpcb`: Parses the tokenized text.
  - `syntax_analyzer.lpcb`: Analyzes the syntax of the parsed text.
  - `semantic_analyzer.lpcb`: Analyzes the semantics of the parsed text.
  
- **conversation_en_module/**
  - `greetings.lpcb`: Handles greeting conversations.
  - `small_talk.lpcb`: Handles small talk conversations.
  - `intent_recognition.lpcb`: Recognizes the intent of the user's input.
  - `response_generation.lpcb`: Generates responses based on the recognized intent.
  - `capabilities.lpcb`: Describes the capabilities of the chatbot.
  
- **package/**
  - `packages.lpcb`: Lists the required packages.
  - `install.lpcb`: Script to install the required packages.
  - `config.lpcb`: Configuration settings for the chatbot.

- **tests/**
  - `test.lpcb`: A simple test file for the LPCB interpreter.
  - `import_re.py`: A Python script to interpret LPCB files.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Ensure you have Python installed.
4. Run the main algorithm using the command:
   ```bash
   python lpcb_interpreter.py algorithme/main.lpcb
