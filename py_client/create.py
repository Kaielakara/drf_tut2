import requests

endpoint = 'http://localhost:8000/dropbox/create/'

data = [
  {
    "owner": "kaiel",
    "content": "Detailed project specifications for the upcoming Dropbox clone including database schema and API endpoint definitions.",
    "is_locked": True,
    "is_public": False,
    "shared_with": ["kakashi", "rick"]
  },
  {
    "owner": "kaiel",
    "content": "Critical production server logs that track all unauthorized access attempts from the last twenty-four hours.",
    "is_locked": True,
    "is_public": False,
    "shared_with": []
  },
  {
    "owner": "kakashi",
    "content": "High resolution scans of the first volume of Icha Icha Paradise for reading during boring missions.",
    "is_locked": True,
    "is_public": False,
    "shared_with": ["rick"]
  },
  {
    "owner": "kakashi",
    "content": "A confidential evaluation report detailing the strengths and significant weaknesses of Naruto, Sasuke, and Sakura.",
    "is_locked": True,
    "is_public": False,
    "shared_with": ["kaiel"]
  },
  {
    "owner": "kakashi",
    "content": "A curated list of believable excuses to use when I arrive three hours late to training.",
    "is_locked": False,
    "is_public": True,
    "shared_with": ["bart"]
  },
  {
    "owner": "bart",
    "content": "The ultimate script for prank calling Moe's Tavern asking for someone named Amanda Hugginkiss immediately.",
    "is_locked": False,
    "is_public": True,
    "shared_with": ["rick"]
  },
  {
    "owner": "bart",
    "content": "A comprehensive list of detention lines that I still need to write on the blackboard before Skinner arrives.",
    "is_locked": False,
    "is_public": False,
    "shared_with": ["zenitsu"]
  },
  {
    "owner": "bart",
    "content": "Secret map showing exactly where I spray painted El Barto across the entire town of Springfield.",
    "is_locked": True,
    "is_public": False,
    "shared_with": ["zenitsu"]
  },
  {
    "owner": "rick",
    "content": "The mathematical formula required to synthesize portal fluid for interdimensional travel without melting the user.",
    "is_locked": True,
    "is_public": False,
    "shared_with": []
  },
  {
    "owner": "rick",
    "content": "Complete television guide for all the best shows available on Interdimensional Cable across the central finite curve.",
    "is_locked": False,
    "is_public": True,
    "shared_with": ["bart", "zenitsu"]
  },
  {
    "owner": "rick",
    "content": "Blueprints for a neutrino bomb capable of wiping out a planet but I probably got drunk and forgot.",
    "is_locked": True,
    "is_public": False,
    "shared_with": ["kaiel"]
  },
  {
    "owner": "rick",
    "content": "A cross-dimensional list of every single Jerry Smith that is too annoying to be allowed near the lab.",
    "is_locked": False,
    "is_public": False,
    "shared_with": ["kakashi"]
  },
  {
    "owner": "zenitsu",
    "content": "My private collection of beautiful descriptions regarding Nezuko and why she is the cutest demon ever.",
    "is_locked": True,
    "is_public": False,
    "shared_with": []
  },
  {
    "owner": "zenitsu",
    "content": "My final will and testament because I am absolutely certain that the next mission will be my end.",
    "is_locked": False,
    "is_public": True,
    "shared_with": []
  },
  {
    "owner": "zenitsu",
    "content": "Detailed observations on how to perfect the Thunder Breathing First Form without falling asleep immediately.",
    "is_locked": False,
    "is_public": False,
    "shared_with": ["kakashi"]
  }
]

post_res = requests.post(endpoint, json=data)

print(f"{post_res.json()}")