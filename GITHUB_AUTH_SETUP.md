# GitHub Authentication Setup Guide

You're getting an authentication error because GitHub no longer supports password authentication. You need to set up either SSH keys or a Personal Access Token.

## 🔑 Option 1: SSH Keys (Recommended)

### Step 1: Generate SSH Key

```bash
# Generate a new SSH key
ssh-keygen -t ed25519 -C "ekagansahin@users.noreply.github.com"

# When prompted:
# - Press ENTER to accept default file location (~/.ssh/id_ed25519)
# - Press ENTER for no passphrase (or create one for extra security)
# - Press ENTER again to confirm
```

### Step 2: Start SSH Agent and Add Key

```bash
# Start the ssh-agent
eval "$(ssh-agent -s)"

# Add your SSH key to the agent
ssh-add ~/.ssh/id_ed25519
```

### Step 3: Copy Your Public Key

```bash
# Display your public key
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output (starts with `ssh-ed25519` and ends with your email).

### Step 4: Add SSH Key to GitHub

1. Go to GitHub: https://github.com/settings/keys
2. Click **"New SSH key"**
3. Title: `Linux Mint - Trifaze Project` (or any name you prefer)
4. Key type: **Authentication Key**
5. Paste your public key in the "Key" field
6. Click **"Add SSH key"**

### Step 5: Change Repository URL to SSH

```bash
cd /home/mint/python/game/Trifaze

# Remove the old HTTPS remote
git remote remove origin

# Add SSH remote
git remote add origin git@github.com:ekagansahin/hand-controlled-pong.git

# Verify
git remote -v
```

### Step 6: Test Connection

```bash
ssh -T git@github.com
```

You should see: `Hi ekagansahin! You've successfully authenticated...`

### Step 7: Push to GitHub

```bash
git push -u origin main
```

---

## 🎫 Option 2: Personal Access Token (PAT)

### Step 1: Create a Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Note: `hand-controlled-pong-repo`
4. Expiration: Choose your preference (e.g., 90 days or No expiration)
5. Select scopes:
   - ✅ **repo** (Full control of private repositories)
6. Scroll down and click **"Generate token"**
7. **⚠️ IMPORTANT**: Copy the token immediately! You won't see it again!

Example token format: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Step 2: Use Token When Pushing

```bash
cd /home/mint/python/game/Trifaze

# Try to push
git push -u origin main

# When prompted for username: ekagansahin
# When prompted for password: PASTE YOUR TOKEN (not your GitHub password!)
```

### Step 3: (Optional) Save Token to Avoid Re-entering

```bash
# Configure Git to cache credentials for 1 hour
git config --global credential.helper cache

# Or cache for longer (e.g., 1 month = 2592000 seconds)
git config --global credential.helper 'cache --timeout=2592000'

# Or store permanently (less secure but convenient)
git config --global credential.helper store
```

Then push again and enter your token - it will be saved.

---

## 🚀 Quick Setup Script (SSH Method)

I recommend SSH. Here's a quick script:

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "ekagansahin@users.noreply.github.com" -f ~/.ssh/id_ed25519 -N ""

# Start SSH agent and add key
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Display public key (copy this!)
echo "📋 Copy this SSH key and add it to GitHub:"
echo "   https://github.com/settings/keys"
echo ""
cat ~/.ssh/id_ed25519.pub
echo ""
echo "Press ENTER after you've added the key to GitHub..."
read

# Update repository to use SSH
cd /home/mint/python/game/Trifaze
git remote remove origin 2>/dev/null
git remote add origin git@github.com:ekagansahin/hand-controlled-pong.git

# Test connection
echo "Testing SSH connection..."
ssh -T git@github.com

# Push to GitHub
echo "Pushing to GitHub..."
git push -u origin main
```

---

## 📝 Which Method Should You Choose?

### Use SSH if:
- ✅ You want a one-time setup
- ✅ You don't want to enter passwords/tokens
- ✅ You work with Git regularly
- ✅ **RECOMMENDED for most users**

### Use PAT if:
- You only need temporary access
- You're behind a strict firewall that blocks SSH
- You prefer token-based authentication

---

## 🆘 Troubleshooting

### SSH Connection Test Failed?
```bash
# Check if SSH key is added to agent
ssh-add -l

# If not listed, add it
ssh-add ~/.ssh/id_ed25519
```

### Still Getting Authentication Error?
```bash
# Verify remote URL
git remote -v

# Should show:
# origin  git@github.com:ekagansahin/hand-controlled-pong.git (fetch)
# origin  git@github.com:ekagansahin/hand-controlled-pong.git (push)
```

### Token Not Working?
- Make sure you copied the entire token
- Verify the token has `repo` scope
- Check if the token has expired
- Use the token as your password, NOT your GitHub account password

---

**Ready to proceed? I recommend Option 1 (SSH keys)!**

