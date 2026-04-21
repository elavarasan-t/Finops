import secrets
from datetime import datetime, timedelta, timezone
from pathlib import Path

def generate_api_key():

    api_key = secrets.token_hex(32)

    api_key_exp = datetime.now(timezone.utc) + timedelta(days=180)
    api_key_exp_str = api_key_exp.isoformat()

    env_path = Path(__file__).resolve().parent.parent / ".env"

    # read existing
    lines = []
    if env_path.exists():
        with open(env_path, "r") as f:
            lines = f.readlines()

    # update keys
    def update_key(lines, key, value):
        found = False
        for i, line in enumerate(lines):
            if line.startswith(f"{key}="):
                lines[i] = f"{key}={value}\n"
                found = True
                break
        if not found:
            lines.append(f"{key}={value}\n")
        return lines

    lines = update_key(lines, "API_KEY", str(api_key))
    lines = update_key(lines, "API_KEY_EXP", str(api_key_exp_str))

    # write back
    with open(env_path, "w") as f:
        f.writelines(lines)

    return api_key, api_key_exp_str
