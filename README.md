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
    qr "https://github.com/1homas/QR_Codes" > QR_Code.png

    # SVG
    qr --factory=svg "https://github.com/1homas/QR_Codes" > QR_Code.svg

    # ASCII Characters
    qr --ascii "https://github.com/1homas/QR_Codes" > QR_Code.txt
    ```

1. Preview the images in your OS or a browser and `cat` the `QR_Code.txt` file in a terminal with a monospaced font to view it properly: 
```
cat QR_Code.txt

    █▀▀▀▀▀█  ▀  ▄█▄▄▀██▀▄ █▀▀▀▀▀█
    █ ███ █  ▄▄▀██▄▄▀▀▄▀▀ █ ███ █
    █ ▀▀▀ █ ▄▄▄ ▀██ ▀ ▀▄▄ █ ▀▀▀ █
    ▀▀▀▀▀▀▀ ▀▄█▄█ █ ▀▄█ ▀ ▀▀▀▀▀▀▀
    ▀ ▄█▄█▀▄██▄ ▀ ▄█▀▄▄▀▄▀▄▀ ▄  ▄
    █▀█▀ █▀▀ ▄██▄ ▄ ▀▀██▄▀  █▀██
    █ █▀▄█▀█▄ ▄ █    ▀▀▄ █▀  ▀ ▀▀
    ▀▀ ▀ ▄▀▄▄ █▀▄▄▄▄▄▄▄ █▄█▀▀█▀█▀
    ▀  █▀▄▀▄█▀██▀▀▀ ▄ ▄ █▄▄█ ▄ ▀▄
    ▀ ██▄ ▀▀▄▄▀▀▄█ ▄▀▄█ ▄█ ██  ██
    ▀ ▀▀  ▀ █▄▄▄▀▄▀ ██▄██▀▀▀█ █▄▄
    █▀▀▀▀▀█ ▄█ ▄ █▀ █▀▀ █ ▀ █▄▄█▄
    █ ███ █ ▄▄█▀▀▄█▀▀ ▄▄█▀███▄▄▄▀
    █ ▀▀▀ █  ▀ ▀▀▀▀  ▄▄██▄  █▀▀▄▀
    ▀▀▀▀▀▀▀ ▀▀ ▀▀ ▀     ▀▀▀▀▀▀ ▀

```

## URL Code with Logo Image

1. Edit the `qr_urls.py` script with your document names and URLs

1. Save an image named `logo.png` for the logo in PNG format

1. Run the script:

    ```sh
    qr_urls.py
    ```

1. Then view the generated image:

   ![ISE_Resources.QR.png](ISE_Resources.QR.png)


## WiFi QR Code

1. Edit the `qr_wifi.py` script with your SSID parameters

1. Run the script and optionally redirect the HTML output to a file

    ```sh
    qr_wifi.py
    qr_wifi.py > SSID.html
    ```

## License

This repository is licensed under the [MIT License", url="https://choosealicense.com/licenses/mit/).


