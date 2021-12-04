
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


if __name__ == "__main__":
    import rosunit
    rosunit.unitrun('balance_board', 'ControllerTest', ControllerTest)