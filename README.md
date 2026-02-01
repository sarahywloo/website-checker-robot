# 🦷 Website Checker Robot 
Built with my 7-year-old son, this is a lightweight python-based website monitoring tool that checks our dental office website and sends an email alert if it goes down. Built to solve a real problem (WordPress auto-updates breaking the site) while also being a fun way to explore how real-world engineers build practical tools, together as a family.

---

## Features

- Checks website for uptime daily
- Sends email alert if the site is down
- Easily scheduled with a cron job on macOS or via Github Actions
- Uses `.env` for secure credential management
- Simple to set up and collaborate on Github

---

## Getting Started 

These instructions will help you get the project up and running locally using Visual Studio Code.

### 1. Clone the repository

```bash
gitclone https://github.com/sarahywloo/website-checker-robot.git
cd website-checker-robot
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

### 1. `.env` File (Email Settings)

Create a `.env` file in the project root:

```bash
touch .env
```

Paste the following and update with your email credentials:

```env
EMAIL_SENDER="youremail@gmail.com"
EMAIL_PASSWORD="your_app_password"
EMAIL_RECEIVER="recipient@example.com"
```

### 2. `config.json` (Site Settings)

Update `config.json` with your site details:

```json
{
    "url": "https://www.mywebsite.com"
}
```

### 3. Run the Script Manually

```bash
python check.py
```

You should see a log output indicating whether the site is up or down.

## Automate with Cron (macOS/Linux)

### 1. Open crontab:

```bash
crontab -e
```

Add the following line to run the script every 5 minutes:

```bash
*/5 * * * * /usr/bin/python3 /Users/YOUR_USERNAME/path/to/website-checker-robot/check.py  >> /Users/YOUR_USERNAME/path/to/website-checker-robot/monitor.log 2>&1
```

- Replace `/Users/YOUR_USERNAME/...` with the full path to your Python interpreter and `check.py` file.
- You can find your Python path with:

```bash
which python3
```

## Security & Logging

- Sensitive information is stored securely using `.env`
- Logs can be captured via cron and redirected to monitor.log

## License

MIT License — free to use and modify.