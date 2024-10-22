from math import atan2, asin, sqrt

M_PI=3.1415926535

class Logger:
    
    def __init__(self, filename, headers=["e", "e_dot", "e_int", "stamp"]):
        
        self.filename = filename

        with open(self.filename, 'w') as file:
            
            header_str=""

            for header in headers:
                header_str+=header
                header_str+=", "
            
            header_str+="\n"
            
            file.write(header_str)


    def log_values(self, values_list):

        with open(self.filename, 'a') as file:
            
            vals_str=""
            
            for value in values_list:
                vals_str+=f"{value}, "
            
            vals_str+="\n"
            
            file.write(vals_str)
            

    def save_log(self):
        pass

class FileReader:
    def __init__(self, filename):
        
        self.filename = filename
        
        
    def read_file(self):
        
        read_headers=False

        table=[]
        headers=[]
        with open(self.filename, 'r') as file:

            if not read_headers:
                for line in file:
                    values=line.strip().split(',')

                    for val in values:
                        if val=='':
                            break
                        headers.append(val.strip())

                    read_headers=True
                    break
            
            next(file)
            
            # Read each line and extract values
            for line in file:
                values = line.strip().split(',')
                
                row=[]                
                
                for val in values:
                    if val=='':
                        break
                    row.append(float(val.strip()))

                table.append(row)
        
        return headers, table
    
    

# TODO Part 3: Implement the conversion from Quaternion to Euler Angles
def euler_from_quaternion(quat):
    """
    Convert quaternion (w in last place) to euler roll, pitch, yaw.
    quat = [x, y, z, w]
    """

    w = quat[3]
    x = quat[0]
    y = quat[1]
    z = quat[2]

    # quaternion_to_rMatrix = [
    #     [(w ** 2) + (x ** 2) - (y ** 2) - (z ** 2), (2(x*y - w*z)), 2(w*y + x*z)],
    #     [(2(w*z - x*y)), (w ** 2) - (x ** 2) + (y ** 2) - (z ** 2), (2(y*z - w*x))],
    #     [(2(x*z - w*y)), (2(w*x + y*z)), (w ** 2) - (x ** 2) - (y ** 2) + (z ** 2)],
    # ]

    # roll (x-axis rotation)
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = atan2(sinr_cosp, cosr_cosp)

    # pitch (y-axis rotation)
    pitch = asin(2*(w * y - x * z))
    # sinp = sqrt(1 + 2 * (q.w * q.y - q.x * q.z))
    # cosp = sqrt(1 - 2 * (q.w * q.y - q.x * q.z))
    # pitch = 2 * tan2(sinp, cosp) - M_PI / 2

    # yaw (z-axis rotation)
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = atan2(siny_cosp, cosy_cosp)

    # just unpack yaw
    return yaw



#TODO Part 4: Implement the calculation of the linear error
def calculate_linear_error(current_pose, goal_pose):
        
    # Compute the linear error in x and y
    # Remember that current_pose = [x,y, theta, time stamp] and goal_pose = [x,y]
    # Remember to use the Euclidean distance to calculate the error.
    curr_x = current_pose[0]
    curr_y = current_pose[1]
    goal_x = goal_pose[0]
    goal_y = goal_pose[1]
    error_linear = sqrt((curr_x - goal_x) ** 2 + (curr_y - goal_y) ** 2)

    return error_linear

#TODO Part 4: Implement the calculation of the angular error
def calculate_angular_error(current_pose, goal_pose):

    # Compute the linear error in x and y
    # Remember that current_pose = [x,y, theta, time stamp] and goal_pose = [x,y]
    # Use atan2 to find the desired orientation
    # Remember that this function returns the difference in orientation between where the robot currently faces and where it should face to reach the goal

    error_angular = atan2(goal_pose[1] - current_pose[1], goal_pose[0] - current_pose[0])

    # Remember to handle the cases where the angular error might exceed the range [-π, π]
    if error_angular< - M_PI:
        error_angular = (-1*error_angular) % M_PI
    elif error_angular > M_PI:
        error_angular %= M_PI
    
    return error_angular
