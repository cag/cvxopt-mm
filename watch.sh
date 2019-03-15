#!/usr/bin/env bash
python app.py &
watchmedo shell-command -p '*.py' -c 'pkill -xf "python app.py"; python app.py'
