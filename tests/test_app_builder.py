import sys
import os
sys.path.append('packs/app_builder')
sys.path.append('gap_packs/app_builder_gaps')
sys.path.append('deployment/app_builder_deploy')

from functions import (
    generate_app_core,
    generate_app_screens,
    generate_app_navigation_flow,
    generate_app_database_schema,
    generate_app_api_endpoints
)
from bridge import connect
from deploy import deploy

# Test the complete App Builder workflow
def test_app_builder_workflow():
    print("=== Testing App Builder A1 Workflow ===")
    
    # Step 1: Generate app core
    core = generate_app_core(
        app_name="TaskMaster Pro",
        purpose="help teams manage projects and tasks efficiently",
        audience="small to medium businesses"
    )
    print(f"✅ Core generated: {core['app_name']}")
    
    # Step 2: Generate app screens
    screens = generate_app_screens(
        app_name="TaskMaster Pro",
        features=["dashboard", "create task", "view tasks", "team management", "reports"]
    )
    print(f"✅ Screens generated: {len(screens['screens'])} screens")
    
    # Step 3: Generate navigation flow
    screen_order = [screen['screen_name'] for screen in screens['screens']]
    navigation = generate_app_navigation_flow(screen_order)
    print(f"✅ Navigation generated: {len(navigation['transitions'])} transitions")
    
    # Step 4: Generate database schema
    tables = {
        "users": ["id", "name", "email", "role"],
        "projects": ["id", "name", "description", "owner_id"],
        "tasks": ["id", "title", "description", "status", "project_id", "assignee_id"]
    }
    database = generate_app_database_schema(tables)
    print(f"✅ Database schema generated: {len(database['tables'])} tables")
    
    # Step 5: Generate API endpoints
    endpoints = {
        "get_users": "/api/users",
        "create_project": "/api/projects",
        "get_tasks": "/api/tasks",
        "update_task": "/api/tasks/{id}"
    }
    api = generate_app_api_endpoints(endpoints)
    print(f"✅ API endpoints generated: {len(api['endpoints'])} endpoints")
    
    # Step 6: Connect through GAP bridge
    blueprint_wrapper = connect(core, screens, navigation, database, api)
    print(f"✅ GAP bridge connected: {blueprint_wrapper['status']}")
    
    # Step 7: Deploy
    deploy(blueprint_wrapper)
    print("✅ Deployment completed")
    
    print("\n=== App Builder A1 Workflow Test Complete ===")
    print("✅ All components working correctly!")
    
    return blueprint_wrapper

if __name__ == "__main__":
    result = test_app_builder_workflow()