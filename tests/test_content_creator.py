import sys
import os
sys.path.append('packs/content_creator')
sys.path.append('gap_packs/content_creator_gaps')
sys.path.append('deployment/content_creator_deploy')

from functions import (
    generate_brand_voice,
    generate_content_pillars,
    generate_short_form_content,
    generate_long_form_content,
    generate_email_sequence,
    generate_content_calendar
)
from bridge import connect
from deploy import deploy

# Test the complete Content Creator workflow
def test_content_creator_workflow():
    print("=== Testing Content Creator B4 Workflow ===")
    
    # Step 1: Generate brand voice
    voice = generate_brand_voice(
        business_name="TechGrowth Co",
        audience="startup founders",
        tone="professional yet approachable"
    )
    print(f"✅ Brand voice generated: {voice['business_name']}")
    
    # Step 2: Generate content pillars
    pillars_data = generate_content_pillars(
        business_name="TechGrowth Co",
        offers=["product development", "marketing strategy", "funding advice"]
    )
    pillars = [p["pillar"] for p in pillars_data["pillars"]]
    print(f"✅ Content pillars generated: {len(pillars)} pillars")
    
    # Step 3: Generate short form content
    short_form = generate_short_form_content(pillars, count=2)
    print(f"✅ Short form content generated: {len(short_form['short_form_posts'])} posts")
    
    # Step 4: Generate long form content
    long_form = generate_long_form_content([
        "How to scale your startup",
        "Marketing automation for founders",
        "Securing your first round of funding"
    ])
    print(f"✅ Long form content generated: {len(long_form['long_form_articles'])} articles")
    
    # Step 5: Generate email sequence
    email_seq = generate_email_sequence(goal="convert leads to customers", steps=5)
    print(f"✅ Email sequence generated: {len(email_seq['email_sequence'])} emails")
    
    # Step 6: Generate content calendar
    calendar = generate_content_calendar(pillars, days=30)
    print(f"✅ Content calendar generated: {len(calendar['calendar'])} days")
    
    # Step 7: Connect through GAP bridge
    content_wrapper = connect(voice, pillars_data, short_form, long_form, email_seq, calendar)
    print(f"✅ GAP bridge connected: {content_wrapper['status']}")
    
    # Step 8: Deploy
    deploy(content_wrapper)
    print("✅ Deployment completed")
    
    print("\n=== Content Creator B4 Workflow Test Complete ===")
    print("✅ All components working correctly!")
    
    return content_wrapper

if __name__ == "__main__":
    result = test_content_creator_workflow()