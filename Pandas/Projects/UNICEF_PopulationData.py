import pandas as pd
from matplotlib import pyplot as plt

try :
    populationDF = pd.read_excel ( r'C:\Users\kisho\Downloads\WPP2019_POP_F01_1_TOTAL_POPULATION_BOTH_SEXES.xlsx',
                                   engine='openpyxl', header=16, sheet_name='ESTIMATES' )
    # populationDF = populationDF.set_index ( 'Index')
    filteredPopulationDF = populationDF[populationDF['Type'].str.contains ( 'Country/Area' )]

    southAsiaDataDF = filteredPopulationDF[filteredPopulationDF['Parent code'] == 5501]
    southAsiaDataDF.drop ( columns=['Variant', 'Notes', 'Index'], inplace=True )
    southAsiaDataDF.rename ( columns={'Region, subregion, country or area *' : 'Country'}, inplace=True )
    # southAsiaDataDF.reset_index()
    # southAsiaDataDF.set_index ( 'Country',inplace=True )
    print ( southAsiaDataDF.head () )
    # southAsiaDataDF['1970'].plot (figsize=(12,5))
    filteredData = southAsiaDataDF['1970']
    pivotedTable = southAsiaDataDF.pivot_table ( data=southAsiaDataDF, index=['1970'] )
    pivotedTable.plot ()
    plt.tight_layout ()
    plt.show ()
    # print()
    # southAsiaDataDF[southAsiaDataDF['Country'].str.contains('India')].plot()
    # plt.show()

    # pivotSouthAsia = southAsiaDataDF.pivot_table('Country')
    # print('\n\n Columns',pivotSouthAsia)
except Exception as e :
    print ( e.__cause__ )
    # print(e.with_traceback())
    print ( e.__doc__ )
    print ( e.args )
