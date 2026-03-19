# X-Core Platform

🚀 **The Ultimate Modular AI Platform for Digital Blueprint Generation**

## 📋 Project Overview

X-Core Platform is a proprietary, modular AI system that generates complete digital blueprints for applications, websites, bots, and content systems. Built with a unique Brain API integration and GAP bridge architecture, it enables users to create production-ready technical specifications with minimal effort.

### Core Features

- **Modular Pack System**: Extensible pack architecture for different blueprint types
- **Brain API Integration**: Proprietary API with usage tracking and monetization
- **GAP Bridge Architecture**: Intelligent data transformation between components
- **Automated Deployment**: Ready-to-use deployment pipelines
- **Multi-Tier Functionality**: Level 1 (Core), Level 2 (Premium), Level 3 (Professional Ultra)

### Available Packs

1. **A1 - App Builder Pack** 📱
   - Generate complete mobile app blueprints
   - Core idea, screens, navigation, database schema, API endpoints
   - Premium: UX recommendations, UI style guide, database optimizations
   - Professional Ultra: Wireframes, ER diagrams, microservice maps, localization

2. **A2 - Web Builder Pack** 🌐
   - Complete website blueprint generation
   - Pages, layout, navigation, SEO metadata
   - Production-ready site architecture

3. **A3 - Bot Builder Pack** 🤖
   - AI bot blueprints with intents and conversation flows
   - Response mappings, actions, integration planning
   - Perfect for chatbots, customer support, automation

4. **B4 - Content Creator Pack** ✍️
   - Full content systems generation
   - Brand voice, content pillars, short/long-form content
   - Email sequences, content calendars
   - Money printer pack with recurring revenue potential

## 🛠️ Tech Stack

- **Backend**: Python 3.11+
- **Architecture**: Modular pack system with GAP bridges
- **API**: Proprietary Brain API with UUID-based authentication
- **Deployment**: Standalone Python application

## 📁 Project Structure

```
xcore_platform/
├── xcore/                    # Core platform system
│   ├── brain_api.py         # Brain API integration
│   ├── pack_loader.py       # Dynamic pack loading
│   ├── pack_runner.py       # Pack execution engine
│   ├── xcore_registry.py    # Pack registration system
│   ├── license_manager.py   # System validation
│   ├── cli.py               # Command-line interface
│   └── xcore_startup.py     # Platform initialization
│
├── packs/                    # Pack modules
│   ├── app_builder/         # A1 - App Builder Pack
│   ├── web_builder/         # A2 - Web Builder Pack
│   ├── bot_builder/         # A3 - Bot Builder Pack
│   └── content_creator/     # B4 - Content Creator Pack
│       ├── pack.json        # Pack configuration
│       ├── functions.py     # Pack functions (16 for A1, 5-6 for others)
│       └── meta.txt         # Usage documentation
│
├── gap_packs/               # GAP bridges (data transformation)
│   ├── app_builder_gaps/    # A1 bridge
│   ├── web_builder_gaps/    # A2 bridge
│   ├── bot_builder_gaps/    # A3 bridge
│   └── content_creator_gaps/# B4 bridge
│       ├── gap.json         # Bridge configuration
│       └── bridge.py        # Bridge logic
│
└── deployment/               # Deployment pipelines
    ├── app_builder_deploy/  # A1 deployment
    ├── web_builder_deploy/  # A2 deployment
    ├── bot_builder_deploy/  # A3 deployment
    └── content_creator_deploy/# B4 deployment
        ├── deploy.json      # Deployment configuration
        └── deploy.py        # Deployment logic
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/johnyendes/4-Core-Platform-Builder.git
cd 4-Core-Platform-Builder
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your Brain API configuration
```

5. **Verify installation**
```bash
python -c "import sys; print(f'Python {sys.version}')"
python test_a1_comprehensive.py  # Test App Builder Pack
```

## 📖 Usage

### Basic Usage Example

```python
from packs.app_builder.functions import *
from gap_packs.app_builder_gaps.bridge import connect
from deployment.app_builder_deploy.deploy import deploy

# Generate app blueprint
core = generate_app_core("TaskMaster Pro", "manage tasks", "productivity users")
screens = generate_app_screens("TaskMaster Pro", ["dashboard", "create task", "view tasks"])
navigation = generate_app_navigation_flow(["Dashboard", "Create Task", "View Tasks"])
database = generate_app_database_schema({"users": ["id", "name"], "tasks": ["id", "title"]})
api = generate_app_api_endpoints({"get_users": "/api/users", "create_task": "/api/tasks"})

# Bridge components
blueprint = connect(core, screens, navigation, database, api)

# Deploy
deploy(blueprint)
```

