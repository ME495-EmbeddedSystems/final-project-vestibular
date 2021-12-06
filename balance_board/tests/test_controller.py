
import rospy
import unittest
from board_pid import BoardPid

class ControllerTest(unittest.TestCase):
    def testcontrollerforzero(self):
        Kp = 0
        Ki = 0 
        Kd = 0
        target = 255
        controller = BoardPid(
            kp=Kp,
            kd=Kd,
            ki = Ki,
            target=target
        )

        value = 2
        self.assertEquals(controller.get(value),0)

    def testcontrollertargetzero(self):
        """ Test for when target and current position is the same
        """
        Kp = 32
        Ki = 4
        Kd = 1
        target = 255
        controller = BoardPid(
            kp=Kp,
            kd=Kd,
            ki = Ki,
            target=target
        )

        value = 255
        self.assertEquals(controller.get(value),0)



if __name__ == "__main__":
    import rosunit
    rosunit.unitrun('balance_board', 'ControllerTest', ControllerTest)