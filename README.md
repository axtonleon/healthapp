# Health App

A comprehensive health-focused application built with Flask, leveraging natural language processing and AI-powered chat functionality.

## Features

- **Flask-based Backend**: Utilizes Flask to create a robust RESTful API for handling HTTP requests and serving responses.
- **Natural Language Processing**: Implements advanced NLP capabilities using LangChain libraries to process and analyze user queries.
- **AI-Powered Chat**: Integrates OpenAI's ChatGPT API to provide intelligent, conversational responses to user inquiries.
- **File-based Data Loading**: Employs DirectoryLoader to load relevant health-related text files from local directories.
- **Vector Store Indexing**: Utilizes VectorstoreIndexCreator to efficiently index and search through large datasets.
- **Error Handling**: Implements custom error handlers for 404 and 500 errors, enhancing user experience and debugging capabilities.

## Key Components

- **App Initialization**: Sets up the Flask application and configures environment variables for API keys.
- **Route Handlers**: Defines routes for the main page and chat functionality.
- **Request Processing**: Parses incoming JSON data and extracts user queries.
- **Query Execution**: Uses the VectorstoreIndexCreator to generate responses based on user input.
- **Response Formatting**: Returns JSON-formatted responses for easy parsing by clients.

## Technologies Used

- Flask: Web framework for building the backend
- LangChain: Library for natural language processing and indexing
- OpenAI: Provides AI models for chat functionality
- Python: Core programming language

This project demonstrates how to combine Flask, LangChain, and OpenAI APIs to create a powerful, AI-driven health application. It showcases best practices in error handling, efficient data processing, and seamless integration of various technologies to build a robust solution.
