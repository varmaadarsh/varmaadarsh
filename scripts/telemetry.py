import os
import requests

USERNAME = "varmaadarsh"

TOKEN = os.environ.get("GH_TOKEN")

query = """
query($username:String!){
  user(login:$username){
    contributionsCollection{
      contributionCalendar{
        totalContributions
        weeks{
          contributionDays{
            contributionCount
            date
          }
        }
      }
    }
  }
}
"""

variables = {
    "username": USERNAME
}

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.post(
    "https://api.github.com/graphql",
    json={
        "query": query,
        "variables": variables
    },
    headers=headers
)

print(response.status_code)
print(response.json())
