import os
from PIL import Image
import sys

def optimize_images(directory):
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    print(f"Scanning directory: {directory}")
    
    files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not files:
        print("No images found to optimize.")
        return

    print(f"Found {len(files)} images.")

    for filename in files:
        filepath = os.path.join(directory, filename)
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}.webp"
        new_filepath = os.path.join(directory, new_filename)
        
        print(f"Processing: {filename} -> {new_filename}")
        
        try:
            with Image.open(filepath) as img:
                # Convert to RGB if necessary (e.g. for PNGs with transparency if saving as JPG, but WebP handles RGBA)
                # WebP supports transparency, so we can keep RGBA if present.
                
                # Resize if incredibly large (optional, but good for that 4.8MB file)
                # Let's say max width 1920 for web generally, unless it's a specific large asset.
                # However, preserving quality is key. Let's just compress first.
                
                img.save(new_filepath, 'WEBP', quality=80)
                print(f"Saved: {new_filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    target_dir = "assets/images"
    optimize_images(target_dir)
