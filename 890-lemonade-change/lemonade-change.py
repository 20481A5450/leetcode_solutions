class LemonadeStand:
    def __init__(self):
        self.fives = 0
        self.tens = 0

    def can_provide_change(self, bills):
        for bill in bills:
            if not self.process_transaction(bill):
                return False
        return True

    def process_transaction(self, bill):
        if bill == 5:
            self.fives += 1
            return True
        elif bill == 10:
            if self.fives == 0:
                return False
            self.fives -= 1
            self.tens += 1
            return True
        elif bill == 20:
            return self.provide_change_for_20()
        else:
            raise ValueError("Invalid bill")

    def provide_change_for_20(self):
        if self.tens > 0 and self.fives > 0:
            self.tens -= 1
            self.fives -= 1
        elif self.fives >= 3:
            self.fives -= 3
        else:
            return False
        return True

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        return LemonadeStand().can_provide_change(bills)