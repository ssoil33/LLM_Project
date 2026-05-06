from typing import TypedDict, Annotated, List
from langgraph.graph.message import add_messages

class PIDAgentState(TypedDict):
    task: str
    plan: List[str]
    messages: Annotated[list, add_messages]
    detected_symbols: dict
    mto_result: dict
    final_report: str