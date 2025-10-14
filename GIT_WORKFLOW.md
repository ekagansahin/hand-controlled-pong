# Git Workflow Guide

## 📝 Understanding Local vs GitHub

Your files exist in **two places**:
1. **Local** (your computer) - `/home/mint/python/game/Trifaze`
2. **GitHub** (cloud) - `https://github.com/ekagansahin/hand-controlled-pong`

**Important**: Changes you make locally do NOT automatically appear on GitHub!

## 🔄 How to Sync Changes to GitHub

### Every time you make changes:

```bash
cd /home/mint/python/game/Trifaze

# 1. Check what files changed
git status

# 2. Add the files you want to upload
git add .                           # Add all changed files
# OR
git add pong_game.py README.md      # Add specific files only

# 3. Commit with a message describing what you changed
git commit -m "Fixed bug in paddle movement"

# 4. Push to GitHub
git push
```

### Common Workflow Examples:

**Example 1: You fixed a bug**
```bash
git add pong_game.py
git commit -m "Fix: Prevent ball from going through paddles"
git push
```

**Example 2: Updated documentation**
```bash
git add README.md
git commit -m "docs: Add troubleshooting section"
git push
```

**Example 3: Multiple changes**
```bash
git add .
git commit -m "feat: Add sound effects and improve UI"
git push
```

## 📥 Getting Changes FROM GitHub to Local

If you (or someone else) made changes on GitHub:

```bash
git pull
```

## 🔍 Check Current Status

```bash
# See what files have changed locally
git status

# See what changes you made
git diff

# See commit history
git log --oneline

# Check if you're in sync with GitHub
git fetch
git status
```

## 🚀 Quick Reference

| Action | Command |
|--------|---------|
| Check status | `git status` |
| Add all changes | `git add .` |
| Add specific file | `git add filename.py` |
| Commit changes | `git commit -m "your message"` |
| Push to GitHub | `git push` |
| Pull from GitHub | `git pull` |
| See history | `git log` |
| Undo local changes | `git checkout -- filename.py` |

## 💡 Best Practices

1. **Commit often** - Small, focused commits are better
2. **Write clear messages** - Explain WHAT and WHY you changed
3. **Pull before push** - Always `git pull` before starting work
4. **Test before commit** - Make sure code works before committing

## 🎯 Commit Message Tips

Good commit messages:
- `fix: Correct calibration timing issue`
- `feat: Add difficulty levels`
- `docs: Update installation instructions`
- `refactor: Improve hand tracking performance`

Bad commit messages:
- `stuff`
- `changes`
- `asdf`
- `updated`

## 🆘 Common Issues

### "Your branch is ahead of origin/main"
You have local commits not on GitHub yet.
```bash
git push
```

### "Your branch is behind origin/main"
GitHub has changes you don't have locally.
```bash
git pull
```

### "Merge conflict"
You and GitHub both changed the same file.
```bash
# Edit the conflicted files
# Look for <<<<<<< and >>>>>>> markers
# Fix the conflicts, then:
git add .
git commit -m "Resolve merge conflict"
git push
```

### Accidentally committed the wrong file
```bash
# Remove file from last commit (keeps local changes)
git reset HEAD~1 filename.py

# Or remove from staging before commit
git reset HEAD filename.py
```

## 📊 Workflow Diagram

```
┌─────────────┐
│  Your PC    │
│  (Local)    │
└──────┬──────┘
       │
       │ git add
       │ git commit
       │
       ▼
┌─────────────┐
│  Staging    │
│  Area       │
└──────┬──────┘
       │
       │ git push
       │
       ▼
┌─────────────┐
│   GitHub    │
│  (Remote)   │
└─────────────┘
       │
       │ git pull
       │
       ▼
┌─────────────┐
│  Your PC    │
│  (Updated)  │
└─────────────┘
```

---

**Remember**: Always `git pull` → make changes → `git add` → `git commit` → `git push`

