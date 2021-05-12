# Similar to SQL grouo by

import pandas as pd

df = {'Country' : ['India', 'India', 'South_Africa', 'Germany', 'Ireland', 'Palestine', 'South_Africa'],
      'Name' : ['I.C.Vidyasagar',
                'Siddhartha',
                'Desomnd_Tutu',
                'Martin_Luther',
                'St_Paul', 'Solomon',
                'Nelson_Mandela'],
      'Points' : [30, 120, 25,
                  20, 40, 110,
                  60]}

df = pd.DataFrame ( df )

print ( df )

print ( "\n", df.groupby ( 'Country' ).describe ().transpose () )
