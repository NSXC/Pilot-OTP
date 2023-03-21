start cmd.exe  start ngrok http 80
start cmd.exe  start grab 
start cmd.exe /k C:/Python311/python.exe "c:/Users/Josep/OneDrive/Desktop/Pilot OTP/server.py"
start cmd.exe /k C:/Python311/python.exe "c:/Users/Josep/OneDrive/Desktop/Pilot OTP/main.py"
cd "c:/Users/Josep/OneDrive/Desktop/Pilot OTP/login"
cargo build 
cargo run 