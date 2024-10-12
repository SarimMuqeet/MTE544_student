import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

def plot_distances(filename):
    # Read the file from CSV
    df = pd.read_csv(filename)

    # Pull the values out
    x_vel = df['x'].values
    y_vel = df[' y'].values
    th_pos = df[' th'].values #after converting from quaternions it is already position
    time = df[' stamp'].values  # Assuming time is in nanoseconds

    print(th_pos)

    # Convert time from nanoseconds to seconds
    time = time / 1e9

    # Get position values
    x_pos, y_pos = get_pos_from_vel(x_vel, y_vel, th_pos, time)

    # Plotting x_pos vs y_pos
    plt.scatter(x_pos, y_pos, label="Position")
    plt.title('Robot XY Position from Odom')
    plt.xlabel('Distance (m)')
    plt.ylabel('Distance (m)')
    plt.grid()
    plt.legend()
    plt.show()

def get_pos_from_vel(x_vel, y_vel, th_pos, timestamps):
    # Ensure timestamps are in chronological order
    sorted_indices = np.argsort(timestamps)
    timestamps = timestamps[sorted_indices]
    x_vel = x_vel[sorted_indices]
    y_vel = y_vel[sorted_indices]
    th_pos = th_pos[sorted_indices]

    # Time differences between consecutive timestamps, converted from nanoseconds to seconds
    delta_t = np.diff(timestamps) / 1e9
    
    # Initialize position and orientation arrays (initial positions and orientation are assumed to be zero)
    x_pos = np.zeros(len(x_vel))
    y_pos = np.zeros(len(y_vel))

    # Integrate velocities and orientation
    for i in range(1, len(timestamps)):

        # Transform local velocities to global frame using the orientation
        x_global = x_vel[i-1] * np.cos(th_pos[i-1]) - y_vel[i-1] * np.sin(th_pos[i-1])
        y_global = x_vel[i-1] * np.sin(th_pos[i-1]) + y_vel[i-1] * np.cos(th_pos[i-1])

        # Update positions using transformed velocities
        x_pos[i] = x_pos[i-1] + x_global * delta_t[i-1]
        y_pos[i] = y_pos[i-1] + y_global * delta_t[i-1]
    return x_pos, y_pos


# Main code parse for filename
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a file.')
    parser.add_argument('--file', required=True, help='File to process')
    
    args = parser.parse_args()

    print("Plotting the file:", args.file)
    
    # Plot the data from the single file
    plot_distances(args.file)
