movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1

def scoreMore(filmName):
    for i in range(0, len(movies)):
        if movies[i]['name']==filmName:
            if movies[i]['imdb']>5.5:
                print(True)
                break
            else:
                print(False)
                break

scoreMore('Exam')

#2

def scoreLess():
    less = []
    for i in range(0, len(movies)):
        if movies[i]['imdb']>5.5:
            less.append(movies[i]['name'])
            
    print(less)
            
scoreLess()
            
#3

def searchCat(catName):
    for i in range(0, len(movies)):
        if movies[i]['category']==catName:
            print(movies[i]['name'], end='\t')
                
searchCat('Romance')

#4
print()

def avgImdb():
    sum=0
    q=0
    for i in range(0, len(movies)):
        sum+=movies[i]['imdb']
        q+=1
        
    print(sum/q)
    
avgImdb()
        
#5

def searchCatAvg(catName):
    sum=q=0
    for i in range(0, len(movies)):
        if movies[i]['category']==catName:
            sum+=movies[i]['imdb']
            q+=1
            
    print(sum/q)
    
searchCatAvg("Suspense")
