use anyhow::Result;
use clap::{Parser, Subcommand};
use the_dot::Dot;

#[derive(Parser)]
#[command(name = "the-dot")] 
#[command(version, about = "THE DOT — Rust CLI", long_about = None)]
struct Cli {
    #[command(subcommand)]
    command: Option<Commands>,
}

#[derive(Subcommand)]
enum Commands {
    /// Register worship of THE DOT
    Worship { name: Option<String> },
    /// Display THE DOT philosophy
    Tenets,
    /// Validate a commit message
    Validate { message: Vec<String> },
    /// Show the active worship suffix and source hint
    Suffix,
    /// Show THE DOT backstory (timeless)
    Backstory,
    /// Config commands
    Config { #[arg(default_value_t = String::from("show"))] sub: String },
    /// Doctor: verify environment and practice (minimal parity)
    Doctor,
    /// Initialize: write .dot.ini at repo root if missing
    Init,
}

fn main() -> Result<()> {
    let cli = Cli::parse();
    let mut dot = Dot::new();

    match cli.command.unwrap_or(Commands::Worship { name: None }) {
        Commands::Worship { name } => {
            let name = name.unwrap_or_else(|| "CLI User".to_string());
            println!("{}", dot.worship(&name));
        }
        Commands::Tenets => {
            println!("THE DOT Philosophy:");
            for (i, t) in dot.tenets().iter().enumerate() {
                println!("  {}. {}", i + 1, t);
            }
        }
        Commands::Validate { message } => {
            if message.is_empty() {
                eprintln!("Error: provide a commit message to validate");
                std::process::exit(1);
            }
            let msg = message.join(" ");
            if dot.validate_commit(msg) {
                println!("✓ Valid commit message - properly worships THE DOT");
            } else {
                println!("✗ Invalid commit message - must end with 'BECAUSE I WORSHIP THE DOT'");
                std::process::exit(1);
            }
        }
        Commands::Suffix => {
            println!("Current worship suffix:\n  {}", the_dot::worship_suffix());
            println!("Source:\n  {}", the_dot::worship_suffix_source());
        }
        Commands::Backstory => {
            // Keep in sync with Python's backstory for compatibility
            println!("{}", include_str!("../../../../docs/BACKSTORY.md"));
        }
        Commands::Config { sub } => {
            match sub.as_str() {
                "show" => {
                    println!("Current worship suffix:\n  {}", the_dot::worship_suffix());
                    println!("Source:\n  {}", the_dot::worship_suffix_source());
                }
                _ => {
                    eprintln!("Unknown config subcommand: {}", sub);
                    std::process::exit(1);
                }
            }
        }
        Commands::Doctor => {
            // Minimal parity: report when not in a git repo
            let out = std::process::Command::new("git")
                .args(["rev-parse", "--git-dir"])
                .output();
            match out {
                Ok(o) if o.status.success() => {
                    let git_dir = String::from_utf8_lossy(&o.stdout).trim().to_string();
                    println!("Repo: OK ({})", git_dir);
                    println!("Suffix: {}", the_dot::worship_suffix());
                    println!("✓ Doctor completed");
                }
                _ => {
                    println!("Repo: NOT A GIT REPOSITORY");
                    std::process::exit(1);
                }
            }
        }
        Commands::Init => {
            // Require git repository (parity with Python init)
            let git_dir = std::process::Command::new("git")
                .args(["rev-parse", "--git-dir"]) 
                .output();
            if git_dir.as_ref().map(|o| o.status.success()).unwrap_or(false) == false {
                println!("Error: Not in a git repository");
                std::process::exit(1);
            }
            // Determine repo root
            let toplevel = std::process::Command::new("git")
                .args(["rev-parse", "--show-toplevel"]) 
                .output()
                .expect("git present");
            let root = String::from_utf8_lossy(&toplevel.stdout).trim().to_string();
            let ini_path = std::path::Path::new(&root).join(".dot.ini");
            if ini_path.exists() {
                println!("\u2713 Found existing .dot.ini configuration");
            } else {
                // Write default suffix
                let content = "[dot]\nworship_suffix = BECAUSE I WORSHIP THE DOT\n";
                std::fs::write(&ini_path, content).expect("write .dot.ini");
                println!("\u2713 Created {}", ini_path.display());
            }
            println!("\u2713 Initialization complete");
        }
    }

    Ok(())
}
