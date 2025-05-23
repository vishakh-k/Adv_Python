import pandas as pd
import numpy as np
a=[[1,2,3,4,5,6],[2,34,5,6,7]];
b=["a","b","c","d"];

s=pd.Series(a);
s1=pd.Series(b);


print(s,s1);

print(np.array(a[0][1]));