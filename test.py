
import re as regex # I don't like the abbreviation "re", as it can be easily overlooked or overwritten

assert not regex.match("a", "cat") # Match starts looking at the beginning
assert regex.search("a", "cat") # Search searches anywhere in the string
assert not regex.search("c", "dog")
# Anything in brackets is a set of characters, any single character in a set becomes a search criteria
assert len(regex.split("[ab]", "carbs")) == 3 # Splits at every occasion
assert regex.sub("[el]", "o", "Hello") == "Hoooo" # Substitutes at every occasion