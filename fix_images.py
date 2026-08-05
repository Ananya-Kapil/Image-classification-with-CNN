from PIL import Image
import os

folders = [
    "dataset/train/cats",
    "dataset/train/dogs",
    "dataset/validation/cats",
    "dataset/validation/dogs",
    "dataset/test/cats",
    "dataset/test/dogs",
]

fixed = 0
deleted = 0

for folder in folders:
    print(f"\nChecking {folder}")

    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)

        try:
            with Image.open(path) as img:
                rgb = img.convert("RGB")
                rgb.save(path, "JPEG", quality=95)

            fixed += 1

            if fixed % 500 == 0:
                print(f"Fixed {fixed} images...")

        except Exception as e:
            print(f"Deleting unreadable image: {path}")
            print(e)
            os.remove(path)
            deleted += 1

print("\nDone!")
print("Images fixed:", fixed)
print("Images deleted:", deleted)