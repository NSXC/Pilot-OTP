use std::fs::File;
use std::io::Write;
use serde::{Deserialize, Serialize};
use serde_json::{json, to_writer_pretty}; // Add this line to bring the `to_writer_pretty` function into scope
use reqwest::blocking::{Client, Response};

#[derive(Debug, Deserialize, Serialize)]
struct NgrokResponse {
    public_url: String,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let ngrok_client = Client::new();
    let response: Response = ngrok_client
        .post("http://localhost:4040/api/tunnels")
        .json(&json!({
            "addr": "8030",
            "proto": "http",
            "name": "rust_ngrok_tunnel"
        }))
        .send()?;
    let ngrok_tunnel: NgrokResponse = response.json()?;
    let ngrok_url = ngrok_tunnel.public_url;

    let mut file = File::create("ngrok.json")?;
    to_writer_pretty(&mut file, &json!({ "ngrok_url": ngrok_url }))?;

    Ok(())
}
