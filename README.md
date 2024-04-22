---
title: text_summarization
app_file: app.py
sdk: gradio
sdk_version: 3.50.2
---
# Text Summarization Project

This project aims to summarize the given text.
It's hosted on HuggingFace Spaces - [Live Demo](https://huggingface.co/spaces/SanskarModi/text_summarization)

### Tools and Technologies used :
 - PyTorch 
 - HuggingFaces
 - Gradio
 - DVC
 - Azure Blob Storage

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Structure

The project follows a modular structure for better organization and maintainability. Here's an overview of the directory structure:

- `.github/workflows`: GitHub Actions workflows for CI/CD.
- `src/`: Source code directory.
  - `textSummarizer/`
    - `components/`: Modules for different stages of the pipeline.
    - `utils/`: Utility functions.
    - `config/`: Configuration settings.
    - `pipeline/`: Scripts for pipeline stages.
    - `entity/`: Data entity classes.
    - `constants/`: Constants used throughout the project.
- `config/`: Configuration files.
- `colab_notebooks/`: Jupyter notebooks for trials, testing and training on colab or kaggle.
- `app.py`: Gradio Application.
- `requirements.txt`: Project dependencies.
- `setup.py`: Setup script for installing the project.
- `main.py`: Main script for execution.

## Setup

To set up the project environment, follow these steps:

1. Clone this repository.
2. Install Python 3.8 and ensure pip is installed.
3. Uncomment the last line in requirements.txt containing `. e` and save changes.
4. Install project dependencies using `pip install -r requirements.txt`.

## Usage

#### Data Ingestion , Data Transformation , Model Traininig and Model Evaluation

To run the complete pipeline, run:

```bash
python main.py
```

### To start the Gradio Application :

```bash
python app.py
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

Please ensure that your contributions adhere to the project's coding standards and guidelines.