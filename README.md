# AI Text-to-Image Generator

This project is a web application that generates images based on text prompts using a pre-trained Stable Diffusion model. The application allows users to enter a text prompt, generate an image based on the prompt, regenerate the image, or create a new image with a different prompt. Each generated image is saved with a unique filename, and logs are maintained for image generation activities.

## Features

- Generate images from text prompts using a pre-trained Stable Diffusion model.
- Display the generated image along with the text prompt.
- Regenerate the image using the same text prompt.
- Create a new image with a different text prompt.
- Disable buttons during image generation to prevent multiple submissions.
- Log image descriptions, unique filenames, and generation timestamps.

## Requirements

- Python 3.7 or higher
- Flask
- Torch
- Diffusers
- PIL (Pillow)
- Transformers
- Accelerate

## Installation and USage

1. Clone the repository

```bash
git clone {repository url}
```
2. Create a virtual environment and activate it:

```bash
python -m venv myenv
source myenv/Scripts/Activate
```
3. Install the required packages:

```bash
pip install -r requirements.txt
```
4. Run the Application:

```bash
python app.py
```
5. The browser will automatically be opened in a minute.

6. Enter a text prompt in the input field and click the "Generate Image" button.

7. Wait for the image to be generated and displayed below the input field.

8. Use the "Regenerate" button to generate the image again with the same prompt, or use the "Create New Image" button to generate a new image with a different prompt.

9. The genereated image will automatically be stored in the 'results' folder. The Unique file name along with the image description and generation timestamp will be recorded in the 'image_generation_log.txt' file.

## Project Structure

- app.py: The main Flask application file that handles routing and image generation.

- generator.py: Contains the function to generate images using the Stable Diffusion model.

-templates/index.html: The HTML template for the web application.

- static/styles.css: The CSS file for styling the web application.

- requirements.txt: The list of required Python packages.

- results/image_generation_log.txt: The log file that records image generation activities.


## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- Stable Diffusion for the pre-trained model.
- Flask for the web framework.
- Torch and Diffusers for the deep learning libraries.
- PIL (Pillow) for image processing.