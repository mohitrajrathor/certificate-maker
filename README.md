# Certificate Maker 

This Python script allows you to format HTML files so that these can be converted into images or pdf. It's a convenient tool for generating image representations of web pages, which can be useful for various purposes such as generating formating certificate, thumbnails, creating previews, or automating website screenshots.

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome Web Browser
- ChromeDriver
- imgkit
- wkhtmltopdf


## Installation

1. Clone or download the repository.


2. Install the required dependencies using pip.


3. Download ChromeDriver from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads) and place it in the `html_to_image_converter` directory.

## Usage

### Command Line Interface (CLI)

To convert a local HTML file to an image:


To convert a web page URL to an image:


You can specify additional options such as output image format, width, and height:


### Script Usage

You can also use the converter as a module in your Python scripts:

```python
from html_to_image_converter import HTMLToImageConverter

# Initialize the converter
converter = HTMLToImageConverter()

# Convert HTML file to image
converter.convert_from_file("path/to/your/file.html", output_image="output.png")

# Convert web page URL to image
converter.convert_from_url("https://example.com", output_image="output.png")
```