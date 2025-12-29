use assert_cmd::Command;
use predicates::prelude::*;
use std::fs;

fn bin() -> Command {
    Command::cargo_bin("dot").unwrap()
}

#[test]
fn init_not_repo_errors() {
    let dir = tempfile::tempdir().unwrap();
    let mut cmd = bin();
    cmd.current_dir(dir.path());
    cmd.arg("init");
    cmd.assert().failure().stdout(predicate::str::contains("Not in a git repository"));
}

#[test]
fn init_creates_dot_ini_in_repo() {
    let dir = tempfile::tempdir().unwrap();
    // Initialize a git repo
    let status = std::process::Command::new("git")
        .arg("init")
        .current_dir(dir.path())
        .status()
        .unwrap();
    assert!(status.success());

    let mut cmd = bin();
    cmd.current_dir(dir.path());
    cmd.arg("init");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("Initialization complete"));
    let ini = dir.path().join(".dot.ini");
    let content = fs::read_to_string(ini).unwrap();
    assert!(content.contains("worship_suffix = BECAUSE I WORSHIP THE DOT"));
}

#[test]
fn init_with_existing_dot_ini() {
    let dir = tempfile::tempdir().unwrap();
    // Initialize a git repo
    let status = std::process::Command::new("git")
        .arg("init")
        .current_dir(dir.path())
        .status()
        .unwrap();
    assert!(status.success());

    // Create existing .dot.ini
    let ini = dir.path().join(".dot.ini");
    fs::write(&ini, "[dot]\nworship_suffix = CUSTOM SUFFIX\n").unwrap();

    let mut cmd = bin();
    cmd.current_dir(dir.path());
    cmd.arg("init");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("Found existing .dot.ini"))
        .stdout(predicate::str::contains("Initialization complete"));
}
