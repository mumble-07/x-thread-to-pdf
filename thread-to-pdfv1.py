import os
import requests
from bs4 import BeautifulSoup
import pdfkit

# >>>>>>>>>>>>>>>>> fetch content and images
def fetch_thread_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

# >>>>>>>>>>>>>>>>> extrac imagesd and urls
    images = soup.find_all('img')
    image_urls = [img['src'] for img in images]

    text_content = soup.get_text()

    return text_content, image_urls

# >>>>>>>>>>>>>>>>> save tyo pdf
def save_to_pdf(text_content, image_urls, pdf_filename):
    # Create HTML content with images
    html_content = ""
    for image_url in image_urls:
        html_content += f'<img src="{image_url}">'
    html_content += f'<p>{text_content}</p>'

    # Save HTML to a temporary file
    temp_html_file = 'temp.html'
    with open(temp_html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Convert HTML to PDF
    pdfkit.from_file(temp_html_file, pdf_filename)

    # Remove temporary HTML file
    os.remove(temp_html_file)

# URL of the thread
thread_url = "Thread_URL" # make it dynamic, either do this in GUI style or HTML stle... hhmmm let's see

# Fetch content and images from the thread
text_content, image_urls = fetch_thread_content(thread_url)

# Save content and images to a PDF
pdf_filename = "thread_content.pdf"
save_to_pdf(text_content, image_urls, pdf_filename)

print(f"Thread content saved to {pdf_filename}")
