from game import RPS

name = input("\nHello, enter your name: ")


def rps_run(user_name, wanna_play=True, first_time=True):

    while wanna_play:
        game = RPS(user_name)
        if first_time:
            game.print_welcome_message()
            game.print_rules()

        game.get_and_set_user_move()
        game.get_and_set_python_move()
        game.get_winner()
        game.print_winner()

        play = game.play_again()

        return rps_run(name, play, False)

    print("\nThanks for playing, see you next time!")


if __name__ == "__main__":
    rps_run(name)
