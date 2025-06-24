# GitHub Follow Checker 🔍

A Python tool to analyze your GitHub follow relationships and discover who you follow but don't follow you back, and vice versa. Perfect for managing your GitHub social network!

## ✨ Features

- 🔄 **Two-way Analysis**: Find users you follow but who don't follow back, and users who follow you but you don't follow back
- 📊 **Detailed Statistics**: Get comprehensive stats about your follow relationships
- 🚀 **Rate Limit Optimization**: Support for GitHub Personal Access Tokens for higher API limits
- 📄 **Pagination Support**: Handles large follower/following lists automatically
- 🎨 **Clean Output**: Well-formatted results with direct links to user profiles
- ⚡ **Fast & Efficient**: Optimized API calls to minimize requests

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- `requests` library

### Installation

1. Clone this repository:
```bash
git clone https://github.com/kamlendras/github-follow-checker.git
cd github-follow-checker
```

2. Install dependencies:
```bash
pip install requests
```

3. Run the program:
```bash
python github_follow_checker.py
```

## 📖 Usage

1. **Enter your GitHub username** when prompted
2. **Optionally provide a GitHub Personal Access Token** for higher rate limits
3. **View your results** organized in clear sections

### Example Output

```
============================================================
GitHub Follow Analysis for: your_username
============================================================
Total following: 150
Total followers: 120
Mutual follows: 100
You follow but don't follow back: 50
They follow but you don't follow back: 20

❌ Users you follow but who DON'T follow you back (50):
  1. some_developer
     Profile: https://github.com/some_developer
  2. another_user
     Profile: https://github.com/another_user

👥 Users who follow you but you DON'T follow back (20):
  1. cool_contributor
     Profile: https://github.com/cool_contributor
  2. awesome_coder
     Profile: https://github.com/awesome_coder

============================================================
SUMMARY:
• Consider unfollowing 50 users who don't follow back
• Consider following back 20 users who follow you
```

## 🔑 GitHub Personal Access Token

For better performance and higher rate limits, create a GitHub Personal Access Token:

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a descriptive name
4. **No special scopes needed** - public access is sufficient
5. Copy the token and use it when prompted

### Rate Limits
- **Without token**: 60 requests per hour
- **With token**: 5,000 requests per hour

## 🛠️ Technical Details

### API Endpoints Used
- `GET /users/{username}/following` - Get users you follow
- `GET /users/{username}/followers` - Get your followers

### Dependencies
- `requests` - HTTP library for API calls
- `json` - JSON parsing (built-in)
- `typing` - Type hints (built-in)

## 📋 What You Can Do With The Results

### Users You Follow But Don't Follow Back (❌)
- **Unfollow inactive accounts** to clean up your timeline
- **Keep following** accounts you find valuable regardless of reciprocity
- **Reach out** to mutual connections who might have missed your follow

### Users Who Follow You But You Don't Follow Back (👥)
- **Follow back** people in your field or with shared interests
- **Check their profiles** to see if they align with your interests
- **Engage with their repositories** to build community

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

- 🐛 Report bugs by opening an issue
- 💡 Suggest new features
- 🔧 Submit pull requests for improvements
- 📚 Improve documentation

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool uses the GitHub API and respects all rate limits. It only accesses public information available through GitHub's API. Always follow GitHub's Terms of Service when using this tool.

## 🆘 Troubleshooting

### Common Issues

**"Error fetching data: 403"**
- You've hit the rate limit. Wait an hour or use a Personal Access Token

**"Error fetching data: 404"**
- Check that the username is spelled correctly and the user exists

**"Error: Make sure your username is correct"**
- Verify the username and ensure your internet connection is stable

### Getting Help

If you encounter issues:
1. Check the [Issues](https://github.com/kamlendras/github-follow-checker/issues) page
2. Create a new issue with:
   - Your operating system
   - Python version
   - Error message (if any)
   - Steps to reproduce

## 🌟 Star History

If you find this tool useful, please consider giving it a star! ⭐

## 📞 Contact

- GitHub: [@kamlendras](https://github.com/kamlendras)
- Issues: [Project Issues](https://github.com/kamlendras/github-follow-checker/issues)

---

Made with ❤️ for the GitHub community