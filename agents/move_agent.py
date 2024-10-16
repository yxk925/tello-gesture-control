import rospy
from diffbot_msgs.msg import MoveCmd

class MoveAgent:
  def __init__(self):
    print("MoveAgent init")
    self.pub = rospy.Publisher('move_master/cmd', MoveCmd, queue_size=10)
    
  def connect(self):
    return
    
  def streamon(self):
    print("streamon")
    return
  
  def get_frame_read(self):
    print("NOT implemented!!!")
  
  def move_down(self, x: int):
    print("move down", x)
    
  def takeoff(self):
    print("takeoff")
    
  def land(self):
    print("land")
    
  def forward(self, distance):
    rospy.loginfo("forward %f", distance)
    cmd = MoveCmd()
    cmd.cmd = MoveCmd.kForward
    cmd.param = str(distance)
    self.pub_cmd(cmd)
    
  def backward(self, distance):
    rospy.loginfo("backward %f", distance)
    cmd = MoveCmd()
    cmd.cmd = MoveCmd.kBackward
    cmd.param = str(distance)
    self.pub_cmd(cmd)
    
  def turnLeft(self, angle):
    rospy.loginfo("turn left %f", angle)
    cmd = MoveCmd()
    cmd.cmd = MoveCmd.kTurnLeft
    cmd.param = str(angle)
    self.pub_cmd(cmd)
  
  def turnRight(self, angle):
    rospy.loginfo("turn right %f", angle)
    cmd = MoveCmd()
    cmd.cmd = MoveCmd.kTurnRight
    cmd.param = str(angle)
    self.pub_cmd(cmd)
  
  def stop(self):
    rospy.loginfo("stop")
    cmd = MoveCmd()
    cmd.cmd = MoveCmd.kStop
    self.pub_cmd(cmd)
    
  def pub_cmd(self, cmd):
    rospy.loginfo("pub_cmd %d:%s", cmd.cmd, cmd.param)
    self.pub.publish(cmd)
    
  def send_rc_control(self, left_right_velocity, forw_back_velocity,
                                       up_down_velocity, yaw_velocity):
    print(f"send_rc_control left_right_velocity:{left_right_velocity}, forw_back_velocity:{forw_back_velocity},\
        up_down_velocity:{up_down_velocity}, yaw_velocity:{yaw_velocity}")