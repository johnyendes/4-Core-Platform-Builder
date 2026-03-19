from typing import Dict, Any, List

def generate_bot_core(bot_name: str, purpose: str, audience: str) -> Dict[str, Any]:
    return {
        "bot_name": bot_name,
        "purpose": purpose,
        "audience": audience,
        "summary": f"{bot_name} is designed to {purpose} for {audience}."
    }


def generate_bot_intents(intents: List[str]) -> Dict[str, Any]:
    intent_list = []
    for intent in intents:
        intent_list.append({
            "intent": intent,
            "description": f"User intent: {intent}."
        })
    return {"intents": intent_list}


def generate_bot_responses(intent_response_map: Dict[str, str]) -> Dict[str, Any]:
    responses = []
    for intent, response in intent_response_map.items():
        responses.append({
            "intent": intent,
            "response": response
        })
    return {"responses": responses}


def generate_bot_actions(actions: Dict[str, str]) -> Dict[str, Any]:
    """
    Example actions:
    {
        "lookup_order": "Call API /orders/{id}",
        "book_call": "Open scheduler page"
    }
    """
    action_list = []
    for name, description in actions.items():
        action_list.append({"action": name, "description": description})
    return {"actions": action_list}


def generate_bot_flow(steps: List[str]) -> Dict[str, Any]:
    """
    Simple conversation flow represented as an ordered list:
    ['greeting', 'ask_question', 'present_solution', 'close']
    """
    flow = []
    for index, step in enumerate(steps):
        flow.append({"step": index + 1, "name": step})
    return {"conversation_flow": flow}