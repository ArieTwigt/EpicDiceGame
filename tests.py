from games.dice import Dice
from games.game import Game
from pytest import raises


def test_max_score():
    # Arrange
    my_dice = Dice(8)
    my_dice_2 = Dice(6)
    # Act
    

    # Assert
    assert my_dice.max_score == 8
    assert my_dice_2.max_score == 6


def test_color():
    # Arrange
    my_dice = Dice(6, color="Yellow")

    # Assert
    assert my_dice.color == "Yellow"


def test_number_throws():
    # Arrange
    my_dice = Dice(6)
    my_game = Game(8, my_dice)

    # Act
    # throw the dice 8 times
    for i in range(0, 8):
        my_game.take_turn()

    # Assert
    assert len(my_game.throws) == 8


def test_type_error_dice():
    # Arrange
    with raises(TypeError):
        my_dice = Dice("Arie")


def test_negative_value_dice():
    with raises(ValueError):
        my_dice = Dice(-10)