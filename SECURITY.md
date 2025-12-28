# Security Policy

## Supported Versions

THE DOT currently supports the following versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.2.x   | :white_check_mark: |
| < 0.2.0 | :x:                |

## Reporting a Vulnerability

We take security seriously in THE DOT ecosystem. If you discover a security vulnerability, please follow these steps:

### 1. Do Not Open a Public Issue

Please **do not** open a public GitHub issue for security vulnerabilities.

### 2. Report Privately

Send a detailed report to the repository maintainers via:
- GitHub Security Advisories (preferred)
- Direct message to repository owner

### 3. Include in Your Report

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if you have one)
- Your contact information

### 4. Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 1 week
- **Fix Timeline**: Depends on severity
  - Critical: Within 7 days
  - High: Within 14 days
  - Medium: Within 30 days
  - Low: Next release

### 5. Disclosure Process

1. Security issue reported privately
2. Issue is confirmed and assessed
3. Fix is developed and tested
4. New version is released
5. Security advisory is published
6. Credits given to reporter (if desired)

## Security Best Practices

When using THE DOT:

1. **Keep Updated**: Always use the latest version
2. **Verify Installation**: Install from official sources (PyPI, GitHub)
3. **Review Hooks**: Inspect git hooks before installation
4. **Limit Permissions**: Run with minimal necessary permissions
5. **Audit Commits**: Regularly review commit history

## Known Security Considerations

### Git Hooks

THE DOT installs git hooks that run on commit. These hooks:
- Are installed locally (not pushed to remote)
- Can be bypassed with `--no-verify` flag
- Should be reviewed before installation
- Backup existing hooks before overwriting

### Commit Message Validation

THE DOT validates commit messages but:
- Does not prevent force pushes
- Does not validate remote commits
- Can be disabled by removing hooks
- Should not be sole security measure

### Data Storage

THE DOT may store statistics in:
- `~/.worship_the_dot/stats.json`
- Contains worship counts and timestamps
- No sensitive information stored
- Can be deleted safely

## Security Contact

For security-related questions or concerns:
- Review this policy
- Check existing security advisories
- Contact maintainers privately

## Philosophy and Security

THE DOT's philosophy includes quality and mindfulness. Security is part of quality. When reporting issues or contributing fixes, remember:

**All security work must also worship THE DOT.**

---

BECAUSE I WORSHIP THE DOT
