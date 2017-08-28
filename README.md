# stat_4710
This is a collection of random scripts that I wrote to test out various concepts in my STAT 4710 class at the University of Missouri - Columbia. Below you'll find a detailed description of each script.

#### Disclaimer
If the formatting or whatever else in my Python code makes you cringe I'm sorry. I'm brand new to Python and will probably come back and fix things up once I know better. If you have any suggestions or admonitions send me an email at arfv2b@mail.missouri.edu

## License Plate Program

### Purpose
To find the total number of allowable license plates given the following parameters, some of which may not reflect real world laws 1 to 1.
1. License plates must be exactly 6 characters long
2. The characters include all 26 uppercase letters along with all number digits. This gives a total of 36 possible choices for each character.
3. Certain words are not allowed. In the real world these would be vulgar words but for the purposes of this program (and because this program might be seen by instructors and possible empoloyers) I'm just going to use a list of nonsense words.
4. Words that use ambigous characters are also not allowed. For example: If the word "APPLE" is not allowed then the string "4PPLE" is also not allowed.
5. If the word is less than 6 characters than all positional variations of that word are also not allowed. For example: If "APPLE" is not allowed on a license plate both the plates "8APPLE" and "APPLE8" are not allowed. 

### How it Works

First a letter mapping is defined that maps each allowable character to a list that includes that letter along with any allowable character that could possibly be used to substitute for it. The letter mapping is shown below:

```Python
letter_mapping = 	{
			'A' : [ 'A', '4' ],
			'B' : [ 'B' , '8' ],
			'C' : [ 'C' ],
			'D' : [ 'D' ],
			'E' : [ 'E' , '3' ],
			'F' : [ 'F' ],
			'G' : [ 'G' , '6' ],
			'H' : [ 'H' ],
			'I' : [ 'I', '1' ],
			'J' : [ 'J' ],
			'K' : [ 'K' ],
			'L' : [ 'L' ],
			'M' : [ 'M' ],
			'N' : [ 'N' ],
			'O' : [ 'O', '0' ],
			'P' : [ 'P' ],
			'Q' : [ 'Q' ],
			'R' : [ 'R' ],
			'S' : [ 'S' , '5' ],
			'T' : [ 'T' ],
			'U' : [ 'U' ],
			'V' : [ 'V' ],
			'W' : [ 'W' ],
			'X' : [ 'X' ],
			'Y' : [ 'Y' ],
			'Z' : [ 'Z' , '2' ],
			'0' : [ '0' , 'O' ],
			'1' : [ '1' , 'I' ],
			'2' : [ '2' , 'Z' ],
			'3' : [ '3' , 'E' ],
			'4' : [ '4' , 'A' ],
			'5' : [ '5' , 'S' ],
			'6' : [ '6' , 'G' ],
			'7' : [ '7' ],
			'8' : [ '8' , 'B' ],
			'9' : [ '9' ]
		}
```

The program will iterate through the list of words that are not allowed. In each iteration it will do the following. 

1. Determine the total ways that that word can be written with ambiguous characters. It does this by iterating through each character in the word and checking the letter mapping to how many variations there are for that character. It maintains a variable that it will multiply by the length of the list of possible characters for the one at that position. This is done by passing the ambiguous string to the function `ways_to_write( ambiguousStr ):` shown below.

```Python
def ways_to_write( ambiguousString ):

	total_ways = 1

	for c in ambiguousString:

		total_ways *= len( letter_mapping[c] )

	return total_ways
  ```
  
  2. After determining the total ways that we can write a word using letter substitution then we have to find how many variations there are if we modify the position of the string. This is done by passing the string, the total ways to write that we just calculated, and the number of available characters to the function `count_total_possibilties( ambiguous_str , total_ways, total_character_possibilities ):`. First the function checks to see if the word is exactly the length of the maximum allowed length of license plate strings (in this case 6). If it is then there is only one way. If not it will calculate how many remaining spots there are. The number of allowable ways to write this string on a license plate is equal to the number of remaining spots + 1 multiplied by both the total ways to write the original string as found by the preivous function and the number of ways to fill the open spots ( 36 to the power of the remaining spots). I'm still unsure if this is correct however and some checking would be appreciated. This function is shown below.  
  
  ```Python
  def count_total_possibilties( ambiguous_str , total_ways, total_character_possibilities ):

	if len(ambiguous_str) == LICENSE_PLATE_LENGTH:
		return total_ways


	remaining_spots = (LICENSE_PLATE_LENGTH - len( ambiguous_str) )

	different_positional_ways = remaining_spots + 1


	# 	FIXME:
	#		So this is the math that I'm not too sure about. Basically
	#		I get the number of different positional variations. For example
	#		if we have 6 total spaces and the word is 5 letters long there are
	#		two different ways to make that. One with a random character at the
	#		beginning and one with a random character at the end. Here I take
	#		this value and multiply it by how much variation there can be in the
	#		open spots which would be ( 36 * 'number of random open spots to fill' ).
	#		Is this right?

	return (total_ways * different_positional_ways * pow( total_character_possibilities, remaining_spots ))
```

3. After finding the total number of ways to write this on a license plate it will print a censored version of this string and the number of ways it can be written. It will then add this number to a variable and move on to the next string in the list. At the end it will display this value as well as all possible allowable values (this is found by taking the number of allowable characters, 36, to the power of the length of the license plate 6).

### Output

Using the following as the input array
```Python
some_bad_words =    [
                        "this",
                        "is",
                        "just",
                        "list",
                        "example",
                        "words",
                        "nonsense",
                        "apple"
                    ]
```

you will get the following as output


```
There are 15,552 different ways to put 'T#*$' on a license plate.
There are 33,592,320 different ways to put 'I#' on a license plate.
There are 7,776 different ways to put 'J#%#' on a license plate.
There are 15,552 different ways to put 'L##@' on a license plate.
The string 'E&*&@%*' is too long to put on a license plate you dolt!
There are 288 different ways to put 'W***$' on a license plate.
There are 7,776 different ways to put 'B%*$' on a license plate.

Looks like there are 33,639,264 bad license plates in the sample space of 2,176,782,336
```


### Running It Yourself

#### Prerequisites
- Python version >= 2.7
  - If you need to install Python and have a windows machine follow [this guide](https://www.howtogeek.com/197947/how-to-install-python-on-windows/). If you have a Mac follow [this one](http://www.pyladies.com/blog/Get-Your-Mac-Ready-for-Python-Programming/)
- Git version >= 2.0 (optional)
  - This makes downloading the files slightly easier (I think). An install guide can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

#### Running
##### All
Clone the repository or download and unzip the contents of this repository.


##### Mac
  1. In terminal navigate to where you downloaded the files.
  2. Here run the command `python license_plate_program.py`
  
##### Windows
  1. I don't use Windows but I'm sure [this guide](http://pythoncentral.io/execute-python-script-file-shell/) should help out.
  
#### Final
That's all it is. Thanks for taking a look at this.
