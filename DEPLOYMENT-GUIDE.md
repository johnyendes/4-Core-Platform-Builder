# X-Core Platform Deployment Guide

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Local Development Setup](#local-development-setup)
3. [Production Deployment](#production-deployment)
4. [Environment Configuration](#environment-configuration)
5. [Troubleshooting](#troubleshooting)
6. [Monitoring & Maintenance](#monitoring--maintenance)

## 🚀 Prerequisites

### Required Software

- **Python 3.11 or higher**
- **Git**
- **Virtual Environment** (venv or conda)

### Recommended Tools

- **Postman** or **curl** (for API testing)
- **VS Code** or **PyCharm** (for development)

## 💻 Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/johnyendes/4-Core-Platform-Builder.git
cd 4-Core-Platform-Builder
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 5. Verify Installation

```bash
# Test App Builder Pack (A1)
python tests/test_a1_comprehensive.py

# Test other packs
python tests/test_web_builder.py
python tests/test_bot_builder.py
python tests/test_content_creator.py
```

### 6. Run Platform CLI

```bash
# List all available packs
python -m xcore_platform.xcore.cli list-packs

# Get pack information
python -m xcore_platform.xcore.cli pack-info app_builder

# Check system status
python -m xcore_platform.xcore.cli status
```

## 🌍 Production Deployment

### Deployment Options

#### Option 1: Render (Recommended)

**Pros:** Easy setup, automatic SSL, built-in CI/CD

1. **Prepare for Deployment**

```bash
# Create a Procfile (if needed)
echo "web: python -m xcore_platform.xcore.xcore_startup" > Procfile
```

2. **Deploy via Render Dashboard**

   - Go to [render.com](https://render.com)
   - Create a new "Web Service"
   - Connect your GitHub repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `python -m xcore_platform.xcore.xcore_startup`
   - Configure environment variables

3. **Required Environment Variables**

```
BRAIN_API_ENABLED=true
BRAIN_API_BASE_URL=https://your-api-url.com/api
BRAIN_API_KEY=your-production-api-key
DEBUG=false
LOG_LEVEL=INFO
```

#### Option 2: Railway

**Pros:** Simple CLI deployment, good for Python apps

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Set environment variables
railway variables set BRAIN_API_ENABLED=true
railway variables set DEBUG=false

# Deploy
railway up
```

#### Option 3: DigitalOcean App Platform

**Pros:** Reliable, good performance, cost-effective

1. **Create App**

   - Go to DigitalOcean App Platform
   - Create new app
   - Connect GitHub repository

2. **Configure**

   - Build command: `pip install -r requirements.txt`
   - Run command: `gunicorn xcore_platform.xcore.xcore_startup:app --bind 0.0.0.0:$PORT`
   - Add environment variables

3. **Deploy**

   - Click "Deploy"
   - Wait for deployment to complete

#### Option 4: AWS EC2 (Manual)

**Pros:** Full control, scalable

1. **Launch EC2 Instance**

   - Choose Ubuntu 22.04 LTS
   - Configure security groups (allow port 80, 443, 22)

2. **SSH into Instance**

```bash
ssh -i your-key.pem ubuntu@your-instance-ip
```

3. **Setup Server**

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python
sudo apt install python3.11 python3-pip python3-venv -y

# Clone repository
git clone https://github.com/johnyendes/4-Core-Platform-Builder.git
cd 4-Core-Platform-Builder

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn

# Setup environment
cp .env.example .env
nano .env  # Edit with your values

# Test locally
python -m xcore_platform.xcore.xcore_startup
```

4. **Setup Systemd Service**

```bash
sudo nano /etc/systemd/system/xcore-platform.service
```

```ini
[Unit]
Description=X-Core Platform
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/4-Core-Platform-Builder
Environment="PATH=/home/ubuntu/4-Core-Platform-Builder/venv/bin"
ExecStart=/home/ubuntu/4-Core-Platform-Builder/venv/bin/python -m xcore_platform.xcore.xcore_startup
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl enable xcore-platform
sudo systemctl start xcore-platform
sudo systemctl status xcore-platform
```

5. **Setup Nginx Reverse Proxy**

```bash
sudo apt install nginx -y
sudo nano /etc/nginx/sites-available/xcore-platform
```

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```bash
# Enable site and restart nginx
sudo ln -s /etc/nginx/sites-available/xcore-platform /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 🔧 Environment Configuration

### Environment Variables

Create a `.env` file in the root directory:

```bash
# Brain API Configuration
BRAIN_API_ENABLED=true
BRAIN_API_BASE_URL=http://localhost:8000/api
BRAIN_API_KEY=your-brain-api-key-here

# Development Settings
DEBUG=false
LOG_LEVEL=INFO

# Platform Configuration
PLATFORM_NAME=X-Core Platform
PLATFORM_VERSION=1.0.0

# Optional: Database (if needed)
# DATABASE_URL=postgresql://user:password@localhost/xcore

# Optional: Cache Configuration
# CACHE_ENABLED=true
# CACHE_TTL=3600

# Optional: Rate Limiting
# RATE_LIMIT_ENABLED=true
# RATE_LIMIT_REQUESTS=100
# RATE_LIMIT_PERIOD=60
```

### Security Best Practices

1. **Never commit `.env` files** to git
2. **Use strong API keys** with sufficient entropy
3. **Enable HTTPS** in production
4. **Set up firewall rules** to restrict access
5. **Regularly update dependencies**
6. **Monitor logs** for suspicious activity

## 🐛 Troubleshooting

### Common Issues

#### Issue: Import Errors

```bash
# Solution: Ensure you're in the correct directory
cd /path/to/4-Core-Platform-Builder
source venv/bin/activate
pip install -r requirements.txt
```

#### Issue: Brain API Connection Failed

```bash
# Solution: Check environment variables
echo $BRAIN_API_ENABLED
echo $BRAIN_API_BASE_URL

# Solution: Disable Brain API for testing
export BRAIN_API_ENABLED=false
```

#### Issue: Port Already in Use

```bash
# Solution: Kill process using the port
lsof -ti:8000 | xargs kill -9

# Or use a different port
export PORT=8080
```

#### Issue: Permission Denied

```bash
# Solution: Fix file permissions
chmod +x xcore_platform/xcore/*.py
```

### Debug Mode

Enable debug mode for detailed error messages:

```bash
export DEBUG=true
python -m xcore_platform.xcore.xcore_startup
```

### Log Files

Check application logs:

```bash
# Systemd service logs
sudo journalctl -u xcore-platform -f

# Application logs
tail -f /var/log/xcore-platform/app.log
```

## 📊 Monitoring & Maintenance

### Health Checks

```bash
# Check if service is running
sudo systemctl status xcore-platform

# Test basic functionality
python -c "from xcore_platform import BrainAPI; print('✅ Platform working')"
```

### Performance Monitoring

Recommended tools:
- **Prometheus + Grafana** - Metrics and visualization
- **Sentry** - Error tracking
- **Uptime Robot** - Availability monitoring

### Backup Strategy

1. **Database Backups** (if using database)
```bash
# Daily automated backups
0 2 * * * pg_dump xcore > /backup/xcore_$(date +\%Y\%m\%d).sql
```

2. **Configuration Backups**
```bash
# Backup environment configuration
cp .env .env.backup
```

3. **Code Backups**
```bash
# Git provides version control
git push origin main
```

### Update Procedure

1. **Pull latest changes**
```bash
git pull origin main
```

2. **Update dependencies**
```bash
pip install --upgrade -r requirements.txt
```

3. **Restart service**
```bash
sudo systemctl restart xcore-platform
```

4. **Verify functionality**
```bash
python tests/test_a1_comprehensive.py
```

### Scaling Strategy

#### Horizontal Scaling

- Use load balancer (Nginx, HAProxy)
- Deploy multiple instances
- Use shared database/cache

#### Vertical Scaling

- Increase CPU/RAM resources
- Optimize database queries
- Implement caching

## 📞 Support

For issues or questions:

1. Check the [GitHub Issues](https://github.com/johnyendes/4-Core-Platform-Builder/issues)
2. Review the main [README.md](README.md)
3. Consult the code documentation

## 🎯 Quick Start Checklist

- [ ] Repository cloned locally
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Environment configured
- [ ] Tests passing
- [ ] Production server selected
- [ ] Environment variables set
- [ ] Application deployed
- [ ] HTTPS configured
- [ ] Monitoring setup
- [ ] Backup strategy implemented

---

**Ready to deploy?** Follow the production deployment section above for your chosen platform.

**Need help?** Check the troubleshooting section or create a GitHub issue.