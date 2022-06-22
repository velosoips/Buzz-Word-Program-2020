BUZZ WORD PROGRAM: Comparing Trending Words from Tweets in 2018 and 2020

## Description

This program attempts to read through Twitter tweets from October 1, 2020 and October 2, 2020
to determine the top 5 buzz words (most commonly used words) from two different days. The program
counts the number of times a word appears in the twitter tweet compilation files and then lists
the top 5 words from each file/day. These to 5 words can be indicative of trending words,
topics, people, events, etc. Such results can be analyzed by the user for trend analysis.

## Dataset Sources
The .json files containing Twitter Tweets used in this program were obtained from the following website:
https://archive.org/details/archiveteam-twitter-stream-2020-10
Author: @Sketch the Cow (https://archive.org/details/@sketch_the_cow)


## Getting Started

### Dependencies

* To run this program, you will need to download python 3 and a text editor such as Spyder.

### Installing

* How to download program and data:
    * Access the program github page
    * Download the following files:
        * IVeloso - FPFinal.py
        * oct12020.json
        * oct22020.json
    * Make sure each of the files are accessable by your text editor (within the same folder).
    * Make sure Counter from the collections module is downloaded and accessable on your Python.

### Executing program

* How to execute program:

    * Open IVeloso - FPFinal.py on python text editor of choice.
    * Run the file so that it reaches for the two .json files:
        * oct12020.json
        * oct22020.json
    * View results for each file in console.
    
* If you would like to use the program to read other .json files that contain twitter tweets
from other days, months, or years in the same format as those given, you can substitute the files
being opened in lines 46 and 63 to the file names of choice. Make sure to download your files
in the correct folder/location to ensure that they are read when the program runs.
    
## Authors

Contributor name and contact info

ex. Ingrid Veloso
ex. [velosoi1@montclair.edu]

## Version History

* 0.1
    * Initial Release: June 22, 2022
