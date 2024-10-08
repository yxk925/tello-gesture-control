import rospy
from agents.move_agent import MoveAgent


class TelloGestureController:
    def __init__(self, move_agent: MoveAgent):
        self.move_agent = move_agent
        self._is_landing = False

        # RC control velocities
        self.forw_back_velocity = 0
        self.up_down_velocity = 0
        self.left_right_velocity = 0
        self.yaw_velocity = 0

    def gesture_control(self, gesture_buffer):
        gesture_id = gesture_buffer.get_gesture()
        
        if gesture_id is None:
            return
        
        print("got GESTURE", gesture_id)

        if not self._is_landing:
            if gesture_id == 0:  # Forward
                self.move_agent.stop()
            elif gesture_id == 1:  # STOP
                rospy.loginfo("Unsupport STOP")
                #self.move_agent.stop()
            if gesture_id == 5:  # Back
                self.move_agent.forward(0.3)

            elif gesture_id == 2:  # UP
                self.move_agent.backward(0.3)
            elif gesture_id == 4:  # DOWN
                rospy.loginfo("Unsupport DOWN")
                

            elif gesture_id == 3:  # LAND
                rospy.loginfo("Unsupport LAND")

            elif gesture_id == 6: # LEFT
                self.move_agent.turnLeft()
            elif gesture_id == 7: # RIGHT
                self.move_agent.turnRight()
            elif gesture_id == -1:
                rospy.loginfo("Unsupported gesture id:-1")
            else:
                rospy.loginfo("Unknown gesture id %d", gesture_id)
                
                

