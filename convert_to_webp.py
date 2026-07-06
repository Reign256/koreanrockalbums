from pathlib import Path
from PIL import Image

root = Path(".")

converted = 0
updated = 0

print("Converting PNGs to WebP...")

# Convert PNGs
for png in root.rglob("*.png"):

    # Skip logo2.png
    if png.name.lower() == "logo2.png":
        print(f"Skipping {png}")
        continue

    webp = png.with_suffix(".webp")

    try:
        img = Image.open(png)

        img.save(
            webp,
            "WEBP",
            quality=90,
            method=6
        )

        png.unlink()

        converted += 1
        print(f"Converted {png}")

    except Exception as e:
        print(f"Failed {png}: {e}")

print("\nUpdating HTML files...")

# Update HTML
for html in root.rglob("*.html"):

    text = html.read_text(encoding="utf-8")
    original = text

    text = text.replace(".PNG", ".webp")
    text = text.replace(".png", ".webp")

    # Restore logo2 references
    text = text.replace("logo2.webp", "logo2.png")

    if text != original:
        html.write_text(text, encoding="utf-8")
        updated += 1
        print(f"Updated {html}")

print("\nDone!")
print(f"Converted {converted} images.")
print(f"Updated {updated} HTML files.")