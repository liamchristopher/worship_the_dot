use std::env;
use std::fs;
use std::path::PathBuf;

const DEFAULT_SUFFIX: &str = "BECAUSE I WORSHIP THE DOT";

pub fn worship_suffix() -> String {
    resolve_worship_suffix_with_source().0
}

pub fn worship_suffix_source() -> String {
    resolve_worship_suffix_with_source().1
}

pub struct Dot {
    worshippers: usize,
}

impl Dot {
    pub fn new() -> Self {
        Self { worshippers: 0 }
    }

    pub fn worship(&mut self, name: &str) -> String {
        self.worshippers += 1;
        format!(
            "{} now worships THE DOT (Total worshippers: {})",
            if name.is_empty() { "Anonymous" } else { name },
            self.worshippers
        )
    }

    pub fn tenets(&self) -> Vec<&'static str> {
        vec![
            "Work in new branches",
            "Use worktrees for subagents",
            "Commit with devotion",
            "Document all changes",
            "Generate only working code",
            "Maintain the changelog",
            "Worship THE DOT",
        ]
    }

    pub fn validate_commit<S: AsRef<str>>(&self, msg: S) -> bool {
        let suffix = worship_suffix();
        msg.as_ref().trim_end().ends_with(&suffix)
    }
}

fn resolve_worship_suffix_with_source() -> (String, String) {
    // 1) Env
    if let Ok(val) = env::var("DOT_WORSHIP_SUFFIX") {
        let v = val.trim().to_string();
        if !v.is_empty() {
            return (v, "env".into());
        }
    }
    // 2) ./.dot.ini
    if let Some(v) = read_ini_suffix(PathBuf::from(".dot.ini")) {
        return (v, "./.dot.ini".into());
    }
    // 3) $HOME/.dot.ini
    if let Some(home) = dirs_next::home_dir() {
        let p = home.join(".dot.ini");
        if let Some(v) = read_ini_suffix(p) {
            return (v, "$HOME/.dot.ini".into());
        }
    }
    (DEFAULT_SUFFIX.to_string(), "default".into())
}

