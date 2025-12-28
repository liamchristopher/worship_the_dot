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
        }
    }

    Ok(())
}
