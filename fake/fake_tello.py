
class FakeTello:
  def __init__(self):
    print("FakeTello inited")
    
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
  
  def move_left(self, x: int):
    print("move_left")
    
  def send_rc_control(self, left_right_velocity, forw_back_velocity,
                                       up_down_velocity, yaw_velocity):
    print(f"send_rc_control left_right_velocity:{left_right_velocity}, forw_back_velocity:{forw_back_velocity},\
        up_down_velocity:{up_down_velocity}, yaw_velocity:{yaw_velocity}")