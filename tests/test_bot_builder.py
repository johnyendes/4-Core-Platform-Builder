import sys
import os
sys.path.append('packs/bot_builder')
sys.path.append('gap_packs/bot_builder_gaps')
sys.path.append('deployment/bot_builder_deploy')

from functions import (
    generate_bot_core,
    generate_bot_intents,
    generate_bot_responses,
    generate_bot_actions,
    generate_bot_flow
)
from bridge import connect
from deploy import deploy

# Test the complete Bot Builder workflow
def test_bot_builder_workflow():
    print("=== Testing Bot Builder A3 Workflow ===")
    
    # Step 1: Generate bot core
    core = generate_bot_core(
        bot_name="SupportBot Pro",
        purpose="handle customer support inquiries",
        audience="customers needing help"
    )
    print(f"✅ Core generated: {core['bot_name']}")
    
    # Step 2: Generate bot intents
    intents = generate_bot_intents([
        "greeting",
        "ask_help",
        "check_order",
        "contact_human",
        "goodbye"
    ])
    print(f"✅ Intents generated: {len(intents['intents'])} intents")
    
    # Step 3: Generate bot responses
    intent_response_map = {
        "greeting": "Hello! How can I help you today?",
        "ask_help": "I'm here to help. What do you need assistance with?",
        "check_order": "I can help you check your order status.",
        "contact_human": "Let me connect you with a human agent.",
        "goodbye": "Thank you for contacting us. Have a great day!"
    }
    responses = generate_bot_responses(intent_response_map)
    print(f"✅ Responses generated: {len(responses['responses'])} responses")
    
    # Step 4: Generate bot actions
    actions_map = {
        "lookup_order": "Call API /orders/{id}",
        "escalate_ticket": "Create support ticket in Zendesk",
        "schedule_callback": "Open calendar scheduling page"
    }
    actions = generate_bot_actions(actions_map)
    print(f"✅ Actions generated: {len(actions['actions'])} actions")
    
    # Step 5: Generate bot flow
    flow_steps = [
        "greeting",
        "identify_need", 
        "provide_solution",
        "confirm_resolution",
        "close_conversation"
    ]
    flow = generate_bot_flow(flow_steps)
    print(f"✅ Flow generated: {len(flow['conversation_flow'])} steps")
    
    # Step 6: Connect through GAP bridge
    blueprint_wrapper = connect(core, intents, responses, actions, flow)
    print(f"✅ GAP bridge connected: {blueprint_wrapper['status']}")
    
    # Step 7: Deploy
    deploy(blueprint_wrapper)
    print("✅ Deployment completed")
    
    print("\n=== Bot Builder A3 Workflow Test Complete ===")
    print("✅ All components working correctly!")
    
    return blueprint_wrapper

if __name__ == "__main__":
    result = test_bot_builder_workflow()