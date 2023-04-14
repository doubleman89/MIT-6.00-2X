# -*- coding: utf-8 -*-
# Problem Set 5: Experimental Analysis
# Name: 
# Collaborators (discussion):
# Time:

import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
import numpy
import random
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHILADELPHIA',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE',
    'SAN JUAN',
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2010)
TESTING_INTERVAL = range(2010, 2016)

"""
Begin helper code
"""
class Climate(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Climate instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d pylab array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return pylab.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by a linear
            regression model
        model: a pylab array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = pylab.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        degs: a list of degrees of the fitting polynomial

    Returns:
        a list of pylab arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    # TODO
    models = []
    for deg in degs:
        model =pylab.polyfit(x,y,deg)
        models.append(model)
    
    return models

def r_squared(y, estimated):
    """
    Calculate the R-squared error term.
    
    Args:
        y: 1-d pylab array with length N, representing the y-coordinates of the
            N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the R-squared error term
    """
    # calculate mean
    yMean = sum(y)/len(y)
    #return sum((y-yMean)**2)/sum((estimated-yMean)**2)
    return 1- sum((y-estimated)**2)/sum((y-yMean)**2)
    
def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model with the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_ove+r_slope). 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    rSquared = None
    bestModel = None
    bestEstYVals = None
    for model in models:
        estY = pylab.polyval(model,x)
        rSquaredModel = r_squared(y,estY) 
        if rSquared == None or rSquaredModel >rSquared :
            rSquared =  round(rSquaredModel,5)
            bestModel = model
            bestEstYVals= estY

    # generate text for se/slope ratio 
    seText =""
    bestModelDegree =len(bestModel)-1
    if bestModelDegree == 1 :
        se = round(se_over_slope(x,y,bestEstYVals,bestModel),5)
        seText = "and with SE/slope ratio " + str(se)

    plt.plot(x,y,"bo",label="plot data")
    plt.plot(x,bestEstYVals,"r", label = "best fit curve with degree " + str(bestModelDegree) + ", r2 = " + str(rSquared)  + seText)
    plt.xlabel("date")
    plt.ylabel("temperature")
    plt.legend(loc="best")

