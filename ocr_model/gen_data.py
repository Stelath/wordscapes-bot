import os
import random
import numpy as np
import argparse
from tqdm.auto import tqdm
from PIL import Image, ImageDraw, ImageFont

def main(output_dir, noise_level, noise_variance, num_images_per_character):
    # Define the path to the system font
    font_path = "/System/Library/Fonts/Supplemental/KeepCalm-Medium.ttf"

    # Define the characters to generate
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load the font
    font_size = 64
    font = ImageFont.truetype(font_path, font_size)

    # Generate the images
    for character in tqdm(characters, desc="Generating images"):
        os.makedirs(os.path.join(output_dir, character), exist_ok=True)
        for i in tqdm(range(num_images_per_character), desc=f"Character: {character}"):
            # Choose a random noise level
            cur_noise_level = np.clip(np.random.normal(loc=noise_level, scale=noise_variance), 0, 1)
            
            # Create a blank image
            image = Image.new("L", (font_size, font_size), 255)
            draw = ImageDraw.Draw(image)

            # Draw the character on the image
            offset = tuple(np.random.randint(low=-5, high=20, size=2))
            draw.text(offset, character, font=font, fill=0)

            # Add noise to the image
            pixels = np.array(image, dtype=np.int16)
            noise = np.random.choice([255, 0], size=pixels.shape, p=[cur_noise_level, 1 - cur_noise_level])
            
            noisy_pixels = np.clip(pixels + noise, 0, 255)
            noisy_image = Image.fromarray(noisy_pixels.astype(np.uint8))

            # Save the image
            noisy_image.save(os.path.join(output_dir, character, f"{i:05}.png"))

    print("Dataset generation complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output-dir", default='data/', help="Output directory")
    parser.add_argument("-n", "--noise-level", type=float, default=0.05, help="Noise level")
    parser.add_argument('-nv', '--noise-variance', type=float, default=0.05, help="Noise variance")
    parser.add_argument('-np', '--num-images-per-character', type=int, default=1000, help="Number of images to generate for each character")
    args = parser.parse_args()

    main(args.output_dir, args.noise_level, args.noise_variance, args.num_images_per_character)
