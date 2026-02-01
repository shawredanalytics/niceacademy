import zipfile
import os
import xml.etree.ElementTree as ET
import shutil

pptx_path = r"C:\Users\MANIKUMAR\Desktop\Nice Academy\NICE Academy.pptx"
extract_dir = "temp_pptx"
media_dir = os.path.join(extract_dir, "ppt", "media")

# Clean up previous run
if os.path.exists(extract_dir):
    try:
        shutil.rmtree(extract_dir)
    except Exception as e:
        print(f"Warning: Could not clean up {extract_dir}: {e}")

# Unzip PPTX
print(f"Extracting {pptx_path}...")
try:
    with zipfile.ZipFile(pptx_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
except FileNotFoundError:
    print("Error: PPTX file not found.")
    exit(1)
except Exception as e:
    print(f"Error extracting zip: {e}")
    exit(1)

# Extract Text from Slides
print("\n--- Extracted Text ---")
slides_dir = os.path.join(extract_dir, "ppt", "slides")
if os.path.exists(slides_dir):
    try:
        slides = sorted([f for f in os.listdir(slides_dir) if f.startswith("slide") and f.endswith(".xml")], key=lambda x: int(x.replace("slide", "").replace(".xml", "")))
        
        for slide in slides:
            print(f"\n[Slide: {slide}]")
            try:
                tree = ET.parse(os.path.join(slides_dir, slide))
                root = tree.getroot()
                
                slide_text = []
                for elem in root.iter():
                    if elem.tag.endswith('}t'):
                        if elem.text:
                            slide_text.append(elem.text)
                
                print(" ".join(slide_text))
            except Exception as e:
                print(f"Error parsing {slide}: {e}")
    except Exception as e:
        print(f"Error listing slides: {e}")
else:
    print("No slides found.")

# List Images
print("\n--- Extracted Images ---")
if os.path.exists(media_dir):
    images = os.listdir(media_dir)
    for img in images:
        print(f"Image: {img}")
        
    # Copy images to a public folder in the app so we can use them
    public_assets_dir = r"public\assets"
    if not os.path.exists(public_assets_dir):
        os.makedirs(public_assets_dir, exist_ok=True)
        
    for img in images:
        src = os.path.join(media_dir, img)
        dst = os.path.join(public_assets_dir, img)
        try:
            shutil.copy2(src, dst)
        except Exception as e:
            print(f"Error copying {img}: {e}")
    print(f"\nImages copied to {public_assets_dir}")
else:
    print("No media found.")
