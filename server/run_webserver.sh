#!/usr/bin/env bash
#source venv/bin/activate
#source ../.env
sanic web_server.app --host=0.0.0.0 --port=5000 --debug #--workers=4
