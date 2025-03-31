import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/w-ok-e/autonav/install/turtlebot3_teleop'
