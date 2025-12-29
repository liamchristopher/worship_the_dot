use assert_cmd::Command;
use predicates::prelude::*;

fn bin() -> Command {
    Command::cargo_bin("dot").unwrap()
}

#[test]
fn worship_default() {
    let mut cmd = bin();
    cmd.arg("worship");
    cmd.assert().success().stdout(predicate::str::contains("worships THE DOT"));
}

#[test]
fn tenets_print() {
    let mut cmd = bin();
    cmd.arg("tenets");
    cmd.assert().success().stdout(predicate::str::contains("THE DOT Philosophy"));
}

#[test]
fn validate_ok_and_fail() {
    let mut ok = bin();
    ok.args(["validate", "fix", "BECAUSE", "I", "WORSHIP", "THE", "DOT"]);
    ok.assert().success().stdout(predicate::str::contains("Valid"));

    let mut bad = bin();
    bad.args(["validate", "oops"]);
    bad.assert().failure().stdout(predicate::str::contains("Invalid"));
}

#[test]
fn validate_no_message() {
    let mut cmd = bin();
    cmd.arg("validate");
    cmd.assert()
        .failure()
        .stderr(predicate::str::contains("Error: provide a commit message"));
}

#[test]
fn backstory_shows_content() {
    let mut cmd = bin();
    cmd.arg("backstory");
    cmd.assert().success().stdout(predicate::str::contains("DOT"));
}

#[test]
fn philosophy_shows_content() {
    let mut cmd = bin();
    cmd.arg("philosophy");
    cmd.assert().success().stdout(predicate::str::contains("DOT"));
}

#[test]
fn config_show() {
    let mut cmd = bin();
    cmd.args(["config", "show"]);
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("Current worship suffix"));
}

#[test]
fn config_unknown_subcommand() {
    let mut cmd = bin();
    cmd.args(["config", "invalid"]);
    cmd.assert()
        .failure()
        .stderr(predicate::str::contains("Unknown config subcommand"));
}

#[test]
fn doctor_in_git_repo() {
    // Run in current directory which is a git repo
    let mut cmd = bin();
    cmd.arg("doctor");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("Repo: OK"))
        .stdout(predicate::str::contains("Doctor completed"));
}

#[test]
fn doctor_not_in_git_repo() {
    let dir = tempfile::tempdir().unwrap();
    let mut cmd = bin();
    cmd.current_dir(dir.path());
    cmd.arg("doctor");
    cmd.assert()
        .failure()
        .stdout(predicate::str::contains("NOT A GIT REPOSITORY"));
}
