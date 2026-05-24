---
title: Hugging Face MLOps Pipeline
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "3.0"
python_version: "3.10"
app_file: app.py
pinned: false
---

# hugging-face-mlops-pipeline

This project provides a Hugging Face Spaces app for summarizing text using a transformer model through a Gradio interface.

## Project Goal

The goal is to demonstrate a simple MLOps pipeline by deploying an end-to-end summarization app on Hugging Face Spaces, including model inference and continuous syncing from the repository.

## Overview

This repository builds a text summarization application using Hugging Face Transformers and Gradio. The app is designed to be hosted as a Hugging Face Space and synchronizes repository updates via GitHub Actions.

## Features

- Summarizes text using a Hugging Face transformer model
- Provides a Gradio web interface for easy interaction
- Designed for deployment on Hugging Face Spaces
- Includes a GitHub Actions workflow for syncing the repository to the Space

## Project Structure

- `app.py` — main Gradio application
- `requirements.txt` — Python dependencies
- `.github/workflows/main.yml` — workflow configuration for syncing to Hugging Face
- `README.md` — Space metadata and project documentation

## Requirements

- Python 3.10 or higher
- `gradio`
- `transformers`
- `tensorflow`

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the app locally:

```bash
python app.py
```

Then open the local Gradio link shown in the terminal.

## Deployment to Hugging Face Spaces

1. Ensure `README.md` contains the Spaces front matter at the top.
2. Set the app entry file to `app.py`.
3. Configure `HF_TOKEN` as a GitHub secret if using workflow sync.
4. Push the repository to GitHub and allow the workflow to sync changes to the Space.

## Notes

- The app uses a transformer summarization pipeline, which may download models on first run.
- Verify the `app.py` import matches the installed package: `import gradio as gr`.
