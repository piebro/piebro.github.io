# /// script
# dependencies = [
#   "requests",
#   "beautifulsoup4",
# ]
# ///
import re
import requests
from bs4 import BeautifulSoup

# Function to get the star count from GitHub API
def get_star_count(repo_url):
    # Extract the owner and repo name from the URL
    parts = repo_url.split('/')
    owner, repo = parts[-2], parts[-1]
    
    # there is a rate limit of 60 requests per hour
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    
    # Make a request to the GitHub API
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data.get('stargazers_count', 0)
    else:
        print(f"Failed to fetch data for {repo_url}")
        return None

# Load the HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

star_tags = soup.find_all('a', class_='tag star')

for star_tag in star_tags:
    repo_url = star_tag['href'].replace('/stargazers', '')  # Remove /stargazers to get base repo URL
    star_or_heart_and_count = star_tag.text.strip()
    if star_or_heart_and_count.startswith('★'):
        current_star_count = int(star_or_heart_and_count[1:])
        new_star_count = get_star_count(repo_url)
        if new_star_count is not None and new_star_count != current_star_count:
            # Read the entire file content
            with open('index.html', 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Find the exact tag in the content using the href as reference
            pattern = f'<a href="{star_tag["href"]}"[^>]*>.*?</a>'
            old_tag = re.search(pattern, content).group(0)
            # Create new tag with same format but updated count
            new_tag = re.sub(r'\d+</a>$', f'{new_star_count}</a>', old_tag)
            
            # Replace the old tag with the new one
            updated_content = content.replace(old_tag, new_tag)
            
            # Write the updated content back to the file
            with open('index.html', 'w', encoding='utf-8') as file:
                file.write(updated_content)