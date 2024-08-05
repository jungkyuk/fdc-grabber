# Introduction
A simple script to get nutrient info from Food Data Central by FDC IDs

## Setup
1. Clone the repo with `git clone https://github.com/jungkyuk/fdc-grabber.git`

2. Create a .env file with your api key:  
BEFORE COPY AND PASTING, REPLACE <YOUR_API_KEY_HERE> with your API key from FDC  
`echo FDC_API_KEY=<YOUR_API_KEY_HERE> > .env`

3. Create a virtual environment:  
`python -m venv .venv`

4. Activate the venv  
Windows: `.venv/Scripts/activate`  
Mac: `source .venv/bin/activate`

5. Install requirements
Run `pip install -r requirements.txt`

## Usage
Run with `python foodcodes.py <fdcID>`
