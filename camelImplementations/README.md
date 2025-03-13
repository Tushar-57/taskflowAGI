# CAMEL Agent Implementation with Local Models 🤖
Since you would not like to run out of tokens, so this project extends and demonstrates how to implement CAMEL (Conversational Agents with Memory and Extensible Logic) using local models through local present LLMs.

## 🌟 Overview
This implementation shows how to create a simple chat agent using the CAMEL framework, configured to work with local LLM models via Ollama/OpenAI/Claude/etc.

## 🛠️ Prerequisites & Installation 📦 
- Python 3.x
- CAMEL library (`pip install camel-ai`)
- download any model of your choice locally
- ```bash 
    ollama run **llama3.2:3b** (replace with your model choice)
```

## 🚀 Features
- Uses local model inference and creating agentic workflow
- Implements a basic chat agent
- Configurable temperature and token limits
- Simple message handling system

## 💻 Code Example
The main script demonstrates:
- Setting up a CAMEL chat agent
- Configuring model parameters
- Creating and handling messages
- Getting responses from the agent

## 🔍 Usage
The code creates a chat agent that:
1. Initializes a local Llama 3.2 3B model through Ollama
2. Sets up a helpful assistant with specific parameters
3. Processes user messages and generates responses

## 🔧 Configuration
Current configuration includes:
- Model: Llama 3.2 3B
- Temperature: 0.4
- Token Limit: 4096
- Platform: Ollama

CAMEL allows you to create agents with different personalities and specialized roles. 

## 🤝 Contributing
Feel free to fork, modify, and experiment with the code. Contributions are welcome!

## 📄 License
This project is open-source and available under the MIT License.

