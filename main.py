import base64

import fitz  # PyMuPDF
from openai import OpenAI
from PIL import Image
import io

from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI client
client = OpenAI()


def extract_page_image(page):
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return img_byte_arr


def translate_page(image_data):
    base64_image = base64.b64encode(image_data).decode('utf-8')
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": "Translate the mathematical content in this image from Vietnamese to English. "
                             "Use LaTex formatting if necessary."
                             "Preserve the mathematical notation and formatting."
                             "Use language style that is appropriate for a math book for middle and high school students."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                ],
            }
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content


def main():
    pdf_path = "./FULL BOOK PP 1-151.pdf"
    output_file = "translated_book.md"

    doc = fitz.open(pdf_path)
    total_pages = len(doc)

    with open(output_file, "w", encoding="utf-8") as f:
        for page_num in range(total_pages):
            print(f"Translating page {page_num + 1}/{total_pages}")

            # Extract page image
            page = doc.load_page(page_num)
            page_image = extract_page_image(page)

            # Translate page content
            translated_content = translate_page(page_image)

            # Append translated content to file
            f.write(f"Page {page_num + 1}:\n")
            f.write(translated_content)
            f.write("\n\n")

            print(f"Page {page_num + 1} translated and appended.")
            if page_num > 5:
                break

    doc.close()
    print(f"Translation complete. Output saved to {output_file}")


if __name__ == "__main__":
    main()