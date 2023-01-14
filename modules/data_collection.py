import requests
from bs4 import BeautifulSoup
import pandas as pd


alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_soup(letter):
  """
  Collects web page data with get request."""
  page = requests.get(f"https://youngjustice.fandom.com/wiki/Category:Individuals?from={letter}")

  return page


def get_characters(page):
  """Using BeautifulSoup, webscrapes data to obtain character names"""
  soup = BeautifulSoup(page.content, 'html.parser')
  category_page_members = soup.find(class_='category-page__members')
  member_items = category_page_members.find_all(class_='category-page__member')
  member = member_items[0]
  # print(member)

  members = [m.get_text().replace("\n","") for m in member_items]

  return members

def to_pandas_dataframe(members, letter):
  """Inputs character data to pandas DataFrame, 
  and subsequently creates a new CSV file. """
  character = pd.DataFrame({"name": members})

  character.to_csv(f'/Users/shanejeon/Desktop/programming/intoTheDCUniverse/DCuniverse_app/data/YJcharacters{letter}')


def collect_character_data():
  """Iterates through every alphabetized page, from characters A - Z."""
  for letter in alph: 
    characters = get_characters(get_soup(letter))

    to_pandas_dataframe(characters, letter)
  
  return

    
collect_character_data()