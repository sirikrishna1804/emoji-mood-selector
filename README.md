# Emoji Mood Selector 🎉

A simple Flask web app using **Gemini 2.5-Flash** (via `google-generativeai`) to return a fun quote or GIF based on your selected mood.

## Features
* Choose from **happy**, **sad**, or **angry** moods.
* Gemini generates a short quote and a GIF URL that matches the mood.
* Responsive UI built with vanilla HTML/CSS/JS.

## Setup
1. **Clone repository** (or copy files).
2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure API key**
   Save your Gemini API key in an environment variable called `GOOGLE_API_KEY`.
   On Windows (PowerShell):
   ```powershell
   setx GOOGLE_API_KEY "YOUR_API_KEY"
   $Env:GOOGLE_API_KEY="YOUR_API_KEY"  # For current session
   ```
   On macOS / Linux (bash/zsh):
   ```bash
   export GOOGLE_API_KEY="YOUR_API_KEY"
   ```
5. **Run app**
   ```bash
   python app.py
   ```
   Visit `http://localhost:5000` in your browser.

## Folder structure
```
app.py                # Flask backend
requirements.txt      # Python deps
README.md             # This file
/static/
    style.css         # Styles
    main.js           # Front-end JS
/templates/
    index.html        # Front-end HTML
```

## Notes
* If Gemini returns no GIF URL, a default fallback GIF is shown.
* For production deployment, disable `debug=True` in `app.py`.
