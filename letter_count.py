# given a string, count how many times each letter woccurs in it


our_string ='superclifragilisticexpialodicious'

def letter_count(s):
    our_dict = {}

    for letter in s:
        if letter in our_dict:
            our_dict(letter) +=1