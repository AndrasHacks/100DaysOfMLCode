# 100 Days Of ML - LOG

## Day 1 : March 1 , 2020
 
**Today's Progress** : I have started to read again the [Machine Learning for Humans](https://medium.com/machine-learning-for-humans/why-machine-learning-matters-6164faf1df12) articles, and started to get a grasp of linear regression. I understand the very basic math of having a single feature and figuring out the learnign algorithm.

**Thoughts** : Tomorrow I need to get into coding mode and implement some learning algorithms what I researched today.

**Tasks for the upcomming days** :
 + Implement linear regression for a single feature in Python
 - Implement linear regression for three freatures in Python
 - Implement gradient descent
 - Play with the Boston Housing dataset
 - Dig deeper in the math with the 'An Introduction into Statistical Learning'

**Interesting links and arcticles**:
 - kaggle.com
 - www.drivendata.org
 - https://github.com/zdhiman/100days-ml/tree/master/2018
 - https://github.com/Avik-Jain/100-Days-Of-ML-Code

## Day 4: March 9, 2020

I coded the linear regression by hand - i.e.: minimizing the cost function.
Also I was able to achieve the same reuslt, by implementing an algebra math closed form solution, found on internet.
I managed to get Spyder and anaconda run on my mini laptop after some sweat.


## Day 5: March 15, 2020

Today I will implement the gradient descent, and peek into ther solutions /
usage of libraries!

I need to create a blog - I will just use markdwodn and copy all my stuff to Dev.to

The unreasonable efectiveness of Data:

The paper, which I am reading argues, that the current translation engines are using only memorization
of phareses from the source language to the target language, yet are more powerfull, than the previous
generation of them, which were depending on heavy semantic and syntactic rules.

Scene completetion - remove an unwanted car or a ex-spouse from a photo and fill it up with pixels taken
from a large corpus of other photos. Their algorithms performed better on larger set of photos.

!! Curse of dimensionality and overfitting models to data --> throwing away rare events is almost always a bad idea,
because data consists are idividually rare, but collectively frequent.

Natural language processing - finding synonyms: If we observe in a large corpus A and B, which are rarely occur together,
but allways occurt in the neightbourhood of the same words, that means, that A and B are likely to be synonyms.

Follow data - choose a representation which can be used for unsupervices learning, as unlabeled data is more plentiful,
than labelled data! With very large data sources the data holds a lot of details, so use a non-paremetric model.

## March 20, 2020 - Friday

logistic regression and Support Vector machines
Both of them are paramteric models and serve to solve classification problems

logistic model: sigmoid function to make sure, that the end result will be [0,1]
SVM: geometrical thinking about the problem
	- define a cost function for the optimization problem and let it have some cost
	- throw data to higher dimensions.

Tomorrow I would like to apply the data explanatory on the Boston Housing Data set

___________________________________

## March 28th, 2020 - Saturday

I've started a MOOC - the Analytivcs Edge from MIT. They teach me how to R :)!

Nifty R functions:
	c() --> create arrays (only one type / array is allowed)
			Country.Names = c("Great Britain", "USA", "Australia")

	data.frame() -> Create a dataframe
			CountryHealthCare = data.frame(Country.Names, HospitalsPerThousandCitizen)

	str(MyDataFrame) --> gives the structure of the dataframe. Describes the columns and gives some hints.

	summary(MyDataFrame) --> Gets numerical basic analysis about the data for a dataframe (Min, Max, Quartiles). 

	rbind(MyDataFrame1, MyDataFrame2) --> pushes two dataframes to one

	ShitEuropeanCountries = subset(CountryHealthCare, Region == "Europe" & HospitalsPerThousandCitizen < 0.01)
	^ this one creates a subset of data based on the conditions

	getwd(), setwd() --> get and set the working directory
	read.csv(), write.csv() --> read or reate CSV files in the working directory

	which.min(CountryHealthCare$HospitalsPerThousandCitizen) --> gets the row where the HospitalsPerThousandCitizen is the min
	which.max()

	CountryHealthCare$Country[1] --> gets the first row's Country

	plot(CountryHealthCare$GDP, CountryHealthCare$HospitalsPerThousandCitizen) --> creates a scatterplot

	myDataFrame[c("FirtsFavoriteColumn", "SecondFavoriteColumn", "ThirdFavoriteColumn")] --> Select multiple columns
	from the dataframe

	Histogram: Usefull to understand the distribution of a variable. --> hist(WHO$CellularUsage)

	Box Plot: Usefull to understand the statistical range of a variable.
				Box size --> area between 1st quartile and 3rd quartile. The horizontal line is the median.
				The vertical line shows the min-max and the circles are outliers 

				Inter cortal range --> height or the box --> 1st qu - 3rd qu
				Outlier greater then 3rd qu + inter cortal range or less then the 1st qu - inter cortal range

			boxplot(WHO$LifeExpectancy ~ WHO$Region)

	Adding labels:
		boxplot(WHO$LifeExpectancy ~ WHO$Region, xlab="", ylab="Life Expectancy", main="Life Expectancy of Countries by Region")

