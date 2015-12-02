import tmdbsimple as tmdb
from glb import *
tmdb.API_KEY = APIKEY


def movieSearch(movieName):
    search = tmdb.Search()
    responses = search.movie(query=movieName)

    movie = tmdb.Movies(responses['results'][0]['id'])

    info = movie.info()

    return info


def peopleSearch(personId, answer, answerDepartment):
    person = tmdb.People(personId)
    previousMoviesPerson = person.movie_credits()[answerDepartment]
    print str(answer) + " " + str(person.info()['name'])
    avgRevenuePerson = 0
    avgRatingPerson = 0
    cntRatingPerson = 0
    cntRevenuePerson = 0
    bestRatingPerson = 0
    bestRevenuePerson = 0
    worstRatingPerson = 999999999999999999
    worstRevenuePerson = 999999999999999999
    if(answer == 'Directing' or answer == 'Writing' or answer == 'Production'):

        for i in range(len(previousMoviesPerson)):
            if(previousMoviesPerson[i]['department'] == answer):
                movieInfo = movieSearch(previousMoviesPerson[i]['title'])
                if(movieInfo['budget'] and movieInfo['revenue']):
                    cntRevenuePerson += 1

                    movieInfo['budget'] = float(movieInfo['budget'])
                    movieInfo['revenue'] = float(movieInfo['revenue'])

                    avgRevenuePerson = avgRevenuePerson + \
                        (movieInfo['revenue'] / movieInfo['budget'])
                    bestRevenuePerson = max(
                        bestRevenuePerson,
                        (movieInfo['revenue'] / movieInfo['budget']))
                    worstRevenuePerson = min(
                        worstRevenuePerson,
                        (movieInfo['revenue'] / movieInfo['budget']))

                if(movieInfo['vote_average'] != 0):
                    avgRatingPerson = float(
                        avgRatingPerson +
                        movieInfo['vote_average'])
                    bestRatingPerson = max(
                        bestRatingPerson,
                        movieInfo['vote_average'])
                    worstRatingPerson = min(
                        worstRatingPerson,
                        movieInfo['vote_average'])
                    cntRatingPerson += 1
    if(cntRatingPerson > 0):
        avgRatingPerson = (avgRatingPerson / cntRatingPerson)
    else:
        avgRatingPerson = 5
    if(cntRevenuePerson > 0):
        avgRevenuePerson = (avgRevenuePerson / cntRevenuePerson)
    else:
        avgRevenuePerson = 1
    result = {}
    if(avgRatingPerson > 10):
        avgRatingPerson = 6
    if(bestRatingPerson > 10):
        bestRatingPerson = 6
    if(worstRatingPerson > 6):
        worstRatingPerson = 6

    # print '______________'

    result['avgRatingPerson'] = avgRatingPerson
    result['avgRevenuePerson'] = avgRevenuePerson
    result['bestRatingPerson'] = bestRatingPerson
    result['bestRevenuePerson'] = bestRevenuePerson
    result['worstRatingPerson'] = worstRatingPerson
    result['worstRevenuePerson'] = worstRevenuePerson
    for key in result:

        print str(key) + " " + str(result[key])
    print '______________'

    return result


def findBitVector(thisMovieGenres):
    a = []
    for i in range(len(thisMovieGenres)):
        a.append(thisMovieGenres[i]['name'])
    thisMovieGenre = a
    ans = []
    for i in range(len(genres)):
        ans.append(0)
    cnt = 0
    for genre in genres:

        if(genre in thisMovieGenre):
            print genre
            ans[cnt] = 1
        cnt += 1
    return ans


def getFingerPrint(movieName):

    movieNameList = []
    movieNameList.append(0)
    ij = 0
    movieNameList[ij] = movieName
    search = tmdb.Search()
    responses = search.movie(query=movieNameList[ij])
    movie = tmdb.Movies(responses['results'][0]['id'])
    movieInfo = movie.info()

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

    for key in genreBitVector:
        inputFeature.append(key)

    inputFeature.append(0)

    for key in directorAvgRating.keys():
        inputFeature.append(directorAvgRating[key])

    for key in writerAvgRating.keys():
        inputFeature.append(writerAvgRating[key])

    target = -1

    print 'Genereating FingerPrint'
    print inputFeature
    fingerPrint = inputFeature
    return fingerPrint
