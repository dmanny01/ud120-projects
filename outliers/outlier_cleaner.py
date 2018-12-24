#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    data = list()

    ### your code goes here
    for i in range(len(predictions)):
        data.append((ages[i][0], net_worths[i][0],(predictions[i][0]-net_worths[i][0])**2))
        data = list(sorted(data, key = lambda x: x[2]))
    cleaned_data = data[:-int(len(data)*0.1)]
    print 'Total clean data size: ', len(cleaned_data)


    return cleaned_data
