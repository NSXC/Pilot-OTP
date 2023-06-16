start cmd.exe /k ngrok http 80
start cmd.exe /k grab
start cmd.exe /k C:/Python311/python.exe "PATHTO SERVER"
start cmd.exe /k C:/Python311/python.exe "PATHTOMAIN"
cd "CDTORUSTPATH"
cargo build 
cargo run 
