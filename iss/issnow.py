#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    print(resp)

if __name__ == "__main__":
    main()

