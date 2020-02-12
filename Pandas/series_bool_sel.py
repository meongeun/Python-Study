import numpy as np
import pandas as pd

s = pd.Series(np.arrange(10), np.arrange(10)+1)

s[s>5]
s[s% 2 == 0]

s.index >5
s[s.index >5 ]

s[(s > 5) & (s<8)]

(s >= 7).sum()
(s[s>=7]).sum()


