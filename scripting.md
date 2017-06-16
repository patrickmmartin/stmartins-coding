# Demo programming via unix pipeline composition 

### Assumes there is a dictionary in the usual place for Ubuntu

## here's the class register
> cat class.txt
> cat class.txt  | grep Ruby

## check for dictionary names in the register
> grep class.txt -f  /usr/share/dict/words

## - all there!

## use the smaller dictionary
> grep class.txt -f  dictionary.txt

## alternative that's effectively identical that shows an explicit pipeline
> cat class.txt  | grep -f dictionary.txt

## now count the matches 
> grep class.txt -f  /usr/share/dict/words | wc -l

## and count the source
> cat class.txt  | wc -l

## now check for the *last names* that a dictionary names
## last names
> cat class.txt  | cut -d" " -f 2

## now check for those
> cat class.txt  | cut -d" " -f 2 | grep -f /usr/share/dict/words

## let's look for some names
> grep banana /usr/share/dict/words
> grep Bob /usr/share/dict/words

## out of how many?
> wc -l /usr/share/dict/words

# Moral of the story? NEVER USE WORDS YOU RECOGNISE IN A PASSWORD (because the bad guys will use a dictionary)