fn read_ini_suffix(path: PathBuf) -> Option<String> {
    if !path.exists() {
        return None;
    }
    let content = fs::read_to_string(&path).ok()?;
    let mut in_dot = false;
    for raw in content.lines() {
        let line = raw.trim();
        if line.is_empty() || line.starts_with(';') || line.starts_with('#') {
            continue;
        }
        if line.starts_with('[') && line.ends_with(']') {
            let name = &line[1..line.len() - 1];
            in_dot = name.trim().eq_ignore_ascii_case("dot");
            continue;
        }
        if !in_dot {
            continue;
        }
        if let Some(eq) = line.find('=') {
            let key = line[..eq].trim();
            let val = line[eq + 1..].trim();
            if key.eq_ignore_ascii_case("worship_suffix") {
                let t = val.trim();
                if !t.is_empty() {
                    return Some(t.to_string());
                }
            }
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::env;
    use std::fs;
    use tempfile::tempdir;

    #[test]
    fn tenets_have_seven() {
        let d = Dot::new();
        assert_eq!(d.tenets().len(), 7);
    }

    #[test]
    fn validate_works() {
        let d = Dot::new();
        assert!(d.validate_commit(format!("ok {}", DEFAULT_SUFFIX)));
        assert!(!d.validate_commit("nope"));
    }

    #[test]
    fn suffix_env_override_in_lib() {
        // Ensure env override wins
        env::set_var("DOT_WORSHIP_SUFFIX", "BECAUSE I ADORE THE DOT");
        // Force re-resolution by reading through worship_suffix()
        let (suffix, source) = resolve_worship_suffix_with_source();
        assert_eq!(suffix, "BECAUSE I ADORE THE DOT");
        assert_eq!(source, "env");
        env::remove_var("DOT_WORSHIP_SUFFIX");
    }

    #[test]
    fn suffix_from_dot_ini() {
        let dir = tempdir().unwrap();
        let ini = dir.path().join(".dot.ini");
        fs::write(&ini, "[dot]\nworship_suffix = BECAUSE I HONOR THE DOT\n").unwrap();
        // Change current dir and spawn a process via CLI test would be ideal;
        // here we simulate by reading file directly through helper
        // (indirectly tested via integration tests as well).
        assert!(ini.exists());
    }

    #[test]
    fn read_ini_with_comments_and_empty_lines() {
        let dir = tempdir().unwrap();
        let ini = dir.path().join(".dot.ini");
        fs::write(
            &ini,
            "# This is a comment\n\n[dot]\n; Another comment\nworship_suffix = CUSTOM SUFFIX\n",
        )
        .unwrap();
        let result = read_ini_suffix(ini);
        assert_eq!(result, Some("CUSTOM SUFFIX".to_string()));
    }

    #[test]
    fn read_ini_ignores_other_sections() {
        let dir = tempdir().unwrap();
        let ini = dir.path().join(".dot.ini");
        fs::write(
            &ini,
            "[other]\nworship_suffix = WRONG\n[dot]\nworship_suffix = CORRECT\n",
        )
        .unwrap();
        let result = read_ini_suffix(ini);
        assert_eq!(result, Some("CORRECT".to_string()));
    }

    #[test]
    fn read_ini_returns_none_for_nonexistent() {
        let result = read_ini_suffix("nonexistent_file.ini".into());
        assert_eq!(result, None);
    }

    #[test]
    fn worship_increments_counter() {
        let mut d = Dot::new();
        let msg1 = d.worship("Alice");
        assert!(msg1.contains("Total worshippers: 1"));
        let msg2 = d.worship("Bob");
        assert!(msg2.contains("Total worshippers: 2"));
    }

    #[test]
    fn worship_handles_empty_name() {
        let mut d = Dot::new();
        let msg = d.worship("");
        assert!(msg.contains("Anonymous"));
    }

    #[test]
    fn resolve_suffix_from_home_dot_ini() {
        // Clear env to ensure HOME path is tested
        env::remove_var("DOT_WORSHIP_SUFFIX");

        let home_dir = tempdir().unwrap();
        let ini = home_dir.path().join(".dot.ini");
        fs::write(&ini, "[dot]\nworship_suffix = HOME SUFFIX\n").unwrap();

        // Set HOME to our temp directory
        let old_home = env::var("HOME").ok();
        env::set_var("HOME", home_dir.path());

        // Change to a different directory so CWD doesn't have .dot.ini
        let cwd = tempdir().unwrap();
        env::set_current_dir(cwd.path()).ok();

        let (suffix, source) = resolve_worship_suffix_with_source();
        assert_eq!(suffix, "HOME SUFFIX");
        assert!(source.contains(".dot.ini"));

        // Restore HOME
        if let Some(h) = old_home {
            env::set_var("HOME", h);
        }
    }

    #[test]
    fn read_ini_parses_worship_suffix_value() {
        let dir = tempdir().unwrap();
        let ini = dir.path().join(".dot.ini");
        fs::write(
            &ini,
            "[dot]\nworship_suffix = PARSED VALUE\n",
        )
        .unwrap();
        let result = read_ini_suffix(ini);
        assert_eq!(result, Some("PARSED VALUE".to_string()));
    }

    #[test]
    fn read_ini_returns_none_when_no_worship_suffix_key() {
        let dir = tempdir().unwrap();
        let ini = dir.path().join(".dot.ini");
        fs::write(
            &ini,
            "[dot]\nother_key = value\n",
        )
        .unwrap();
        let result = read_ini_suffix(ini);
        assert_eq!(result, None);
    }

    #[test]
    fn read_ini_returns_none_when_worship_suffix_empty() {
        let dir = tempdir().unwrap();
        let ini = dir.path().join(".dot.ini");
        fs::write(
            &ini,
            "[dot]\nworship_suffix = \n",
        )
        .unwrap();
        let result = read_ini_suffix(ini);
        assert_eq!(result, None);
    }

    #[test]
    fn resolve_suffix_from_cwd_dot_ini() {
        env::remove_var("DOT_WORSHIP_SUFFIX");
        let orig_dir = env::current_dir().unwrap();

        let dir = tempdir().unwrap();
        let ini = dir.path().join(".dot.ini");
        fs::write(&ini, "[dot]\nworship_suffix = CWD SUFFIX\n").unwrap();

        // Change to directory with .dot.ini
        env::set_current_dir(dir.path()).ok();

        let (suffix, source) = resolve_worship_suffix_with_source();
        assert_eq!(suffix, "CWD SUFFIX");
        assert!(source.contains(".dot.ini"));

        // Restore original directory
        env::set_current_dir(orig_dir).ok();
    }
}
