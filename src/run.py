"""
=========================================
Project: Predict Future Sales - Kaggle
=========================================
Script: run.py

Purpose: run entire pipeline to predict future sales

Creation date: 27/10/2020
Contact: Nadejda Jaeverberg
Email address: nadejda@kth.se
"""

# Clean data and save outputs in interim folder
print("=" * 60)
print("Running cleaning script\n")
from src.make_clean_data.run_clean_data import *
print("=" * 60)
print()

print("DONE!!!")
