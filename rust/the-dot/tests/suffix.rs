use assert_cmd::Command;
use predicates::prelude::*;
use std::fs;

fn bin() -> Command {
    Command::cargo_bin("dot").unwrap()
}

#[test]
fn suffix_default_is_present() {
    let mut cmd = bin();
    cmd.arg("suffix");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("Current worship suffix"))
        .stdout(predicate::str::contains("BECAUSE I WORSHIP THE DOT"));
}

#[test]
fn suffix_respects_env_override() {
    let mut cmd = bin();
    cmd.arg("suffix");
    cmd.env("DOT_WORSHIP_SUFFIX", "BECAUSE I ADORE THE DOT");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("BECAUSE I ADORE THE DOT"));
}

#[test]
fn suffix_reads_cwd_dot_ini() {
    let dir = tempfile::tempdir().unwrap();
    // Write .dot.ini in CWD
    let ini = dir.path().join(".dot.ini");
    fs::write(
        &ini,
        "[dot]\nworship_suffix = BECAUSE I REVERE THE DOT\n",
    )
    .unwrap();

    let mut cmd = bin();
    cmd.current_dir(dir.path());
    cmd.arg("suffix");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("BECAUSE I REVERE THE DOT"));
}

#[test]
fn suffix_reads_home_dot_ini() {
    let home = tempfile::tempdir().unwrap();
    fs::write(
        home.path().join(".dot.ini"),
        "[dot]\nworship_suffix = BECAUSE I HONOR THE DOT\n",
    )
    .unwrap();

    let mut cmd = bin();
    cmd.arg("suffix");
    cmd.env("HOME", home.path());
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("BECAUSE I HONOR THE DOT"));
}

#[test]
fn precedence_env_over_cwd_and_home() {
    let dir = tempfile::tempdir().unwrap();
    fs::write(
        dir.path().join(".dot.ini"),
        "[dot]\nworship_suffix = OVERRIDDEN BY ENV\n",
    )
    .unwrap();
    let home = tempfile::tempdir().unwrap();
    fs::write(
        home.path().join(".dot.ini"),
        "[dot]\nworship_suffix = ALSO OVERRIDDEN\n",
    )
    .unwrap();

    let mut cmd = bin();
    cmd.current_dir(dir.path());
    cmd.env("HOME", home.path());
    cmd.env("DOT_WORSHIP_SUFFIX", "BECAUSE I ADORE THE DOT");
    cmd.arg("suffix");
    cmd.assert()
        .success()
        .stdout(predicate::str::contains("BECAUSE I ADORE THE DOT"));
}

#[test]
fn validate_uses_overridden_suffix() {
    let mut cmd = bin();
    cmd.args([
        "validate",
        "Commit",
        "BECAUSE",
        "I",
        "HONOR",
        "THE",
        "DOT",
    ]);
    // Default suffix should fail for this custom message
    cmd.assert().failure();

    let mut cmd2 = bin();
    cmd2.env("DOT_WORSHIP_SUFFIX", "BECAUSE I HONOR THE DOT");
    cmd2.args([
        "validate",
        "Commit",
        "BECAUSE",
        "I",
        "HONOR",
        "THE",
        "DOT",
    ]);
    cmd2.assert()
        .success()
        .stdout(predicate::str::contains("Valid commit message"));
}

