#!/usr/bin/env bash
echo "cabin-iot-home -> run.sh"
echo "Activating venv..."
source ./.env
export PROJECT_DIR=$(git rev-parse --show-toplevel)
cd PROJECT_DIR
cd board
source venv/bin/activate
echo "Starting app..."
python app.py
