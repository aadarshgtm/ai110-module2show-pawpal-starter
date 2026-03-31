#!/bin/bash

# PawPal+ Run Script
# This script activates the virtual environment and runs the Streamlit app

echo "🐾 Starting PawPal+..."

# Navigate to the project directory
cd "/Users/kaivalya/Desktop/codepath/Assignment 2 AI 110/ai110-module2show-pawpal-starter"

# Activate the virtual environment
source ../venv/bin/activate

# Run the Streamlit app
echo "🚀 Launching Streamlit app..."
streamlit run app.py