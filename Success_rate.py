#Get rid of the companies with less than 4 applications
data=data[data["NUM_OF_APPS"]>3]

# Calculate Success rate
lookup = data.EMPLOYER_NAME.value_counts()
lookup2 = dict(zip(data.EMPLOYER_NAME.unique(),np.zeros((data.EMPLOYER_NAME.value_counts().size))))
lkp=lookup.size
dd=data.copy()
for i in range(0,lkp):
    loc=dd.EMPLOYER_NAME.values==lookup.index[i]
    lookup2[lookup.index[i]]=(np.sum(dd[loc].CASE_STATUS.values))/lookup[i]
    dd=dd[np.invert(loc)]
data['SUCCESS_RATE']= data['NUM_OF_APPS'].map(lookup2)
