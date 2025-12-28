use assert_cmd::Command;
use predicates::prelude::*;

fn bin() -> Command {
    Command::cargo_bin("the-dot").unwrap()
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

