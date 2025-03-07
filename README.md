# Secrets Management Demo

This project demonstrates different approaches to handling secrets in Python applications, from bad practices to better ones.

## Files

- `hardcoded_secrets.py` - **BAD PRACTICE**: API call with hardcoded secrets
- `config.py` - Configuration file containing secrets
- `config_secrets.py` - **BETTER PRACTICE**: API call using secrets from config file
- `env_secrets.py` - **GOOD PRACTICE**: API call using secrets from environment variables
- `.gitignore` - Shows which files should be excluded from version control
- `run_demo.sh` - Script to run all three examples

## Running the Demo

Make the script executable and run it:

```bash
chmod +x run_demo.sh
./run_demo.sh
```

## Security Scanning with TruffleHog

TruffleHog is a tool that scans repositories for secrets. When we run TruffleHog on this repository:

```bash
trufflehog .
```

It successfully detected:
1. The high entropy API key in `hardcoded_secrets.py` - demonstrating why hardcoding secrets in source code is dangerous
2. The high entropy API key in `run_demo.sh` - showing that secrets in scripts are also detectable

## Best Practices for Secrets Management

1. **NEVER hardcode secrets** in your source code
2. **BETTER**: Store secrets in configuration files that are excluded from version control (via .gitignore)
3. **BEST**: Use environment variables or dedicated secrets management services
4. Regularly scan your codebase for accidentally committed secrets
5. Rotate any secrets that have been exposed