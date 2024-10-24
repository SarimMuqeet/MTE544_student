# For trajectory point range:
import numpy as np

# Type of planner
POINT_PLANNER=0; TRAJECTORY_PLANNER=1

# Type of trajector
PARABOLA=0; SIGMOID=1

class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self, goalPoint=[-1.0, -1.0]):
        
        if self.type==POINT_PLANNER:
            return self.point_planner(goalPoint)
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()


    def point_planner(self, goalPoint):
        x = goalPoint[0]
        y = goalPoint[1]
        return x, y

    # TODO Part 6: Implement the trajectories here
    def trajectory_planner(self):
        trajectory_points = []
        
        # Hardcoded for now
        trajectory_type = PARABOLA

        if trajectory_type == PARABOLA:
            # Parabola: y = x^2, x in [0.0, 1.5]
            #i + 0.1 = 1.6 so 1.5 is last point in list
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
        
        
        #pass
        # the return should be a list of trajectory points: [ [x1,y1], ..., [xn,yn]]
        # return 

