'''
Understanding:
Use the bubble sorting method

The objective of the sorting robot is to take a list and sort the integers from lowest to highest. 

 The robot is given alist and then it can move left or right to evaluate the value. 
 The initial position is at index 0, initial item value is none. 
 
Planning:
Need to turn the Light On to start and turn the light off to stop



'''

class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"
    


    def sort(self):
        """
        Sort the robot's list.
        if self.light_is_on is false:
            self.set_light_on()
        
        Move to the end of the list and swap the last value with none
        Then return to the begining and compare the first value with the current item. 
        
        if that is 1 then swap it and move back to the beginning. if it is 0 or -1 keep it and move right one then call the function again.


        """

        # while True:
        #     self.set_light_off()
        #     while self.can_move_right():
        #         self.swap_item()
        #         self.move_right()
        #         if self.compare_item() == 1:
        #             self.swap_item()
        #             self.set_light_on()
        #         self.move_left()
        #         self.swap_item()
        #         self.move_right()
        #     if not self.light_is_on():
        #         break
        #     while self.can_move_left():
        #         self.move_left()
        
        
        self.set_light_on() # Turning the light on
        self.swap_item() # swapping none for initial value
        while self.light_is_on(): # while the light is on do the following
            self.set_light_off() # Turn the light off
            while self.can_move_right(): # While the robot is capable of moving right
                self.move_right() # move right one space
                if self.compare_item() == 1: #compare item if the returned value is 1 move to line 103 else move to line 104
                    self.set_light_on() # turn light on and move to line 106
                elif self.compare_item() == -1: # if value returned is -1 move to line 105 otherwise move to line 106
                    self.swap_item() # swap the item at the current position
            while self.can_move_left(): # while the robot can move left
                if self.compare_item() == 1: # compare the item at the current position. if the value returned is 1 move to line 108 else move to line 109
                    self.swap_item() # swap the item at the current position
                elif self.compare_item() == -1: # compare the item at the current postion. if the value returned is -1 move to line 110 else move to line 11
                    self.set_light_on() # set the light to on
                self.move_left() # move left one space and repeat loop on line 98
        self.swap_item() # swap the item at current position when the light is turned of and loop on 98 is finished

        # self.set_light_on()
        # # self.swap_item()
        # while self.can_move_right() is True:
        #     self.move_right()
        
        # if self.can_move_right() is False:
        #     self.swap_item()

        # while self.can_move_left() is True:
        #     self.move_left()

        # self.sort_again()
        # print("item", self._item)
        # print("position", self._position)
        # self.set_light_off()  




        # Fill this out
        # if self.light_is_on() is False:
        #     self.set_light_on()
        
        # while self.can_move_right() is True:
        #     self.move_right()
        
        # if self.can_move_right() is False:
        #     self.swap_item()

        # while self.can_move_left() is True:
        #     self.move_left()

        # print("item", self._item)
        # print("position", self._position)
        





if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    # l= [1,2,3,4,5,6]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)