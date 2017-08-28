# stat_4710
This is a collection of random scripts that I wrote to test out various concepts in my STAT 4710 class at the University of Missouri - Columbia. Below you'll find a detailed description of each script.



## License Plate Program

### Purpose
To find the total number of allowable license plates given the following parameters, some of which may not reflect real world laws 1 to 1.
1. License plates must be exactly 6 characters long
2. The characters include all 26 uppercase letters along with all number digits. This gives a total of 36 possible choices for each character.
3. Certain words are not allowed. In the real world these would be vulgar words but for the purposes of this program (and because this program might be seen by instructors and possible empoloyers) I'm just going to use a list of nonsense words.
4. Words that use ambigous characters are also not allowed. For example: If the word "APPLE" is not allowed then the string "4PPLE" is also not allowed.
5. If the word is less than 6 characters than all positional variations of that word are also not allowed. For example: If "APPLE" is not allowed on a license plate both the plates "8APPLE" and "APPLE8" are not allowed. 

### How it Works

First a letter mapping is defined that maps each allowable character to a list that includes that letter along with any allowable character that could possibly be used to substitute for it. 

The program will iterate through the list of words that are not allowed. In each iteration it will do the following. 

1. Determine the total ways that that word can be written with ambiguous characters. It does this by iterating through each character in the word and checking the letter mapping to how many variations there are for that character. It maintains a variable that it will multiply by the length of the list of possible characters for the one at that position. This is done by passing the ambiguous string to the function `ways_to_write( ambiguousStr ):` shown below.

```Python
def ways_to_write( ambiguousString ):

	total_ways = 1

	for c in ambiguousString:

		total_ways *= len( letter_mapping[c] )

	return total_ways
  ```