"""
    word_per_page = 0
    pages = int(input("Number of pages: "))
    word_per_page == int(input("Number of words per page: "))
    total_words = pages * word_per_page

    print(total_words)
"""

# Squash bugs with a print() Statement

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))  # The `==` operator checks equality but does not assign a value. 
# As a result, `word_per_page` remains 0, and the input value is ignored.
total_words = pages * word_per_page

print(f"pages = {pages}")
print(f"words_per_page = {word_per_page}")
print(total_words)
