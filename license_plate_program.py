#!/usr/bin/python

import locale
locale.setlocale(locale.LC_ALL, 'en_US')

import sys
import random
import no_no_words

#
#	GLOBAL VARIABLES
#

LICENSE_PLATE_LENGTH = 6

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


#
#	FUNCTION DEFINITIONS
#

def ways_to_write( ambiguousString ):

	total_ways = 1

	for c in ambiguousString:

		total_ways *= len( letter_mapping[c] )

	return total_ways


def print_total_ways_to_write( ambiguous_str , total_ways ):

	print "If allowing the use of ambiguous characters there are", total_ways, "total ways to write the string '",ambiguous_str,"'"





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


def lay_down_some_new_lines( new_line_count = 1):

	for i in range(1,new_line_count,1):
		sys.stdout.write('\n')

def print_with_new_line_padding( str , padding_count = 1 ):

	lay_down_some_new_lines( padding_count )

	print str

	lay_down_some_new_lines( padding_count )


def censor_word( word_str ):

	censor_chars = [ '@' , '#' , '$' , '*', '&' , '%' ]

	word_len = len( word_str )

	new_word = word_str[0]

	for i in range(1, word_len , 1):
		new_word += random.choice(censor_chars)

	return new_word

def testing():

	random_string = "Some random string"

	print_with_new_line_padding( random_string )





























































#
#	MAIN
#

lay_down_some_new_lines( 5 )

sample_space = pow( len( letter_mapping ) , LICENSE_PLATE_LENGTH )

bad_word_possibilites = 0

for str in no_no_words.some_bad_words:

	upper_str = str.upper()

	if len( upper_str ) > LICENSE_PLATE_LENGTH :

		print_string = "The string '{}' is too long to put on a license plate you dolt!".format( censor_word(upper_str) )

		print_with_new_line_padding( print_string, 1)

		continue

	total_ways_to_write_word = ways_to_write( upper_str )

	total_possibilities = count_total_possibilties( upper_str , total_ways_to_write_word, len( letter_mapping ) )

	bad_word_possibilites += total_possibilities


	safe_str = censor_word( upper_str )
	print_string = "There are {} different ways to put '{}' on a license plate.".format( locale.format("%d", total_possibilities, grouping=True), safe_str )

	print_with_new_line_padding( print_string , 1)

	# print "Total possibilities -> ", total_possibilities



random_string = "Looks like there are {} bad license plates in the sample space of {}".format(	locale.format("%d", bad_word_possibilites, grouping=True),
																								locale.format("%d", sample_space, grouping=True)
																								)

print_with_new_line_padding( random_string, 2)
