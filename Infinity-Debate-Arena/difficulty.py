# Configuration for different difficulty modes in the Infinity Debate Arena game.
# Feel free to modify the strategies and time limits as needed.


DIFFICULTY_MODES = {
    "1": {
        "name": "Beginner",
        "strategy": "Debate politely and explain reasoning clearly.",
        "time_limit": 60
    },
    "2": {
        "name": "Advanced",
        "strategy": "Challenge assumptions and demand logical rigor.",
        "time_limit": 40
    },
    "3": {
        "name": "Expert",
        "strategy": (
            "Be aggressive and adversarial. Expose logical fallacies "
            "and punish weak arguments."
        ),
        "time_limit": 20
    }
}
