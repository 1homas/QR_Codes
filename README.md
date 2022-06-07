# QR Codes

Create QR Codes using the **[qrcode Python library](https://pypi.org/project/qrcode/)**

## Quick Start

1. Clone this repository

    ```sh
    git clone https://github.com/1homas/QR_Codes.git
    ```

1. Create your Python environment 

    ```sh
    pip install pipenv          # Python virtual environment manager
    pipenv install --python 3.9 # Python 3.9+ is currently recommended
    pipenv install pillow       # Python Imaging Library
    pipenv install qrcode       # QR Code library
    pipenv shell                # launch the environment
    ```

## URL QR Code

1. Generate a Text QR code for a URL :

    ```sh
    # PNG
    qr "https://github.com/1homas/QR_Codes" > QR_Codes.png
    # SVG
    qr --factory=svg "https://github.com/1homas/QR_Codes" > QR_Codes.svg
    # ASCII Characters
    qr --ascii "https://github.com/1homas/QR_Codes" > QR_Codes.txt
    ```


## URL Code with Logo Image

1. Edit the script with your document names and URLs

1. Save an image named `logo.png` for the logo in PNG format

1. Run the script:

    ```sh
    qr_urls.py
    ```


## License

This repository is licensed under the [MIT License", url="https://choosealicense.com/licenses/mit/).


