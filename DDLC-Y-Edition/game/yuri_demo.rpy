# A brief demonstration scene with Yuri talking to the player.

# redefine y here so she speaks in purple and slower
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", what_cps=20, color="#9b59b6")

label start:
    scene bg club

    show yuri 1 at truecenter

    y "Hello... I'm Yuri. Welcome to the Yuri edition of Doki Doki Literature Club."

    "The room feels colder than usual, but the books smell comforting."

    show yuri 2

    y "I hope you enjoy spending some time with me. I'm rather fond of long, introspective conversations."

    menu:
        "Respond kindly":
            "Yuri smiles warmly."
            y "So thoughtful of you... perhaps we can share a book sometime."
        "Say nothing":
            "She seems a little disappointed, but continues speaking anyway."
            y "That's alright. I understand."

    return
