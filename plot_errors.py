import matplotlib.pyplot as plt
from utilities import FileReader

PLOT_TRAJECTORY = True

def plot_errors(filename):
    
    headers, values=FileReader(filename).read_file()
    
    time_list=[]
    
    first_stamp=values[0][-1]
    
    for val in values:
        time_list.append(val[-1] - first_stamp)

    if not PLOT_TRAJECTORY:
        fig, axes = plt.subplots(1,2, figsize=(14,6))
        fig.suptitle("Sigmoid: Angular Plots of Robot State Space and Individual Errors")

        axes[0].plot([lin[0] for lin in values], [lin[1] for lin in values])
        # axes[0].set_title("angular state space (e vs e_dot)")
        axes[0].grid()
           
        axes[0].set_xlabel('e_dot')
        axes[0].set_ylabel('e')
        axes[1].set_title("individual state vs time (angular)")
        for i in range(0, len(headers) - 1):
            axes[1].plot(time_list, [lin[i] for lin in values], label= headers[i]+ " angular")
        
        axes[1].legend()
        axes[1].grid()
        axes[1].set_xlabel('time (s)')
        axes[1].set_ylabel('value (m, m/s , m/^2 )')
        axes[0].legend()


    #plotting trajectory now
    if PLOT_TRAJECTORY:
        fig, axes = plt.subplots(1,1, figsize=(14,6))
        fig.suptitle("Plot of Robot xy Location and Commanded Sigmoid Trajectory ")
        axes.plot([lin[0] for lin in values], [lin[1] for lin in values], label='Robot Pose')
        # axes[0].set_title("angular state space (e vs e_dot)")
        axes.grid()
        
        axes.set_xlabel('x')
        axes.set_ylabel('y')
        headers, values=FileReader("trajectory.csv").read_file()
        axes.plot([lin[0] for lin in values], [lin[1] for lin in values], label ='Commanded Trajectory')
        axes.legend()

    plt.show()
    
    





import argparse

if __name__=="__main__":

    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--files', nargs='+', required=True, help='List of files to process')
    
    args = parser.parse_args()
    
    print("plotting the files", args.files)

    filenames=args.files
    for filename in filenames:
        plot_errors(filename)



