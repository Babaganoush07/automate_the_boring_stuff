'''Write a function named printTable() that takes a list of lists of strings 
and displays it in a well-organized table with each column right-justified. 
Assume that all the inner lists will contain the same number of strings. 
For example, the value could look like this:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose'''

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose'],
              ['one', 'two', 'three', 'four']]

def print_table(list_data):

    colWidths = [0] * len(list_data)

    for line in range(len(list_data)):
        for word in range(len(list_data[line])):
            if colWidths[line] <= len(list_data[line][word]):
                colWidths[line] = len(list_data[line][word])
            else:
                colWidths[line] = colWidths[line]
       
    for row in range(len(list_data[0])):
        for column in range(len(list_data)):
            print(list_data[column][row].rjust(colWidths[column]), end=' ')
        print()
        
print_table(table_data)