### Using All Packs

```python
# App Builder (A1)
from packs.app_builder.functions import *

# Web Builder (A2)
from packs.web_builder.functions import *

# Bot Builder (A3)
from packs.bot_builder.functions import *

# Content Creator (B4)
from packs.content_creator.functions import *
```

## 🧪 Testing

Run comprehensive tests for each pack:

```bash
# Test App Builder Pack (A1) - All 16 functions
python test_a1_comprehensive.py

# Test Web Builder Pack (A2)
python test_web_builder.py

# Test Bot Builder Pack (A3)
python test_bot_builder.py

# Test Content Creator Pack (B4)
python test_content_creator.py
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```bash
# Brain API Configuration
BRAIN_API_ENABLED=true
BRAIN_API_BASE_URL=http://localhost:8000/api
BRAIN_API_KEY=your-brain-api-key-here

# Development Settings
DEBUG=true
LOG_LEVEL=INFO
```

## 📦 Deployment

### Deployment Options

1. **Render / Railway / Fly.io** (Recommended for Python apps)
2. **DigitalOcean App Platform**
3. **AWS EC2 / Elastic Beanstalk**
4. **Heroku**

### Deployment Steps

1. **Prepare environment variables**
```bash
# Set all required environment variables in your deployment platform
BRAIN_API_ENABLED=true
BRAIN_API_BASE_URL=https://your-api-url.com/api
BRAIN_API_KEY=your-production-api-key
```

2. **Deploy using platform CLI or web interface**
```bash
# Example for Render
render deploy
```

3. **Configure web server (if needed)**
```bash
# Using gunicorn
gunicorn xcore.xcore_startup:app --bind 0.0.0.0:$PORT
```

### API Integration

The frontend (if you build one) connects to the backend via:

```python
# API Base URL Configuration
API_BASE_URL = os.getenv('BRAIN_API_BASE_URL', 'http://localhost:8000/api')
```

**Note**: Currently, this is a Python-only platform. To add a web interface, you would need to:
1. Build a React/Vue/Next.js frontend
2. Create REST API endpoints in the Python backend
3. Configure CORS for cross-origin requests

## 🏗️ Architecture

### Core Components

1. **Brain API**: Central monetization engine requiring API keys
2. **Pack Loader**: Dynamic loading of all pack types
3. **Pack Runner**: Execution engine with Brain API integration
4. **GAP Bridges**: Data transformation between pack components
5. **Deployment Pipelines**: Automated export and validation

### Pack Architecture

Each pack follows a consistent structure:
- **Level 1**: Core functions (5 functions)
- **Level 2**: Premium functions (5 functions) - optional
- **Level 3**: Professional Ultra functions (6 functions) - optional
- **GAP Bridge**: Unifies all pack outputs
- **Deployment**: Exports and validates final blueprints

## 💰 Business Model

### Pricing Structure

- **A1 App Builder**: $297-$497
- **A2 Web Builder**: $197-$397
- **A3 Bot Builder**: $247-$497
- **B4 Content Creator**: $297-$497

### Bundle Options

- **Builder Trio**: A1 + A2 + A3 ($697-$1,297)
- **Digital Empire**: A1 + A2 + A3 + B4 ($997-$1,797)
- **Social Media Accelerator**: B4 + Platform-specific packs

## 🤝 Contributing

This is a proprietary platform. For contributions or licensing inquiries, please contact the development team.

## 📄 License

Proprietary - All rights reserved.

## 🔐 Security

- Brain API requires valid API keys for all operations
- Usage tracking for billing and analytics
- UUID-based key system (XCORE-{uuid})

## 📞 Support

For support, documentation, or inquiries, please refer to the platform documentation or contact the development team.

## 🎯 Roadmap

### Completed ✅
- A1 App Builder Pack (16 functions, 3 levels)
- A2 Web Builder Pack (5 functions)
- A3 Bot Builder Pack (5 functions)
- B4 Content Creator Pack (6 functions)
- Brain API integration
- GAP bridge architecture
- Deployment pipelines

### Future Plans 🚀
- Web interface (React/Vue/Next.js)
- Additional specialized packs
- Enhanced Brain API features
- Analytics dashboard
- Multi-tenant support

---

**Built with ❤️ by the X-Core Development Team**