def gen_cities_avg(climate : Climate, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """

    means =[[]for i in range(len(years))]
    
    for j in range(len(years)):
        for city in multi_cities:
            year = years[j]
            yearlyTemps = climate.get_yearly_temp(city,year)
            means[j].append(sum(yearlyTemps)/len(yearlyTemps))
        # calculate mean for specific year            
        means[j] = sum(means[j])/len(means[j])

    return pylab.array(means)

def moving_average(y, window_length):
    """
    Compute the moving average of y with specified window length.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        window_length: an integer indicating the window length for computing
            moving average

    Returns:
        an 1-d pylab array with the same length as y storing moving average of
        y-coordinates of the N sample points
    """
    yMA = []
    for i in range(len(y)): 
        # check how many points can be collected for moving average
        
        if i-window_length < 0: 
            startIndex = 0
            collectedPoints = i+1
        else:
            startIndex =  i-window_length+1
            collectedPoints = window_length
        yMA.append(sum(y[startIndex:(i+1)])/abs(collectedPoints))          

    return pylab.array(yMA)         

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d pylab array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    return (sum((y-estimated)**2)/len(y))**0.5

def gen_std_devs(climate :Climate, multi_cities, years):
    """
    For each year in years, compute the standard deviation over the averaged yearly
    temperatures for each city in multi_cities. 

    Args:
        climate: instance of Climate
        multi_cities: the names of cities we want to use in our std dev calculation (list of str)
        years: the range of years to calculate standard deviation for (list of int)

    Returns:
        a pylab 1-d array of floats with length = len(years). Each element in
        this array corresponds to the standard deviation of the average annual 
        city temperatures for the given cities in a given year.
    """
    std =[[]for i in range(len(years))]
    
    for j in range(len(years)):
        for city in multi_cities:
            year = years[j]
            yearlyTemps = climate.get_yearly_temp(city,year)
            std[j].append(yearlyTemps)
        # calculate mean for specific day
        std[j] = numpy.mean(std[j],axis=0)    
        # calculate std for specific year                
        std[j] = numpy.std(std[j])
    return pylab.array(std)

def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model’s estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: an 1-d pylab array with length N, representing the x-coordinates of
            the N sample points
        y: an 1-d pylab array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a pylab array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    rmseVal = None
    bestModel = None
    bestEstYVals = None
    for model in models:
        estY = pylab.polyval(model,x)
        rmseModdel =  rmse(y,estY) 
        if rmseVal == None or rmseModdel <rmseVal :
            rmseVal =  rmseModdel
            bestModel = model
            bestEstYVals= estY
        #plt.plot(x,estY, label = "curve with degree " + str(len(model)-1) + "with rmse :" + str(rmseModdel))

    # generate text for se/slope ratio 
    bestModelDegree =len(bestModel)-1
    plt.plot(x,y,"bo",label="plot data")
    plt.plot(x,bestEstYVals,"r", label = "best fit curve with degree " + str(bestModelDegree) + "with rmse :" + str(rmseVal))
    plt.xlabel("date")
    plt.ylabel("temperature")
    plt.legend(loc="best")


if __name__ == '__main__':

    climate = Climate("data.csv")
    ######### Part A.4 #######################
    notRandomSamples =[]
    # samples from january 10th
    # for year in TRAINING_INTERVAL:
    #     notRandomSamples.append( climate.get_daily_temp("NEW YORK",1,10,year) )

    # x = pylab.array(TRAINING_INTERVAL)
    # y = pylab.array(notRandomSamples)
    # models = generate_models(x,y,[1] )
    # evaluate_models_on_training(x,y,models)
 
 
    # annual temperature for NY

    # x = pylab.array(TRAINING_INTERVAL)
    # y = pylab.array(gen_cities_avg(climate, ["NEW YORK"], TRAINING_INTERVAL))
    # models = generate_models(x,y,[1] )
    # evaluate_models_on_training(x,y,models)    

    ############ Part B ##########################
    # x = pylab.array(TRAINING_INTERVAL)
    # y = pylab.array(gen_cities_avg(climate, CITIES, TRAINING_INTERVAL))
    # ##randomCities = random.sample(CITIES,20)
    # ##y = pylab.array(gen_cities_avg(climate, randomCities, TRAINING_INTERVAL))
    # models = generate_models(x,y,[1] )
    # evaluate_models_on_training(x,y,models)   

    ############ Part C ###########
    # x = pylab.array(TRAINING_INTERVAL)
    # y = pylab.array(gen_cities_avg(climate, CITIES, TRAINING_INTERVAL))
    # yMA=moving_average(y,5)
    # models = generate_models(x,yMA,[1] )
    
    # evaluate_models_on_training(x,yMA,models)   
    # Part D.2.I
    #generate training data samples from MA 
#     x = pylab.array(TRAINING_INTERVAL)
#     y = pylab.array(gen_cities_avg(climate, CITIES, TRAINING_INTERVAL))
#     yMA=moving_average(y,5)
#    #generate training data samples from NY data
#     # x = pylab.array(TRAINING_INTERVAL)
#     # yMA = pylab.array(gen_cities_avg(climate, ["NEW YORK"], TRAINING_INTERVAL))
 

#     models = generate_models(x,yMA,[1,2,20] )
#     # evaluate_models_on_training(x,yMA,models) 
    
#     # Part D.2.II
#     # generate test data samples 
#     x = pylab.array(TESTING_INTERVAL)
#     y = pylab.array(gen_cities_avg(climate, CITIES, TESTING_INTERVAL))
#     yMA=moving_average(y,5)
#     evaluate_models_on_testing(x,yMA,models)  

    # Part E
    # compute standard deviation for the training set


    

    x = pylab.array(TRAINING_INTERVAL)
    y = gen_std_devs(climate,CITIES,TRAINING_INTERVAL)
    # compute MA for calculated SD
    yMA=moving_average(y,5)
    models = generate_models(x,yMA,[1] )
    evaluate_models_on_training(x,yMA,models) 
