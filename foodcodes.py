from dotenv import load_dotenv
import requests
import sys
import os

# SETUP API KEY HERE
global FDC_API_KEY
FDC_API_KEY = '<YOUR_API_KEY_HERE>'

# Call the API
# Sample API Call: https://api.nal.usda.gov/fdc/v1/food/######?api_key=DEMO_KEY'
def GetFoodByID(fdcID):
   uri = 'https://api.nal.usda.gov/fdc/v1/food/'
   
   payload = {'api_key': FDC_API_KEY}
   r = requests.get(uri + fdcID, params=payload)
   print(r.text)

def main():
   # Ensure Correct Usage
   n = len(sys.argv)
   if n != 2:
      print('Usage: python3 foodcodes.py <FDCID>')
      exit(1)
   fdcID = sys.argv[1]
   
   # Call FDC API
   GetFoodByID(fdcID)
   
   
if __name__ == "__main__":
   main()