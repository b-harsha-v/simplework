from typing import TypedDict, Optional, List


class SimpleWorkState(TypedDict):

    # user input
    user_message: str

    # detected intent
    intent: Optional[str]

    # planning information
    goal: Optional[str]
    duration: Optional[int]

    # generated outputs
    plan: Optional[str]
    tasks: Optional[List[str]]
    schedule: Optional[List[str]]

    # final response
    response: Optional[str]