# Project Structure

This document describes the file organization of the Hand-Controlled Pong Game repository.

## 📁 File Tree

```
hand-controlled-pong/
│
├── 📄 pong_game.py              # Main game code
├── 📄 requirements.txt          # Python dependencies
├── 📄 setup.py                  # Package installation script
├── 📄 .gitignore               # Files to exclude from Git
│
├── 📚 Documentation
│   ├── README.md               # Project overview & quick start
│   ├── QUICKSTART.md           # 5-minute setup guide
│   ├── INSTALL.md              # Detailed installation (all OS)
│   ├── CONTRIBUTING.md         # Contribution guidelines
│   ├── CHANGELOG.md            # Version history
│   ├── LICENSE                 # MIT License
│   ├── REPO_SETUP.md           # GitHub setup instructions
│   ├── GITHUB_AUTH_SETUP.md    # SSH/Token authentication guide
│   └── GIT_WORKFLOW.md         # How to use Git (this is new!)
│
├── 🚀 Launch Scripts
│   ├── run_game.sh             # Linux/macOS launcher
│   └── run_game.bat            # Windows launcher
│
├── 🔧 GitHub Configuration
│   └── .github/
│       ├── workflows/
│       │   └── python-app.yml  # CI/CD automation
│       ├── ISSUE_TEMPLATE/
│       │   ├── bug_report.md
│       │   ├── feature_request.md
│       │   └── question.md
│       └── PULL_REQUEST_TEMPLATE.md
│
└── 🔒 Local Only (NOT in GitHub)
    ├── venv/                   # Virtual environment (excluded)
    ├── __pycache__/            # Python cache (excluded)
    ├── FIX_AUTH_ERROR.txt     # Your local setup notes (excluded)
    ├── setup_github_ssh.sh    # Your local SSH script (excluded)
    └── HOW_TO_RUN.md          # Local notes (excluded)
```

## 📋 File Descriptions

### Core Files (Required)

| File | Purpose |
|------|---------|
| `pong_game.py` | Main game implementation with hand tracking |
| `requirements.txt` | List of Python packages needed |
| `setup.py` | Allows installation with `pip install` |
| `.gitignore` | Tells Git which files to ignore |

### Documentation (User-Facing)

| File | Audience | Content |
|------|----------|---------|
| `README.md` | Everyone | First thing visitors see, project overview |
| `QUICKSTART.md` | New users | Get started in 5 minutes |
| `INSTALL.md` | New users | Detailed OS-specific installation |
| `CONTRIBUTING.md` | Contributors | How to contribute to the project |
| `LICENSE` | Legal | MIT license terms |
| `CHANGELOG.md` | All users | What changed in each version |

### Documentation (Developer/Setup)

| File | Audience | Content |
|------|----------|---------|
| `REPO_SETUP.md` | You | How you set up this GitHub repo |
| `GITHUB_AUTH_SETUP.md` | You/Contributors | SSH/Token authentication |
| `GIT_WORKFLOW.md` | You/Contributors | How to use Git commands |
| `PROJECT_STRUCTURE.md` | You/Contributors | This file! |

### Scripts

| File | OS | Purpose |
|------|-----|---------|
| `run_game.sh` | Linux/macOS | Easy game launcher |
| `run_game.bat` | Windows | Easy game launcher |

### GitHub Templates

| File | Purpose |
|------|---------|
| `.github/workflows/python-app.yml` | Automated testing on GitHub |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Bug report template |
| `.github/ISSUE_TEMPLATE/feature_request.md` | Feature request template |
| `.github/ISSUE_TEMPLATE/question.md` | Question template |
| `.github/PULL_REQUEST_TEMPLATE.md` | Pull request template |

### Local Files (Excluded from GitHub)

These files are on your computer but NOT on GitHub (via `.gitignore`):

| File/Folder | Why Excluded |
|-------------|--------------|
| `venv/` | Virtual environment (users create their own) |
| `__pycache__/` | Python cache files (auto-generated) |
| `FIX_AUTH_ERROR.txt` | Your personal setup notes |
| `setup_github_ssh.sh` | Your personal SSH setup script |
| `HOW_TO_RUN.md` | Duplicate of QUICKSTART.md info |

## 🎯 What Users See on GitHub

When someone visits your repository, they see:

```
hand-controlled-pong/
├── pong_game.py
├── requirements.txt
├── setup.py
├── README.md              ← First thing they read
├── QUICKSTART.md
├── INSTALL.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── REPO_SETUP.md
├── GITHUB_AUTH_SETUP.md
├── GIT_WORKFLOW.md
├── PROJECT_STRUCTURE.md
├── run_game.sh
├── run_game.bat
└── .github/
    ├── workflows/
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

They do NOT see:
- `venv/` folder
- `FIX_AUTH_ERROR.txt`
- `setup_github_ssh.sh`
- `HOW_TO_RUN.md`
- Your personal files

## 📊 Directory Size Reference

Approximate file counts:
- **Root files**: 13 files
- **Documentation**: 9 markdown files
- **Scripts**: 2 launcher scripts
- **GitHub templates**: 5 template files
- **Total public files**: ~29 files

## 🔄 Keeping It Clean

To remove personal files from GitHub (if already pushed):

```bash
git rm --cached FIX_AUTH_ERROR.txt setup_github_ssh.sh HOW_TO_RUN.md
git commit -m "chore: Remove local setup files from repository"
git push
```

Then they'll only exist on your computer, not on GitHub.

## 🆕 Adding New Files

When you create new files:

1. **Should it be public?**
   - YES → Add, commit, push normally
   - NO → Add to `.gitignore` first

2. **Public file example** (new feature):
   ```bash
   # Create new file
   nano leaderboard.py
   
   # Add to git
   git add leaderboard.py
   git commit -m "feat: Add leaderboard system"
   git push
   ```

3. **Private file example** (personal notes):
   ```bash
   # Create file
   nano my_notes.txt
   
   # Add to .gitignore
   echo "my_notes.txt" >> .gitignore
   
   # Commit .gitignore update
   git add .gitignore
   git commit -m "chore: Update gitignore"
   git push
   ```

## 📚 Related Documentation

- [GIT_WORKFLOW.md](GIT_WORKFLOW.md) - Learn Git commands
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [README.md](README.md) - Project overview

---

**Keep your repository clean and organized!** 🎯

