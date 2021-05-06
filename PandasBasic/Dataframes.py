import logging as logger

import numpy as np
import pandas as pd

try :
    from numpy.random import randn

    np.random.seed ( 101 )

    randomMatrix = randn ( 5, 5 )

    print ( randomMatrix )

    randomMatrixSeries = pd.DataFrame ( data=randomMatrix )

    print ( randomMatrixSeries )

    randomMatrix = pd.DataFrame ( data=randomMatrix, index='A1 B1 C1 D1 E1'.split (),
                                  columns='A2 B2 C2 D2 E2'.split () )

    print ( randomMatrix )

    print ( '\nClipped' )
    clippedColumnRandomMatrix = ['A2', 'B2',
                                 'C2']  # This method only works for columns. For rows, we will use a different method
    print ( randomMatrix[clippedColumnRandomMatrix] )
    randomMatrix["New"] = randomMatrix['A2'] + randomMatrix['E2']
    print ( randomMatrix )
    randomMatrix.drop ( columns='New',
                        inplace=True )  # The parameter inplace asks you if you want to make the change permanent
    print ( '\nAfter dropping: \n', randomMatrix )

    print ( '\nCliped Row' )
    clippedRowRandomMatrix = randomMatrix.loc[('A1 C1 D1'.split ())]
    print (
        clippedRowRandomMatrix )  # For columns, we defined the columns we wanted (Line 34), then fed that as a parameter to the actual matrix. For rows, since you're getting the clipped row matrix utself, you can directly reference it for values

    randomMatrix.loc["NewRow"] = randomMatrix.loc['A1'] + randomMatrix.loc['C1']
    print ( randomMatrix )

    randomMatrix.drop ( index="NewRow", inplace=True )
    print ( '\nAfter dropping: \n', randomMatrix )

except Exception as e :
    print ( 'Error detected!:{} \n {} \n {}'.format ( e.args, e.__class__, e.__doc__ ) )
    logger.error ( e.args )
