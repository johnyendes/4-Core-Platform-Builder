from typing import Dict, Any, List


def generate_brand_voice(business_name: str, audience: str, tone: str) -> Dict[str, Any]:
    return {
        "business_name": business_name,
        "audience": audience,
        "tone": tone,
        "voice_profile": f"{business_name} speaks in a {tone} tone to {audience}."
    }


def generate_content_pillars(business_name: str, offers: List[str]) -> Dict[str, Any]:
    pillars = []
    for offer in offers:
        pillars.append({
            "pillar": offer,
            "description": f"Content supporting the offer: {offer} for {business_name}."
        })

    return {
        "business_name": business_name,
        "pillars": pillars
    }


def generate_short_form_content(pillars: List[str], count: int) -> Dict[str, Any]:
    posts = []
    for p in pillars:
        for i in range(count):
            posts.append({
                "pillar": p,
                "post": f"Short-form content #{i+1} based on pillar: {p}."
            })

    return {"short_form_posts": posts}


def generate_long_form_content(topics: List[str]) -> Dict[str, Any]:
    articles = []
    for t in topics:
        articles.append({
            "topic": t,
            "article": f"Long-form article outline for topic: {t}."
        })
    return {"long_form_articles": articles}


def generate_email_sequence(goal: str, steps: int) -> Dict[str, Any]:
    emails = []
    for i in range(steps):
        emails.append({
            "email_number": i+1,
            "goal": goal,
            "content": f"Email #{i+1} designed to move subscriber toward '{goal}'."
        })

    return {"email_sequence": emails}


def generate_content_calendar(pillars: List[str], days: int) -> Dict[str, Any]:
    schedule = []
    for day in range(1, days+1):
        schedule.append({
            "day": day,
            "pillar": pillars[(day-1) % len(pillars)],
            "content": f"Content for day {day} based on pillar {pillars[(day-1) % len(pillars)]}."
        })

    return {"calendar": schedule}