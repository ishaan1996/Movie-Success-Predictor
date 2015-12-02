import tmdbsimple as tmdb
from glb import *
from functions import *

'''

	DATASET PREPARATION
	Global file contains list of movie names .
	Dataset preparation from list of movie names.
	output2.txt contains dataset

'''

tmdb.API_KEY = APIKEY
with open('output2.txt', 'a') as f:
    for ij in range(0, len(movieNameList)):
        print movieNameList[ij]
        search = tmdb.Search()
        try:
            responses = search.movie(query=movieNameList[ij])
            movie = tmdb.Movies(responses['results'][0]['id'])
            movieInfo = movie.info()
        except:
            print ij
            continue
        credits = movie.credits()['crew']

        genre = movieInfo['genres']
        revenue = float(movieInfo['revenue'])

        budget = float(movieInfo['budget'])
        review = movieInfo['vote_average']
        popularity = movieInfo['popularity']

        # print genre
        # print revenue

        # print budget
        # print review
        # print popularity

        writerId = -1
        for i in range(len(credits)):
            if(credits[i]['department'] == 'Writing'):
                writerId = credits[i]['id']
                break

        directorId = -1
        for i in range(len(credits)):
            if(credits[i]['department'] == 'Directing'):
                directorId = credits[i]['id']
                break

        # print writerId
        writerAvgRating = peopleSearch(writerId, 'Writing', 'crew')
        # print writerAvgRating
        directorAvgRating = peopleSearch(directorId, 'Directing', 'crew')
        # print directorAvgRating

        # print directorId

        genreBitVector = findBitVector(genre)
        inputFeature = []
        if(budget == 0):
            continue

        for key in genreBitVector:
            inputFeature.append(key)

        inputFeature.append(revenue / budget)

        for key in directorAvgRating.keys():
            inputFeature.append(directorAvgRating[key])

        for key in writerAvgRating.keys():
            inputFeature.append(writerAvgRating[key])

        target = -1

        if(review >= 6.5 and (revenue / budget) >= 3):
            target = 0  # BLOCKBUSTER
        elif(review >= 6.5 and (revenue / budget) < 3):
            target = 1  # CRITICAL WINNER
        elif(review < 6.5 and review >= 5 and (revenue / budget) >= 3):
            target = 2  # PROFITABLE VENTURE
        elif(review < 6.5 and review >= 5 and (revenue / budget) < 3):
            target = 3  # AVERAGE

        for i in inputFeature:
            f.write(str(i) + ',')

        print inputFeature

        f.write(str(target) + ',')
        f.write('\n')

        print target
        print ij
