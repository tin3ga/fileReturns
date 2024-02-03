# fileReturns

Automation script to file Nil Returns.


## Quick Start

1. Clone the repo:

```
$ https://github.com/tin3ga/fileReturns.git
$ cd fileReturns
```

2. Initialize and activate a virtualenv:

```
# windows
$ python -m venv venv
$ venv\Scripts\activate

# mac/linux
$ python -m venv venv
$ source env/bin/activate or . venv/bin/activate
```

3. Install the dependencies:

```
$ pip install -r requirements.txt
```
4. Create .env file with the following template:
```
pin=""
password=""
BROWSER_PATH="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
TESSERACT_OCR_PATH="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
```
5. Run the script:

```
$ python main.py
```