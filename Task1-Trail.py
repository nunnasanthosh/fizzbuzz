1.Classify the Data into diffrent lists for each type of "General Condition" that you find in the data set.

import pandas as pd
DF = pd.read_csv("Trails.csv")
GOOD_Condition = DF[DF["CONDITION"]=="GOOD"].values.tolist()
UNKNOWN_Condition = DF[DF["CONDITION"]=="UNKNOWN"].values.tolist()
MARGINAL_Condition = DF[DF["CONDITION"]=="MARGINAL"].values.tolist()
POOR_Condition = DF[DF["CONDITION"]=="POOR"].values.tolist()
print("Good\n" ,  Condition_good ," BAD\n" , Condition_Poor, Condition_marginal,Condition_UnKnown )



2.Find the number of trails that are installed after the year 2000. Return a list of them. 

Year_2000 = DF[DF["INST_YEAR"]>2000].values.tolist()
print("total Trails established after year 2000: ",len(Year_2000))


3.How many trails are currently Active? How many have lighting?. How many are both "Walking" and have "Biking"?


ActiveTrails = DF[DF["STATUS"]=="ACTIVE"].values.tolist()
print("total Trails that are active: ",len(ActiveTrails))



Lighting = DF[DF["LIGHT"]=="Y"].values.tolist()
print("total Trails that lightning: ",len(Lighting))



