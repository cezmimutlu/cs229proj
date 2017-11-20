#Get rid of the companies with less than 4 applications
data=data[data["NUM_OF_APPS"]>3]

# Calculate Success rate
lookup = data.EMPLOYER_NAME.value_counts()
lookup2 = dict(zip(data.EMPLOYER_NAME.unique(),np.zeros((data.EMPLOYER_NAME.value_counts().size))))
lkp=lookup.size
for i in range(0,lkp):
    lookup2[lookup.index[i]]=(np.sum(data[data.EMPLOYER_NAME==lookup.index[i]].CASE_STATUS.values))/lookup[i]
data['SUCCESS_RATE']= data['NUM_OF_APPS'].map(lookup2)
