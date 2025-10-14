# Contributing to Hand-Controlled Pong Game

First off, thank you for considering contributing to Hand-Controlled Pong Game! It's people like you that make this project such a great tool.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Standards

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
   ```bash
   git clone https://github.com/YOUR-USERNAME/hand-controlled-pong.git
   cd hand-controlled-pong
   ```
3. **Create a virtual environment** and install dependencies
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Create a branch** for your changes
   ```bash
   git checkout -b feature/your-feature-name
   ```

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and what you expected**
- **Include screenshots or videos if applicable**
- **Include your environment details:**
  - OS version
  - Python version
  - Package versions
  - Webcam model/type

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and explain the expected behavior**
- **Explain why this enhancement would be useful**

### Your First Code Contribution

Unsure where to begin? You can start by looking through these beginner-friendly issues:

- **Good First Issue** - issues that should only require a few lines of code
- **Help Wanted** - issues that may be more involved but are good for newcomers

### Pull Requests

1. **Update the README.md** with details of changes if applicable
2. **Update the requirements.txt** if you add new dependencies
3. **Add tests** if you're adding new functionality
4. **Ensure your code follows the style guidelines** (see below)
5. **Write clear commit messages** (see below)
6. **Update documentation** for any changed functionality

## Style Guidelines

### Python Style Guide

This project follows PEP 8 with some modifications:

- **Line length**: Maximum 100 characters (not 79)
- **Indentation**: 4 spaces (no tabs)
- **Imports**: Group in this order
  1. Standard library imports
  2. Related third-party imports
  3. Local application imports
- **Docstrings**: Use Google style docstrings

```python
def example_function(param1, param2):
    """
    Brief description of function.
    
    Args:
        param1 (type): Description of param1
        param2 (type): Description of param2
        
    Returns:
        type: Description of return value
        
    Raises:
        ExceptionType: Description of when this exception is raised
    """
    pass
```

### Code Organization

- **Constants**: Use UPPERCASE_WITH_UNDERSCORES
- **Classes**: Use PascalCase
- **Functions/Variables**: Use lowercase_with_underscores
- **Private members**: Prefix with single underscore `_private_var`

### Comments

- Write comments for complex logic
- Keep comments up-to-date when code changes
- Use inline comments sparingly
- Prefer self-documenting code over excessive comments

## Commit Messages

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that don't affect code meaning (formatting, etc.)
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **perf**: Performance improvement
- **test**: Adding missing tests
- **chore**: Changes to build process or auxiliary tools

### Examples

```
feat(hand-tracking): add two-hand support for multiplayer

Implemented detection and tracking of two hands simultaneously
to enable local multiplayer mode.

Closes #123
```

```
fix(calibration): prevent division by zero error

Added validation to ensure max_diff > min_diff before
calculating motion range.

Fixes #456
```

## Pull Request Process

1. **Ensure all tests pass** before submitting
2. **Update documentation** for any new features
3. **Rebase your branch** on the latest main branch
4. **Create a pull request** with a clear title and description
5. **Link any related issues** in the PR description
6. **Request review** from maintainers
7. **Address review comments** promptly
8. **Squash commits** if requested before merging

### PR Template

When creating a pull request, please include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests you ran

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing tests pass locally
```

## Development Setup

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.
```

### Linting

```bash
# Check code style
flake8 pong_game.py

# Format code
black pong_game.py
```

### Type Checking

```bash
# Run type checker
mypy pong_game.py
```

## Questions?

Feel free to open an issue with the `question` label if you have any questions about contributing!

## Attribution

This Contributing Guide is adapted from various open-source projects and best practices.

---

**Thank you for your contributions! 🎉**

