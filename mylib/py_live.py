import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')




#y_vec = np.random.randn(len(x_vec))

def live_plotter(x_vec,y1_data,abnor_data,safe_data,line1,line2,line3,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8,label="Serious Violations",color="red")    
        line2, = ax.plot(x_vec,abnor_data,'-o',alpha=0.8,label="Abnormal Violations",color="Orange")  
        line3, = ax.plot(x_vec,safe_data,'-o',alpha=0.8,label="Safe",color="green")
        #update plot label/title
        plt.title("Real Time Social Distance Detection")
        plt.xlabel("Time")
        plt.ylabel("Violations and Safe's")
        plt.legend()
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    line2.set_ydata(abnor_data)
    line3.set_ydata(safe_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1] or np.min(abnor_data)<=line2.axes.get_ylim()[0] or np.max(abnor_data)>=line2.axes.get_ylim()[1] or np.min(safe_data)<=line3.axes.get_ylim()[0] or np.max(safe_data)>=line3.axes.get_ylim()[1]:
        plt.ylim([min(np.min(y1_data)-np.std(y1_data),np.min(abnor_data)-np.std(abnor_data),np.min(safe_data)-np.std(safe_data)),max(np.max(y1_data)+np.std(y1_data),np.max(abnor_data)+np.std(abnor_data),np.max(safe_data)+np.std(safe_data))])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1,line2,line3

# the function below is for updating both x and y values (great for updating dates on the x-axis)
def live_plotter_xy(x_vec,y1_data,line1,identifier='',pause_time=0.01):
    if line1==[]:
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        line1, = ax.plot(x_vec,y1_data,'r-o',alpha=0.8)
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
        
    line1.set_data(x_vec,y1_data)
    plt.xlim(np.min(x_vec),np.max(x_vec))
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])

    plt.pause(pause_time)
    
    return line1

'''while True:
    rand_val = np.random.randn(1)
    y_vec[-1] = rand_val
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],0.0)'''

