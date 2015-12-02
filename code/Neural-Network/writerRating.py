# This module assigns a numerical value to the names of the writers
# so that it can be used as a feature in the regression model.
# The aim is to create a dictionary where the keys are the
# names of the writers and the values assigned to the keys are
# the average revenue generated by the films written
# by the corresponding writer.
import creatingDictionary
dataset=creatingDictionary.test()
def populate():
    '''
    This function creates a dictionary where the keys are the names of the
    writers and the values assigned are all zero.
    '''
    writerDictionary={} 
    #An empty dictionary is created.
    for film in dataset:
        #For each new writer the 'for loop' finds( a writer whose name
        #is not already present in the dictionary ) a dictionary entry
        # is created. The key is the name of the writer and the value
        # Assigned is zero.
        if not(film['Writer'] in writerDictionary):
            writerDictionary[film['Writer']]=0
    return writerDictionary

def assignCount():
    '''
    This function calls the populate() function to create the
    dictionary. Later with the for loop it updates the key value from zero
    to the number of films in the dataset written by the writer.
    '''
    writerDictionary=populate()
    # The dictionary with keys the names of the writers and
    # the values zero is created.
    for film in dataset:
        #The for loop traverses the initial input dataset updates the
        #values assigned to the keys in the writerdictionary to be
        #the total number of films written by the writer.
        if (film['Writer'] in writerDictionary):
            writerDictionary[film['Writer']]+=1


    return writerDictionary

def assignTotalRevenue():
    '''
    This function calls the populate() function to create the
    dictionary. Later with the for loop it updates the key value from zero
    to the total revenue generated by the films in the dataset
    written by the writer.
    '''
    writerDictionary=populate()
    count=0
    for film in dataset:
        #The for loop traverses the initial input dataset updates the
        #values assigned to the keys in the writerdictionary to be
        #the total revenue generated  by films written by the writer.
        if (film['Writer'] in writerDictionary):
            writerDictionary[film['Writer']]+=float(film['BoxOffice'])



    return writerDictionary

def assignAverageRevenue():
    writerTotal=assignTotalRevenue()
    # writerTotal is the dictionary where keys are the names of the writers
    # and the values are the total revenue generated by films written by them
    writerCount=assignCount()
    # writerTotal is the dictionary where keys are the names of the writers
    # and the values are the number of films directed by the writer.
    writerAverage=populate()
    # The writer average is the dictionary in which the keys are the
    # names of the directors and the value assigned is zero.
    for writer in writerAverage:
        # All the three dictionaries have the same set of keys
        # The for loop updated the values in the writersAverage dictionary
        # from zero to the average revenue generated by the films
        # written by the writer.
        writerAverage[writer]=writerTotal[writer]/writerCount[writer]

    return writerAverage






    



    
