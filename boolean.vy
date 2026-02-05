# pragma version 0.4.3
# @license MIT

num: uint256

@deploy
def __init__():
    self.num = 42

@external
def set_num(num: uint256):
    self.num = num

@external
@view
def get_num() -> uint256:
    return self.num
