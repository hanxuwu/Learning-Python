# Assignment 2 

## 0.0.1 - Read the file 
Date - 2017-09-20
### Added
- Read the file
- Create the SudokuError
### Problem
- ~~testing the 'sudoku_wrong_2.txt',missing one line~~
- Didn't check the input value

## 0.0.2 - Check the incorrect sudoku 
Date - 2017-09-20
### Added
- Check the sudoku vilid or not
### Problemfix
'sudoku_wrong_2.txt' missing one line originally

## 0.0.3 - Function Preassess 
Date - 2017-09-22
### Added
- Function Preassess() to check clearly have solution or not
### Problem
The function is not pythonic

## 0.0.4 - output the latex(Jupyter) 
Date - 2017-09-25
### Added
- the dict structure
- function ouput the latex
### Problem
haven't test the cancel yet,only bare sudo_test3

## 0.0.5 - output the latex(merge to the sudoku class) 
Date - 2017-09-26
### Added
- bare_tex_output
- tex_output
### Problem
haven't test the cancel yet,only bare sudo_test3 

## 0.0.6 - find the forced number (jupyter) 
Date - 2017-09-27
### Added
- find the forced number and update it in the possible dict
- 

## 0.0.7 - find the forced number (merge to the sudoku class) 
Date - 2017-09-27
### Problemfix
- tex output only one number in the corner(forget +=) 
### change
- sudoku\_dict to self.sudoku_dict
### problem
- didn't test if the run sequence is different 

## 0.0.8 - fixed find more forced number when add each row line and subbox 
Date - 2017-09-27
### Problemfix
- fix testing sudoku_5 (1,6) find forced numebr 9
### add
temp update dict for counting
logic: if add row  or  column   the number is exactly appear once,that means it's it's the forced number or add the subbox,it appear only once, it's also the force number 

## 0.0.9 - fixed read the file without split
Date - 2017-09-27
### Problemfix
- fixed read the file without split  eg:sudoku_4.txt

## 0.0.10 - Not necessary to check row and column when checking the force number
Date - 2017-09-28
- do not need to check the row column when looking for the force number

## 0.0.11 - find the preemptive set(Jupyter)
Date - 2017-09-29
- add necessary attribute in the class worked output tex function
- add find the preemptive set in Jupyter

## 0.0.12 - solve the quiz 4 (Jupyter)
Date - 2017-09-29
### Problemfix 
- wrong spelling cancel
### add
- find the preemptive set
- output the latex in jupyter for preview

## 0.0.13 - solve the sudoku problem (Merge to class)
Date - 2017-09-29
### Problemfix 
- wrong spelling cancel
## add
- Nothing!!