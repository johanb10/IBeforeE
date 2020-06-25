# "I before E except after C"?
## Goal: Figure out if this rule is valuable
# author: Johan M. Cos
import pandas as pd
from pathlib import Path
# We are using a dataset of words extracted from Google books
data_url = 'https://norvig.com/google-books-common-words.txt'
words = pd.read_csv(data_url, index_col=None, names=['word','count'], sep='\t')

# reduce the number of words to only the most common 20k
words = words[:20000]

# create two new variables, to hold the two possibilities for how the i and e can be arranged

contains_ie = words.word.str.contains('ie', regex=False, case=False)
contains_ei = words.word.str.contains('ei', regex=False, case=False)

print('Based on our data, out of', words.shape[0], 'words there are', contains_ie[contains_ie == True].count(), 'words with "ie" and', contains_ei[contains_ei == True].count(), 'words with "ei"')

exceptions = words.word.str.contains('cie', regex=False, case=False)
followers = (contains_ie | contains_ei) & (exceptions == False)

exceptions_count = exceptions[exceptions == True].count()
followers_count = followers[followers == True].count()

print('Based on our data, there are', followers_count, 'cases that follow the rule and', exceptions_count, 'cases that violate the rule \n\nThus, the rule applies', round(100 * (followers_count / (followers_count + exceptions_count))), '% of the time')
# Conclusion: Because the rule works 94% of the time, it would be reasonable to say that the rule does in fact have value
