import numpy as np
import csv

PARABOLA = 0
SIGMOID = 1

class TrajectoryGenerator:
    def trajectory_planner(self):
        trajectory_points = []
        
        # Hardcoded for now
        trajectory_type = PARABOLA  # Change to SIGMOID to test the other trajectory

        if trajectory_type == SIGMOID:
            # Parabola: y = x^2, x in [0.0, 1.5]
            for i in np.arange(0.0, 1.6, 0.1):
                x_val = i
                y_val_parabola = x_val ** 2
                trajectory_points.append([x_val, y_val_parabola])

        elif trajectory_type == SIGMOID:
            # Sigmoid: σ(x) = 2 / (1 + e^(-2x)) - 1, x in [0.0, 2.5]
            for i in np.arange(0.0, 2.6, 0.1):
                x_val = i
                y_val_sigmoid = (2 / (1 + np.exp(-2 * x_val))) - 1
                trajectory_points.append([x_val, y_val_sigmoid])

        return trajectory_points

    def save_trajectory_to_csv(self, filename):
        trajectory_points = self.trajectory_planner()
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['x', 'y'])  # Write the header
            writer.writerows(trajectory_points)  # Write the trajectory points

if __name__ == "__main__":
    generator = TrajectoryGenerator()
    generator.save_trajectory_to_csv('trajectory.csv')
    print("Trajectory data saved to 'trajectory.csv'.")
