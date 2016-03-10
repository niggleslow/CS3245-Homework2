This is the README file for A0110574N's submission

Email Address: a0110574@u.nus.edu

== General Notes about this assignment ==

For this assignment, the general outline of the code is as follows:

>> For the indexing portion, index.py:

1.	Sorts the unsorted documents in the directory (in ascending order)
2.	For each file/document in directory:
	2.1	- 	Use the NLTK sentence and word tokenizers to tokenize the current file
	2.2	- 	Use Porter Stemmer to stem the individual tokens
	2.3 -	Use .lower() to conduct casefolding
3.	A temporary data structure named "array_posting_dictionary" is used to generate >> stemed_token : list(docIDs)
4.	Using the completed "array_posting_dictionary" from step 3, extract the needed information and generate:
	4.1	-	Postings file >> Consists of JSON formatted list of all document IDs (used for NOT operation during search) & Skip Lists
	4.2	-	Dictionary file >> Consists of lines where each individual line follows the format : 
					< stemmed_token, document_frequency, startPostion (of postings list for term), lastPosition (of postings list for term) >
5. Close both files
6. End of Indexing


>> For the searching portion, search.py:

1. Extract queries from the query file
2. For each query in file:
    2.1. Tokenize the raw query into list of query tokens
    2.2. Using the query tokens, create the Reversed Polish Notation version of the BOOLEAN expression
3. Evaluate each RPN-ed BOOLEAN expression sequentially with the aid of a temporary stack.
4. Sort each result in ascending order
5. Write to output file
6. Close all remaining open files - output_file, postings_file
7. End of Searching

* NOTE * Description of helper classes can be found at the top of each respective class :)


== Files included with this submission ==

index.py - indexing code
search.py - searching code
skiplist.py - contains class definition for SkipList, SkipListNode and AdapterList

dictionary.txt - dictionary file obtained from index.py
postings.txt - postings file obtained from index.py
README.txt - information about the overall assignment
ESSAY.txt - answers to the essay questions

== Statement of individual work ==

Please initial one of the following statements.

[X] I, A0110574N, certify that I have followed the CS 3245 Information
Retrieval class guidelines for homework assignments.  In particular, I
expressly vow that I have followed the Facebook rule in discussing
with others in doing the assignment and did not take notes (digital or
printed) from the discussions.  

[ ] I, A0000000X, did not follow the class rules regarding homework
assignment, because of the following reason:

-NA-

I suggest that I should be graded as follows:

-NA-

== References ==

(There's quite many this time around, might have missed out on some :P)

<<Skip Lists Related>>

Inspiration for implementation - https://kunigami.wordpress.com/2012/09/25/skip-lists-in-python/


<<Shunting Yard Related>>

Sample shunting-yard python implementation reference - https://github.com/ekg/shuntingyard/blob/master/shuntingyard.py
Shunting yard algorithm information - http://en.wikipedia.org/wiki/Shunting-yard_algorithm

<<Miscellaneous Python Help>>

Removing leading and trailing whitespaces - http://stackoverflow.com/questions/10443400/remove-leading-and-trailing-spaces
Regex expressions for substitution of subexpression - http://www.tutorialspoint.com/python/python_reg_expressions.htm
JSON storage of data - http://pythontips.com/2013/08/08/storing-and-loading-data-with-json/
Joining of directory names - http://stackoverflow.com/questions/19034822/unknown-python-expression-filename-r-path-to-file

<<Also talked to the following people>>

Talked to:
- Jeremy Ong, Andrew Low, Kester Tan, Brandon Pong (ex-CS3235 student)

-- END --