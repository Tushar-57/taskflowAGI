# CAMEL Agent Implementation with Local Models 🤖
Who likes to run out of tokens during a deep conversation with an LLM. 
This project extends and demonstrates how to implement CAMEL (Conversational Agents with Memory and Extensible Logic) using locally presented models to create agents with different personalities and specialized roles.

## 🌟 Overview
This implementation shows how to create a simple chat agent using the CAMEL framework, configured to work with local LLM models via Ollama/OpenAI/Claude/etc.

## 🌟 To run 'running_camel_with_local_model.py' agent workflow
Follow the installation


## 🛠️ Prerequisites & Installation 📦 
- Python 3.x
- CAMEL library (`pip install camel-ai`)
- download any model of your choice locally using the below command (assuming you already have Ollama installed)
``` bash 
    ollama run **llama3.2:3b** (replace with your model choice)
```

## 🚀 Features
- Uses local model inference and creating agentic workflow
- It implements a basic chat agent
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
2. Set up a helpful assistant with specific parameters and tone
3. Processes user messages and generates responses

## 🔧 Configuration
Current configuration includes:
- Model: Llama 3.2 3B
- Temperature: 0.4
- Token Limit: 4096
- Platform: Ollama
- No running out of tokens.


## 🤝 Contributing
Feel free to fork, modify, and experiment with the code. Contributions are welcome!

## 📄 License
This project is open-source and available under the MIT License.

