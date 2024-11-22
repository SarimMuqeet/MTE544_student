import matplotlib.pyplot as plt
from utilities import FileReader




def plot_errors(filename):
    
    headers, values=FileReader(filename).read_file()
    
    time_list=[]
    
    first_stamp=values[0][-1]
    
    for val in values:
        time_list.append((val[-1] - first_stamp) / 1e9) #to get time in seconds

    
    
    fig, axes = plt.subplots(2,1, figsize=(14,6))


    axes[0].plot([lin[len(headers) - 3] for lin in values], [lin[len(headers) - 2] for lin in values])
    axes[0].set_title("State Space for Q = 0.5, R = 0.2")
    axes[0].set_xlabel("X (m)")  # Set x-axis label
    axes[0].set_ylabel("Y (m)")  # Set y-axis label
    axes[0].grid()

    
    axes[1].set_title("Each individual state for Q = 0.5, R = 0.2")
    for i in range(0, len(headers) - 1):
        axes[1].plot(time_list, [lin[i] for lin in values], label= headers[i])

    axes[1].legend()
    axes[1].set_xlabel("Time (s)")  # Set x-axis label
    axes[1].set_ylabel("Recorded Data")  # Set y-axis label
    axes[1].grid()

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


