import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import uuid

# Load the pipeline
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1").to(device)

def generate_image(prompt):
    # Generate the image from the text prompt
    image = pipe(prompt).images[0]
    # Generate a unique filename
    unique_filename = f"generated_image_{uuid.uuid4().hex}.png"
    image_path = f"results/{unique_filename}"
    # Save the image to a file
    image.save(image_path)
    return unique_filename

