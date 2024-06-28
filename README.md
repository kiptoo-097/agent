# Text Processor

This Django project allows users to upload documents and uses OpenAI's GPT-3.5-turbo model to generate summaries, extract key points, and create a thesis for the uploaded text.

## Features

- Upload documents
- Summarize text
- Extract key points
- Generate thesis

## Prerequisites

- Python 3.8+
- Django 3.2+
- pip (Python package installer)
- OpenAI API key

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/kiptoo-097/agent.git
    cd text-processor
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    venv\Scripts\activate`
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**

    Create a `.env` file in the root directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your-openai-api-key
    ```

5. **Apply migrations**

    ```bash
    python manage.py migrate
    ```

6. **Run the server**

    ```bash
    python manage.py runserver
    ```

## Usage

1. **Access the API**

    Open your browser and go to `http://127.0.0.1:8000/api/documents/` to access the document upload API.



## License

This project is licensed under the MIT License. See the LICENSE file for details.
