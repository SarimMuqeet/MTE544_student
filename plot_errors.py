import matplotlib.pyplot as plt
from utilities import FileReader




def plot_errors(filename):
    
    headers, values=FileReader(filename).read_file()
    
    time_list=[]
    
    first_stamp=values[0][-1]
    
    #convert to seconds from nanoseconds
    for val in values:
        time_list.append((val[-1] - first_stamp) / 1e9)

    
    
    # fig, axes = plt.subplots(1,2, figsize=(14,6))
    fig, axes = plt.subplots(1,1, figsize=(14,6))


    # # state space ---------------------------------------------------------------------
    # axes[0].plot([lin[0] for lin in values], [lin[1] for lin in values])
    # axes[0].set_title("state space")
    # axes[0].set_xlabel("X")  # Set x-axis label
    # axes[0].set_ylabel("Y")  # Set y-axis label
    # axes[0].grid()
    
    # axes[1].set_title("each individual state")
    # for i in range(0, len(headers) - 1):
    #     axes[1].plot(time_list, [lin[i] for lin in values], label= headers[i]+ " linear")

    # axes[1].legend()
    # axes[1].set_xlabel("Time (s)")  # Set x-axis label
    # axes[1].set_ylabel("Errors")  
    # axes[1].grid()


    # #Linear and Angular Errors -------------------------------------------------------------------
    # axes[1].set_title("P: e vs t and e_dot vs t (Linear)")
    # for i in range(0, len(headers) - 2):
    #     axes[1].plot(time_list, [lin[i] for lin in values], label= headers[i]+ " linear")

    # axes[1].legend()
    # axes[1].set_xlabel("Time (s)")  # Set x-axis label
    # axes[1].set_ylabel("Errors")  
    # axes[1].grid()

    # #X, Y, Theta vs T -------------------------------------------------------------------------------
    # axes[1].set_title("PID: x, y, and theta vs time")
    # # for i in range(0, len(headers) - 1):
    # #     axes[1].plot(time_list, [lin[i] for lin in values], label= headers[i])
    # for i, header in enumerate(headers[:-1]):  # Assuming the last two columns are not x, y, or theta
    #     if "x" in header.lower():
    #         unit = " (m)"  # Example unit for x
    #     elif "y" in header.lower():
    #         unit = " (m)"  # Example unit for y
    #     elif "theta" in header.lower():
    #         unit = " (rad)"  # Example unit for theta
    #     else:
    #         unit = ""  # Default to no unit if unrecognized
    #     axes[1].plot(time_list, [lin[i] for lin in values], label=f"{header}{unit}")

    # axes[1].legend()
    # axes[1].set_xlabel("Time (s)")  # Set x-axis label
    # axes[1].set_ylabel("Positional Data")  
    # axes[1].grid()



    # #State Space for X vs Y ---------------------------------------------------------------------------
    # axes[0].plot([lin[0] for lin in values], [lin[1] for lin in values])
    # axes[0].set_title("PID: X vs Y Plot")
    # axes[0].set_xlabel("X (m)")  # Set x-axis label
    # axes[0].set_ylabel("Y (m)")  # Set y-axis label
    # axes[0].grid()

    # # State Space for e vs e_dot ---------------------------------------------------------------------------
    # axes.plot([lin[0] for lin in values], [lin[1] for lin in values])
    # axes.set_title("PID: e vs e_dot Plot (Linear)")
    # axes.set_xlabel("e")  # Set x-axis label
    # axes.set_ylabel("e_dot")  # Set y-axis label
    # axes.grid()


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



