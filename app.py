from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

# Configure Gemini API key from environment variable
GENAI_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GENAI_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY environment variable not set. Please export your Gemini API key.")

genai.configure(api_key=GENAI_API_KEY)

# Initialize Gemini model (gemini-2.5-flash)
model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    """Serve the main page."""
    return render_template("index.html")


@app.route("/get_mood", methods=["POST"])
def get_mood():
    """Receive mood from client, call Gemini to generate a related quote and gif."""
    data = request.get_json(force=True)
    mood = data.get("mood", "happy")

    prompt = (
        "You are a helpful assistant. Return a JSON object with keys 'quote' and 'gif'. "
        "The 'quote' should be a short motivational or funny quote (<= 25 words) matching the mood. "
        "The 'gif' should be a direct HTTPS URL to a fun GIF representing the mood. "
        "Mood: " + mood + ". "
        "Respond ONLY with valid JSON."
    )

    try:
        response = model.generate_content(prompt)
        # The model may wrap JSON in markdown; attempt to extract JSON substring
        import json, re
        json_match = re.search(r"\{.*\}", response.text, re.DOTALL)
        if not json_match:
            raise ValueError("JSON not found in model response")
        payload = json.loads(json_match.group(0))
        quote = payload.get("quote", "Stay positive!")
        gif = payload.get("gif", "")
        return jsonify({"quote": quote, "gif": gif})
    except Exception as e:
        # Fallback in case of error
        return jsonify({
            "quote": "Keep smiling, it suits you!",
            "gif": "https://media.giphy.com/media/1BcfiGlOGXzQ0/giphy.gif",
            "error": str(e)
        }), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
