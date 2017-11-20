# COMPANY_SUCCESS RATE
import time 
lookup = data.EMPLOYER_NAME.value_counts()
lookup2 = dict(zip(data.EMPLOYER_NAME.unique(),np.zeros((data.EMPLOYER_NAME.value_counts().size))))
lkp=lookup.size
dd=data.copy()
for i in range(0,lkp):
    t = time.time()
    loc=dd.EMPLOYER_NAME.values==lookup.index[i]
    lookup2[lookup.index[i]]=(np.sum(dd[loc].CASE_STATUS.values))/lookup.values[i]
    dd=dd[np.invert(loc)]
    diff = (time.time() - t)
    print(diff)
    print(i)
data['SUCCESS_RATE']= data['APPS_PER_COMPANY'].map(lookup2)

# SOC_SUCCESS_RATE
import time 
lookup = data.SOC_NAME.value_counts()
lookup2 = dict(zip(data.SOC_NAME.unique(),np.zeros((data.SOC_NAME.value_counts().size))))
lkp=lookup.size
dd=data.copy()
for i in range(0,lkp):
    t = time.time()
    loc=dd.SOC_NAME.values==lookup.index[i]
    lookup2[lookup.index[i]]=(np.sum(dd[loc].CASE_STATUS.values))/lookup.values[i]
    dd=dd[np.invert(loc)]
    diff = (time.time() - t)
    print(diff)
    print(i)
data['SOC_SUCCESS_RATE']= data['SOC_NAME'].map(lookup2)






