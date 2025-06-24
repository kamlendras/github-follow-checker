import requests
import json
from typing import List, Set

class GitHubFollowChecker:
    def __init__(self, username: str, token: str = None):
        """
        Initialize the GitHub follow checker.
        
        Args:
            username: Your GitHub username
            token: GitHub personal access token (optional but recommended for higher rate limits)
        """
        self.username = username
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "GitHub-Follow-Checker"
        }
        
        if token:
            self.headers["Authorization"] = f"token {token}"
    
    def get_all_pages(self, url: str) -> List[dict]:
        """Fetch all pages of results from a paginated GitHub API endpoint."""
        all_data = []
        page = 1
        
        while True:
            response = requests.get(
                f"{url}?page={page}&per_page=100", 
                headers=self.headers
            )
            
            if response.status_code != 200:
                print(f"Error fetching data: {response.status_code}")
                print(f"Response: {response.text}")
                break
            
            data = response.json()
            if not data:  # No more data
                break
                
            all_data.extend(data)
            page += 1
            
            # Check if we've reached the last page
            if len(data) < 100:
                break
        
        return all_data
    
    def get_following(self) -> Set[str]:
        """Get list of users you follow."""
        url = f"{self.base_url}/users/{self.username}/following"
        following_data = self.get_all_pages(url)
        return {user['login'] for user in following_data}
    
    def get_followers(self) -> Set[str]:
        """Get list of your followers."""
        url = f"{self.base_url}/users/{self.username}/followers"
        followers_data = self.get_all_pages(url)
        return {user['login'] for user in followers_data}
    
    def find_non_mutual_follows(self) -> tuple[List[str], List[str]]:
        """Find users you follow but who don't follow you back, and vice versa."""
        print(f"Fetching following list for {self.username}...")
        following = self.get_following()
        
        print(f"Fetching followers list for {self.username}...")
        followers = self.get_followers()
        
        # Find users you follow but who don't follow you back
        you_follow_not_back = following - followers
        
        # Find users who follow you but you don't follow back
        they_follow_not_back = followers - following
        
        return sorted(list(you_follow_not_back)), sorted(list(they_follow_not_back))
    
    def display_results(self):
        """Display the results in a formatted way."""
        try:
            you_follow_not_back, they_follow_not_back = self.find_non_mutual_follows()
            
            print(f"\n{'='*60}")
            print(f"GitHub Follow Analysis for: {self.username}")
            print(f"{'='*60}")
            
            following = self.get_following()
            followers = self.get_followers()
            mutual_follows = following & followers
            
            print(f"Total following: {len(following)}")
            print(f"Total followers: {len(followers)}")
            print(f"Mutual follows: {len(mutual_follows)}")
            print(f"You follow but don't follow back: {len(you_follow_not_back)}")
            print(f"They follow but you don't follow back: {len(they_follow_not_back)}")
            
            # Show users you follow but who don't follow you back
            if you_follow_not_back:
                print(f"\n❌ Users you follow but who DON'T follow you back ({len(you_follow_not_back)}):")
                print("-" * 60)
                for i, user in enumerate(you_follow_not_back, 1):
                    print(f"{i:3d}. {user}")
                    print(f"     Profile: https://github.com/{user}")
                    if i % 10 == 0:  # Add spacing every 10 entries
                        print()
            else:
                print("\n✅ Great! Everyone you follow also follows you back!")
            
            # Show users who follow you but you don't follow back
            if they_follow_not_back:
                print(f"\n👥 Users who follow you but you DON'T follow back ({len(they_follow_not_back)}):")
                print("-" * 60)
                for i, user in enumerate(they_follow_not_back, 1):
                    print(f"{i:3d}. {user}")
                    print(f"     Profile: https://github.com/{user}")
                    if i % 10 == 0:  # Add spacing every 10 entries
                        print()
            else:
                print("\n✅ You follow back everyone who follows you!")
                
            # Summary
            print(f"\n{'='*60}")
            print("SUMMARY:")
            if not you_follow_not_back and not they_follow_not_back:
                print("🎉 Perfect! All your follows are mutual!")
            else:
                print(f"• Consider unfollowing {len(you_follow_not_back)} users who don't follow back")
                print(f"• Consider following back {len(they_follow_not_back)} users who follow you")
                
        except Exception as e:
            print(f"Error: {e}")
            print("Make sure your username is correct and your token (if provided) is valid.")

def main():
    print("GitHub Non-Mutual Followers Checker")
    print("=" * 40)
    
    # Get user input
    username = input("Enter your GitHub username: ").strip()
    
    print("\nOptional: Enter your GitHub Personal Access Token")
    print("(This increases rate limits from 60 to 5000 requests/hour)")
    print("You can create one at: https://github.com/settings/tokens")
    print("Leave empty if you don't have one:")
    token = input("Token (optional): ").strip()
    
    if not token:
        token = None
        print("\nNote: Using unauthenticated requests (60/hour limit)")
    else:
        print("\nUsing authenticated requests (5000/hour limit)")
    
    # Create checker and run analysis
    checker = GitHubFollowChecker(username, token)
    checker.display_results()

if __name__ == "__main__":
    main()