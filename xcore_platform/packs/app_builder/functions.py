from typing import Dict, Any, List


# -------------------------------
# LEVEL 1 — CORE FUNCTIONS
# -------------------------------

def generate_app_core(app_name: str, purpose: str, audience: str) -> Dict[str, Any]:
    """Generate the core definition of the app."""
    return {
        "app_name": app_name,
        "purpose": purpose,
        "audience": audience,
        "summary": f"{app_name} is an application designed to {purpose} for {audience}."
    }


def generate_app_screens(app_name: str, features: List[str]) -> Dict[str, Any]:
    """Generate a list of app screens based on features."""
    screens = []
    for feature in features:
        screens.append({
            "screen_name": f"{feature.title()} Screen",
            "description": f"Screen allowing the user to {feature} in {app_name}."
        })
    return {"screens": screens}


def generate_app_navigation_flow(screen_order: List[str]) -> Dict[str, Any]:
    """Generate screen-to-screen navigation transitions."""
    transitions = []
    for i in range(len(screen_order) - 1):
        transitions.append({
            "from": screen_order[i],
            "to": screen_order[i + 1]
        })
    return {"navigation_flow": transitions}


def generate_app_database_schema(tables: Dict[str, List[str]]) -> Dict[str, Any]:
    """Generate a basic database schema."""
    schema = []
    for table_name, fields in tables.items():
        schema.append({
            "table": table_name,
            "fields": fields
        })
    return {"database_schema": schema}


def generate_app_api_endpoints(endpoints: Dict[str, str]) -> Dict[str, Any]:
    """Generate a list of API endpoints."""
    api_list = [{"name": name, "path": path} for name, path in endpoints.items()]
    return {"api_endpoints": api_list}


# -------------------------------
# LEVEL 2 — PREMIUM FUNCTIONS
# -------------------------------

def generate_ux_recommendations(app_blueprint: Dict[str, Any]) -> Dict[str, Any]:
    """Generate UX recommendations based on the existing blueprint."""
    screens = app_blueprint.get("screens", {}).get("screens", [])
    recs = []

    for s in screens:
        recs.append({
            "screen": s["screen_name"],
            "recommendation": f"Improve clarity and reduce steps on {s['screen_name']}."
        })

    return {"ux_recommendations": recs}


def generate_ui_style_guide(app_type: str) -> Dict[str, Any]:
    """Generate a simple UI style guide."""
    palettes = {
        "social": ["#FF3B30", "#FF9500", "#4CD964", "#007AFF"],
        "business": ["#003366", "#0055A4", "#7FB3D5", "#D5DBDB"],
        "ecommerce": ["#1ABC9C", "#16A085", "#F1C40F", "#E74C3C"]
    }
    fonts = {
        "social": "Roboto",
        "business": "Inter",
        "ecommerce": "Montserrat"
    }

    return {
        "style_guide": {
            "palette": palettes.get(app_type, ["#333333", "#555555"]),
            "font": fonts.get(app_type, "Arial"),
            "corner_radius": "8px",
            "button_style": "rounded, high-contrast"
        }
    }


def generate_database_optimizations(database: Dict[str, Any]) -> Dict[str, Any]:
    """Recommend optimizations based on database schema."""
    optimizations = []
    tables = database.get("database_schema", [])

    for t in tables:
        optimizations.append({
            "table": t["table"],
            "optimization": f"Add indexes to fields in {t['table']} where frequent lookups occur."
        })

    return {"database_optimizations": optimizations}


def generate_api_security_layer(endpoints: Dict[str, Any]) -> Dict[str, Any]:
    """Generate API security recommendations."""
    secured = []

    for ep in endpoints.get("api_endpoints", []):
        secured.append({
            "endpoint": ep["name"],
            "security": "Add JWT auth, rate limiting, and input sanitization."
        })

    return {"api_security_layer": secured}


def generate_dev_instructions(app_blueprint: Dict[str, Any]) -> Dict[str, Any]:
    """Produce developer instructions based on full blueprint."""
    instructions = []

    if "screens" in app_blueprint:
        instructions.append("Follow screen definitions to build frontend layout.")

    if "database_schema" in app_blueprint:
        instructions.append("Implement database tables exactly as defined.")

    if "api_endpoints" in app_blueprint:
        instructions.append("Create REST routes matching API endpoint definitions.")

    return {"dev_instructions": instructions}


# -------------------------------
# LEVEL 3 — PROFESSIONAL ULTRA
# -------------------------------

def generate_full_wireframes(app_blueprint: Dict[str, Any]) -> Dict[str, Any]:
    """Generate text-based wireframes for each screen."""
    screens = app_blueprint.get("screens", {}).get("screens", [])
    wireframes = []

    for s in screens:
        wireframes.append({
            "screen": s["screen_name"],
            "wireframe": f"[WIREFRAME] Layout structure for {s['screen_name']}."
        })

    return {"wireframes": wireframes}


def generate_er_diagram(database: Dict[str, Any]) -> Dict[str, Any]:
    """Generate a simple ER diagram description."""
    diagram = []
    for table in database.get("database_schema", []):
        diagram.append({
            "entity": table["table"],
            "fields": table["fields"],
            "diagram": f"Entity {table['table']} with fields {', '.join(table['fields'])}."
        })

    return {"er_diagram": diagram}


def generate_microservice_map(app_blueprint: Dict[str, Any]) -> Dict[str, Any]:
    """Generate suggested microservice decomposition."""
    services = []

    if "api_endpoints" in app_blueprint:
        for ep in app_blueprint["api_endpoints"]:
            name = ep["name"]
            root = name.split("_")[0]
            services.append({
                "service": f"{root}_service",
                "reason": f"Handles functionality related to {root}."
            })

    return {"microservice_map": services}


def generate_localization_pack(app_name: str) -> Dict[str, Any]:
    """Generate a localization base pack."""
    languages = ["en", "es", "fr", "de", "zh"]
    base_strings = {
        "welcome": f"Welcome to {app_name}",
        "error_generic": "An unexpected error has occurred.",
        "button_ok": "OK",
        "button_cancel": "Cancel"
    }

    localized = {}

    for lang in languages:
        localized[lang] = {
            "language": lang,
            "phrases": base_strings
        }

    return {"localization_pack": localized}


def generate_performance_plan(app_blueprint: Dict[str, Any]) -> Dict[str, Any]:
    """Generate a performance optimization plan."""
    plan = [
        "Implement caching for repeated API calls.",
        "Use CDN for static assets.",
        "Compress images and minify scripts.",
        "Optimize database queries.",
        "Implement lazy loading for large components."
    ]
    return {"performance_plan": plan}


def generate_pitch_deck_outline(app_blueprint: Dict[str, Any]) -> Dict[str, Any]:
    """Generate a pitch deck outline for investors."""
    name = app_blueprint.get("app_core", {}).get("app_name", "Your App")

    outline = [
        "Problem Slide",
        "Solution Slide",
        f"Product Slide — show screenshots of {name}",
        "Market Size Slide",
        "Business Model Slide",
        "Go-To-Market Strategy Slide",
        "Team Slide",
        "Financial Projections Slide"
    ]

    return {"pitch_deck_outline": outline}