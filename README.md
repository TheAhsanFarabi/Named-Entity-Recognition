# Named Entity Recognition (NER) Web Application

This project is a simple web application for Named Entity Recognition (NER) using Flask and spaCy. It allows users to input text and get recognized entities such as persons, organizations, and locations highlighted.

## Features

- User-friendly web interface for text input and entity visualization.
- Uses spaCy's pre-trained NER model to identify entities.
- Supports multiple entity types including PERSON, ORG, GPE, and more.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/Named-Entity-Recognition.git
    cd Named-Entity-Recognition
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install flask spacy
    python -m spacy download en_core_web_lg
    ```

## Usage

1. **Run the Flask application**:
    ```sh
    python app.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000/`.

3. **Enter text** in the text area and click "Analyze" to see the recognized entities.

## Technologies

- **Python**: Programming language
- **Flask**: Web framework for Python
- **spaCy**: NLP library for Python
- **HTML/CSS**: Frontend technologies

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## Acknowledgements

- Thanks to the [spaCy](https://spacy.io/) team for their excellent NLP library.
- Thanks to the [Flask](https://flask.palletsprojects.com/) team for their lightweight web framework.

