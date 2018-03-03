# A machine learning application that recommends you movies based on what you like
import numpy
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

# Fetch data and format it from the public database of ratings
data = fetch_movielens(min_rating=4.0)

# Create model
model = LightFM(loss='warp') # warp = Weighted Approximate Rank Pairwise. It is content + collaborative for creating recommendations

# Train model
model.fit(data['train'], epochs=30, num_threads=2)

# Generates a recommendation for those parameters
def sampleRecommendation(model, data, userIds):
    # Number of users and movies in training data
    users, items = data['train'].shape

    # Generate recommendations for each user
    for userId in userIds:
        # Movies we already like
        knownPositives = data['item_labels'][data['train'].tocsr()[userId].indices]

        # Movies our model predicts we will like
        scores = model.predict(userId, numpy.arange(items))

        # Rank them for lost liked to least liked
        topItems = data['item_labels'][numpy.argsort(-scores)]

        # Print the results
        print('User %s' % userId)
        print(' Known positives:')

        for x in knownPositives[:3]:
            print('     %s' % x)

        print(' Recommended:')

        for x in topItems[:3]:
            print('     %s' % x)

sampleRecommendation(model, data, [3, 25, 450])
