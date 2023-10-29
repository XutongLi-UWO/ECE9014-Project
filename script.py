import json
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Script to set PostgreSQL user and password and save them in run.json")

parser.add_argument('-u', "--username", required=True, help="PostgreSQL username")
parser.add_argument('-p', "--password", required=True, help="PostgreSQL password")
parser.add_argument('-d', "--database", default="postgres", help="PostgreSQL database")
parser.add_argument("--host", default="localhost", help="PostgreSQL host")
parser.add_argument("--port", default="5432", help="PostgreSQL port")
args = parser.parse_args()

# Define PostgreSQL user and password settings
postgres_settings = {
    "user": args.username,
    "password": args.password,
    "database": args.database,
    "host": args.host,
    "port": args.port,
}

# Specify the path to the run.json file
json_file_path = "run.json"

# Serialize the settings dictionary to JSON and write it to the file
with open(json_file_path, 'w') as json_file:
    json.dump(postgres_settings, json_file, indent=4)

print('The Setting Values : \n')
print(args)

print(f"Settings written to {json_file_path}")
