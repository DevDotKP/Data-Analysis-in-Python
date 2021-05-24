import pandas  as pd

import Constants

milkProdDF = pd.read_html ( Constants.readhtml ( Constants.MILK_PRODUCTION ).text, index_col='Date' )
milkProdDF = milkProdDF[0]
print ( milkProdDF )
