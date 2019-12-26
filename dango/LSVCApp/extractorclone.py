import joblib
from . import credentials;
import tweepy
import csv
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def primary(brand_is, product_is, model_is, pie):

    print('-------------EXTRACTOR-----------')

    #clf = joblib.load('trained_model.sav')
    clf = joblib.load('C:\\Users\\Kaumudi\\Documents\\kmd\\Sentiment Analysis\\LinearSVC\\trained_modelBig.sav')

    auth = tweepy.AppAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


    results = []
    N = 500
    print('Twitter API authenticated. Collecting 500 tweets:')
    #Get the first 5000 items based on the search query
    if bool(model_is) == False:
        for tweet in tweepy.Cursor(api.search, q= brand_is+' AND '+product_is, lang='en').items(N):
            #if tweet is not None:
                #print(tweet)
            #print('***************........***************')
            results.append(tweet)

    else:
        for tweet in tweepy.Cursor(api.search, q= (model_is)+' AND '+'('+brand_is+' OR '+product_is+')', lang='en').items(N):
            #print(tweet)
            results.append(tweet)

    #------------>query = (model_is)+' AND '+'('+brand_is+' OR '+product_is+')'
    #page_count = 0
    #for tweets in tweepy.Cursor(api.search,q=query,count=100,result_type="recent",include_entities=True,since= "2016-02-18", until= "2016-03-18" ).pages():
     #   page_count+=1
      #  print(tweets[0].text.encode('utf-8'))
       # results.append(tweets)
        #if page_count >=2:
       #    break

    #type(results)
    # Create a function to convert a given list of tweets into a Pandas DataFrame.

    def toDataFrame(tweets):
        DataSet = pd.DataFrame()
        DataSet['tweetID'] = [tweet.id for tweet in tweets]
        DataSet['tweetText'] = [tweet.text for tweet in tweets]
        DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
        DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
        DataSet['tweetSource'] = [tweet.source for tweet in tweets]
        DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]
        DataSet['userID'] = [tweet.user.id for tweet in tweets]
        DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
        DataSet['userName'] = [tweet.user.name for tweet in tweets]
        DataSet['userCreateDt'] = [tweet.user.created_at for tweet in tweets]
        DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
        DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]
        DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]
        DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
        DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]
        return DataSet

    get_tweets = toDataFrame(results)
    get_tweets.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    count_vectorizer = joblib.load('C:\\Users\\Kaumudi\\Documents\\kmd\\Sentiment Analysis\\LinearSVC\\count_vectBig.sav')
    get_tweets['NText'] = count_vectorizer.transform(get_tweets['tweetText'])
    get_tweets['Sentiment'] = 0
    
    N1 = get_tweets.shape[0]

    prob = clf.predict_proba(get_tweets.at[0,'NText'])
    count = 0
    for i in range(N1):
        print(prob[i],np.argmax(prob[i]),"\n")
        count = count+1
    get_tweets['Sentiment'] = np.argmax(prob)

    for i in range(count):
        get_tweets.at[i,'Sentiment'] = np.argmax(prob[i])

    get_tweets['Sentiment'].value_counts()

    valuecnts = get_tweets['Sentiment'].value_counts()
    df0 = valuecnts.rename_axis('sentnames').reset_index(name='counts')
    if (df0['sentnames']!=0).all():
        dfl = pd.DataFrame({"sentnames":[0], "counts":[0]}) 
        df0 = df0.append(dfl)
    if (df0['sentnames']!=1).all():
        dfl = pd.DataFrame({"sentnames":[1], "counts":[0]}) 
        df0 = df0.append(dfl)
    if (df0['sentnames']!=2).all():
        dfl = pd.DataFrame({"sentnames":[2], "counts":[0]}) 
        df0 = df0.append(dfl)
    df=df0.sort_values(by=['sentnames'])

    # Create a pie chart
    colors = ["#F44336", "#2196F3", "#4CAF50"]
    fig = plt.figure(dpi=400)
    def my_autopct(pct):
        return ('%.2f' % pct)+'%' if pct > 0 else ''
    plt.pie(
        df['counts'],
        shadow=False,
        colors=colors,
        startangle=90,
        autopct=my_autopct,
        )
    if bool(model_is) == False:
        pietitle = product_is[:1].upper() + product_is[1:]
        plt.title(pietitle, fontsize=18)
    else:
        pietitle = model_is[:1].upper() + model_is[1:]
        plt.title(pietitle, fontsize=18)

    fig.tight_layout()
    fig.savefig('C:\\Users\\Kaumudi\\Documents\\kmd\\Sentiment Analysis\\LinearSVC\\dango\\LSVCApp\\static\\LSVC\\'+pie+'.png', dpi=fig.dpi, transparent = True, bbox_inches = 'tight', pad_inches = 0)

    #type(plt)

    #plt.gcf().canvas.get_supported_filetypes()
    print('saved piechart')
    #timeGraph = get_tweets.plot('tweetCreated','Sentiment').get_figure()
    #lgd = timeGraph.legend(loc='lower left', bbox_to_anchor= (0.0, 4.0))
    #timeGraph.axes([0.0, 0.0, 10.0, 2.0])
    #return [['Sentiment', 'No. of tweets'],['Positive', df.at[2,'counts']],['Neutral', df.at[0,'counts']],['Negative', df.at[1,'counts']]]
    #timeGraph.savefig('C:\\Users\\Kaumudi\\Documents\\kmd\\Sentiment Analysis\\LinearSVC\\dango\\assets\\graph.png', dpi=fig.dpi, transparent = True)
    #print('saved graph')

    return df.iloc[2]['counts']/(df.iloc[0]['counts']+df.iloc[1]['counts']+df.iloc[2]['counts'])


