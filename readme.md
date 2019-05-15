# Insta-py Unfollow

Automatic unfollow script with insta-py from `non-follower` generated json file.

## Requirements

- Python 3.7
- Pip

`python3 -m pip install -r requirements.txt`

## Usage 

Edit `.env.default`, add your credentials and rename it `.env`

`python3 app.py --unfollow=not-followers.json --chunk=20`