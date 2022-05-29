import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv
import random

df = pd.read_csv('data.csv')
data = df['reading_time'].tolist()

pop_mean = statistics.mean(data)
pop_stdev = statistics.stdev(data)
print('The POPULATION mean is: ', pop_mean)
print('The POPULATION standard deviation is: ', pop_stdev)

def sets_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def plot_graph(mean_list):
    df = mean_list
    #orginal(population)
    fig = ff.create_distplot([df], ['Normal Distribution'], show_hist= False)

    first_stdev_start, first_stdev_end = pop_mean - pop_stdev, pop_mean + pop_stdev
    second_stdev_start, second_stdev_end = pop_mean - (2*pop_stdev), pop_mean + (2*pop_stdev)
    third_stdev_start, third_stdev_end = pop_mean - (3*pop_stdev), pop_mean + (3*pop_stdev)

    fig.add_trace(go.Scatter(x = [pop_mean, pop_mean], y = [0, 0.7], mode = 'lines', name = 'Population Mean'))
    fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.7], mode = 'lines', name = 'First Standard Deviation Start'))
    fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.7], mode = 'lines', name = 'First Standard Deviation End'))
    fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.7], mode = 'lines', name = 'Second Standard Deviation Start'))
    fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.7], mode = 'lines', name = 'Second Standard Deviation End'))
    fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0, 0.7], mode = 'lines', name = 'Third Standard Deviation Start'))
    fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.7], mode = 'lines', name = 'Third Standard Deviation End'))


    #intervention(sample)
    df2 = pd.read_csv('intervention_data.csv')
    data = df2['reading_time'].tolist()
    intervention_mean = statistics.mean(data)
    print('The INTERVENTION mean is: ', intervention_mean)
    fig = ff.create_distplot([mean_list], ['Sample Distribution'], show_hist = False)
    fig.add_trace(go.Scatter(x = [intervention_mean, intervention_mean], y = [0, 0.7], mode = 'lines', name = 'Sample Mean'))

    fig.add_trace(go.Scatter(x = [first_stdev_start, first_stdev_start], y = [0, 0.7], mode = 'lines', name = 'First Standard Deviation Start'))
    fig.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.7], mode = 'lines', name = 'First Standard Deviation End'))
    fig.add_trace(go.Scatter(x = [second_stdev_start, second_stdev_start], y = [0, 0.7], mode = 'lines', name = 'Second Standard Deviation Start'))
    fig.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.7], mode = 'lines', name = 'Second Standard Deviation End'))
    fig.add_trace(go.Scatter(x = [third_stdev_start, third_stdev_start], y = [0, 0.7], mode = 'lines', name = 'Third Standard Deviation Start'))
    fig.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.7], mode = 'lines', name = 'Third Standard Deviation End'))


    z_score = (pop_mean - intervention_mean)/pop_stdev
    print('The z_score is: ', z_score)

    fig.show()






def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_mean = sets_of_means(30)
        mean_list.append(set_of_mean)
    

    sample_mean = statistics.mean(mean_list)
    sample_stdev = statistics.stdev(mean_list)
    print('The SAMPLE mean is: ', sample_mean)
    print('The SAMPLE standard deviation is: ', sample_stdev)
    plot_graph(mean_list)


setup()