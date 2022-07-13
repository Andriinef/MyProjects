""" A magician in the subway showed you a trick, he put an ice brick in a bottle to impress you. The brick's length and width are equal, forming a square; its height may be different. Just for fun and also to impress the magician and people around, you decided to calculate the brick's volume. Write a function iceBrickVolume that will accept these parameters:
    radius - bottle's radius (always > 0);
    bottleLength - total bottle length (always > 0);
    rimLength - length from bottle top to brick (always < bottleLength);
    And return volume of ice brick that magician managed to put into a bottle.
"""


def ice_brick_volume(radius, bottle_length, rim_length):
    if radius > 0 and bottle_length > 0 and rim_length< bottle_length:
        # brick_volume = 2 * radius**2 * (bottle_length - rim_length)
        # return brick_volume
        return (bottle_length - rim_length) * 2 * radius ** 2


r = (ice_brick_volume(1, 10, 2), 16)
r2 = (ice_brick_volume(50, 43, 12), 1150)
print(r)
print(r2)
