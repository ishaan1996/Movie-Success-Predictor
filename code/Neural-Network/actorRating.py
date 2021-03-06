#The functions in this file creates a dictionary where
#the keys are the names of the actors who are one of the
#main three actors in any movie in the training set
#The values assigned to the keys are the average revenue
#of the films the actor corresponding to the key appear in the The dataset
import creatingDictionary
dataset=creatingDictionary.test()
def populate():
    '''
    This function operates on the dataset of a list of dictionaries.
    Each dictionary in this input list has the complete information
    regarding a single movie.
    Actors1, Actors2, Actors3 are three keys in each dictionary.

    The output of the function is a Dictionary where the keys are the
    name of actors which appeared as a value assigned to any one of the
    three keys Actors1, Actors2, Actors3 in any Dictionary in the list
    of dictionaries given as input to the function.

    Since this is the initialization function the value assigned to keys
    are all zero.
    '''
    actorDictionary={}
    for film in dataset:
        if not(film['Actors1'] in actorDictionary):
            actorDictionary[film['Actors1']]=0
        if not(film['Actors2'] in actorDictionary):
            actorDictionary[film['Actors2']]=0
        if not(film['Actors3'] in actorDictionary):
            actorDictionary[film['Actors3']]=0
    return actorDictionary

def assignCount():
    '''
    This function creates a dictionary. Where keys are the names of the
    actors. The values assigned to theh keys are the total number of films
    in the dataset in which the actor represented by the key appear.
    The return value is this dictionary.
    '''
    actorsDictionary=populate()
    count=0
    for film in dataset:
        if (film['Actors1'] in actorsDictionary):
            actorsDictionary[film['Actors1']]+=1
        if (film['Actors2'] in actorsDictionary):
            actorsDictionary[film['Actors2']]+=1
        if (film['Actors3'] in actorsDictionary):
            actorsDictionary[film['Actors3']]+=1


    return actorsDictionary

def assignTotalRevenue():
    '''
    This function creates a dictionary. Where keys are the names of the
    actors. The values assigned to theh keys are the total revenue generated by
    films in the dataset in which the actor represented by the key appear.
    The return value is this dictionary.
    '''
    actorsDictionary=populate()
    count=0
    for film in dataset:
        if (film['Actors1'] in actorsDictionary):
            actorsDictionary[film['Actors1']]+=float(film['BoxOffice'])
        if (film['Actors2'] in actorsDictionary):
            actorsDictionary[film['Actors2']]+=float(film['BoxOffice'])
        if (film['Actors3'] in actorsDictionary):
            actorsDictionary[film['Actors3']]+=float(film['BoxOffice'])

    return actorsDictionary

def assignAverageRevenue():
    '''
    This function uses the previous two functions to create a dictionary
    where the keys are the names of the actors and the values assigned are
    the average revenue generated by the films in the dataset in which these
    actors appear.
    '''
    actorsTotal=assignTotalRevenue()
    actorsCount=assignCount()
    actorsAverage=populate()
    for actor in actorsAverage:
        actorsAverage[actor]=actorsTotal[actor]/actorsCount[actor]

    return actorsAverage




    



    
