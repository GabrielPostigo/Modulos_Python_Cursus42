import os
import sys
from dotenv import dotenv_values, load_dotenv

PLACEHOLDER_API_KEY: str = "example_api_key_12345"


def read_mode(env_path: str) -> str:
    """Resolve MATRIX_MODE: env variable, then .env, then default."""
    env_mode: str | None = os.environ.get("MATRIX_MODE")
    if env_mode:
        return env_mode
    if os.path.isfile(env_path):
        file_mode: str | None = dotenv_values(env_path).get("MATRIX_MODE")
        if file_mode:
            return file_mode
    return "development"


def get_config() -> dict[str, str]:
    """Read all required configuration variables from the environment."""
    keys: list[str] = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]
    return {key: os.environ.get(key, "") for key in keys}


def gitignore_ignores_env(script_dir: str) -> bool:
    """Return True if the .gitignore next to this script lists .env."""
    gitignore_path: str = os.path.join(script_dir, ".gitignore")
    if not os.path.isfile(gitignore_path):
        return False
    with open(gitignore_path, "r") as f:
        return any(line.strip() in (".env", "/.env") for line in f)


def describe_database(url: str) -> str:
    """Return a human-readable database status."""
    if not url:
        return "[NOT CONFIGURED]"
    if "localhost" in url or "sqlite" in url or "127.0.0.1" in url:
        return "Connected to local instance"
    return "Connected to remote instance"


def describe_api(key: str) -> str:
    """Return API authentication status."""
    if not key or key == PLACEHOLDER_API_KEY:
        return "NOT authenticated"
    return "Authenticated"


def describe_zion(endpoint: str) -> str:
    """Return Zion network status."""
    if not endpoint:
        return "Offline"
    return "Online"


def show_mode_details(mode: str, log_level: str) -> None:
    """Print what the selected mode actually does."""
    debug_state: str = "ENABLED" if log_level == "DEBUG" else "DISABLED"
    shown_level: str = log_level or "not set"
    print()
    if mode == "production":
        print("  [PRODUCTION MODE]")
        print("  - Secrets must come from environment variables")
        print("  - .env file is ignored")
        print("  - Missing configuration aborts the program")
    else:
        print("  [DEVELOPMENT MODE]")
        print("  - .env file is used for local configuration")
        print("  - Missing configuration only produces warnings")
    print(f"  - Debug logging is {debug_state} (LOG_LEVEL={shown_level})")


def security_check(
    script_dir: str,
    env_file_exists: bool,
    env_loaded: bool,
    mode: str,
    config: dict[str, str],
) -> None:
    """Run real environment checks and print the results."""
    print()
    print("Environment security check:")

    if gitignore_ignores_env(script_dir):
        print("[OK] .env is listed in .gitignore")
    else:
        print("[WARN] .env is NOT in .gitignore - secrets could leak")

    if config["API_KEY"] == PLACEHOLDER_API_KEY:
        print("[WARN] API_KEY still has the example value")
    elif config["API_KEY"]:
        print("[OK] API_KEY is set to a non-example value")

    if mode == "production":
        print("[OK] Production mode: config comes from environment")
    elif env_loaded:
        print("[OK] .env file loaded for development")
    elif env_file_exists:
        print("[WARN] .env file found but not loaded")
    else:
        print("[WARN] .env file not found - using environment variables only")


def main() -> None:
    """Main entry point for the oracle program."""
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    script_dir: str = os.path.dirname(os.path.abspath(__file__))
    env_path: str = os.path.join(script_dir, ".env")
    env_file_exists: bool = os.path.isfile(env_path)

    mode: str = read_mode(env_path)

    # In production the .env file is ignored on purpose.
    env_loaded: bool = False
    if mode != "production" and env_file_exists:
        load_dotenv(dotenv_path=env_path, override=False)
        env_loaded = True

    config: dict[str, str] = get_config()
    missing: list[str] = [key for key, value in config.items() if not value]

    if missing and mode == "production":
        print("ERROR: Missing configuration in production: "
              + ", ".join(missing), file=sys.stderr)
        sys.exit(1)

    if missing:
        print("WARNING: Missing configuration variables:")
        for key in missing:
            print(f"  - {key}")
        print()
        print("Copy .env.example to .env and fill in your values.")
        print()

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {describe_database(config['DATABASE_URL'])}")
    print(f"API Access: {describe_api(config['API_KEY'])}")
    print(f"Log Level: {config['LOG_LEVEL'] or '[NOT SET]'}")
    print(f"Zion Network: {describe_zion(config['ZION_ENDPOINT'])}")

    show_mode_details(mode, config["LOG_LEVEL"])
    security_check(script_dir, env_file_exists, env_loaded, mode, config)

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
