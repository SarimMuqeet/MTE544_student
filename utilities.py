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

            # TODO Part 5: Write the values from the list to the file
            for val in values_list:
                vals_str += str(val) + ", "
            
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
            # Skip the header line

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


# TODO Part 5: Implement the conversion from Quaternion to Euler Angles
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


