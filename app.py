from flask import Flask, request, jsonify, render_template
import os
from langchain_community.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
import constants
app = Flask(__name__)

# Initialize your chatbot components here
os.environ["OPENAI_API_KEY"] = constants.APIKEY


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # This function handles the logic for processing incoming POST requests to the '/chat' route.

    data = request.get_json()
    # In Flask, the 'request' object contains the incoming request data.
    # The 'get_json()' method is used to parse the request body as JSON data.

    query = data.get('query')
    # This line retrieves the value of the 'query' key from the JSON data received in the previous step.

    loader = DirectoryLoader(".", glob="*.txt")
    # This line creates a 'DirectoryLoader' object from the 'langchain' library.
    # The 'DirectoryLoader' is used to load text files from the current directory (".").
    # The 'glob="*.txt"' parameter specifies that only files with the '.txt' extension should be loaded.

    index = VectorstoreIndexCreator().from_loaders([loader])
    # This line creates a vector store index using the 'VectorstoreIndexCreator' from the 'langchain' library.
    # The 'from_loaders' method is used to create the index from the 'loader' objects passed as a list.
    # In this case, only one loader ('loader') is passed.

    answer = index.query(query, llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7))
    # This line queries the vector store index using the 'query' string.
    # The 'llm' parameter specifies the language model to use for generating the answer.
    # In this case, it's using the 'gpt-3.5-turbo' model from OpenAI's ChatGPT API.
    # The 'temperature' parameter controls the randomness of the generated text,
    # with a higher value producing more diverse and unpredictable responses.

    return jsonify({'answer': answer})
    # This line returns the generated answer as a JSON response.
    # The 'jsonify' function from Flask is used to convert the Python dictionary
    # {'answer': answer} into a JSON-formatted string,
    # which can be easily parsed by the client.

if __name__ == '__main__':
    app.run(debug=True)
