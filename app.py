import webbrowser
import os
from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
from generator import generate_image
import time

app = Flask(__name__)
current_prompt = None
generated_image = None
generated_description = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    global current_prompt, generated_image, generated_description

    action = request.form.get("action", None)
    new_prompt = request.form.get("prompt", None)

    if action == "Create New Image" and new_prompt:
        current_prompt = new_prompt
    elif action == "Regenerate" and current_prompt:
        pass  # Use the existing prompt
    else:
        current_prompt = new_prompt

    # Generate the image
    unique_image_name = generate_image(current_prompt)
    generated_description = f"Generated from prompt: '{current_prompt}'"
    image_path = url_for('static', filename=unique_image_name)

    # Log the image description and unique file name with timestamp
    log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {unique_image_name} - {generated_description}\n"
    with open("results\image_generation_log.txt", "a") as log_file:
        log_file.write(log_entry)

    return render_template("index.html", generated_image=image_path, generated_description=generated_description, current_prompt=current_prompt)

@app.context_processor
def inject_generated():
    return {
        "generated_image": generated_image,
        "generated_description": generated_description,
    }


def open_browser_with_delay(url, delay=10):
    # Add a delay before opening the URL in the default browser
    time.sleep(delay)
    # Open the URL in the default browser (only once)
    try:
        webbrowser.get().open(url, new=1)
    except webbrowser.Error:
        print(
            f"Unable to open the browser automatically. Please open {url} manually in your browser."
        )

if __name__ == "__main__":
    import sys

    # Default values for host and port
    host = "127.0.0.1"
    port = 5000

    # Check if host and port are provided as command line arguments
    if len(sys.argv) > 1:
        host = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])

    # Determine the URL to open
    url = f"http://{host}:{port}/"

    # Ensure the browser is opened only once
    if not os.getenv("WERKZEUG_RUN_MAIN"):  # Prevent re-execution in debug mode
        open_browser_with_delay(url)

    # Run the Flask application
    app.run(host=host, port=port, debug=True)
