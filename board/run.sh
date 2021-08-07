#!/usr/bin/env bash
echo "cabin-iot-home -> board -> run"
echo "Activating venv..."
source venv/bin/activate
echo "Starting app..."
python app.py
