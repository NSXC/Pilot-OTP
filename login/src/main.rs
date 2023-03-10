#![allow(dead_code)]
#![allow(non_snake_case)]
#![allow(unused_imports)]
#![allow(unused_mut)]
#![allow(unused_variables)]
#![feature(proc_macro_hygiene, decl_macro)]
#![allow(unused_attributes)]
#![allow(deprecated)]
//remove if this is unreachable
#[macro_use] extern crate rocket;
use rocket::routes;
use rocket::post;
use std::process::Command;
use std::thread;
use std::time::{Duration, SystemTime};
use std::fs;
use mysql::*;
use mysql::prelude::*;
use chrono::prelude::*;
use bcrypt::{hash, verify, DEFAULT_COST};
#[get("/add_user?<username>&<role>&<subtype>")]
fn add_user(username: String, role: String,subtype: String) -> String {
    let time;
    if subtype == "week" {
        time = 7;
    } else if subtype == "day" {
        time = 1;
    } else if subtype == "month" {
        time = 30;
    }  else if subtype == "lifetime" {
        time = 36525;
    }else {
        return format!("Not a valid subtype");
    }
    let url = "mysql://root:admin@localhost:3306/users";
    
    let pool = Pool::new(url).unwrap();
    let mut conn = pool.get_conn().unwrap();
    let now = Local::now().naive_local();
    let expiration_date = now + chrono::Duration::days(time);
    let user_exists: bool = conn.exec_first(
        "SELECT COUNT(*) FROM userinfo WHERE username = :username",
        params! {
            "username" => username.clone(),
        }
    ).unwrap().unwrap_or((0,)).0 > 0;

    if user_exists {
        return format!("User '{}' already exists", username);
    }

    let params = params! {
        "account_creation_date" => now,
        "expiration_date" => expiration_date,
        "username" => username.clone(),
        "role" => role,
    };
    conn.exec_drop("INSERT INTO userinfo (account_creation_date, expiration_date, username, role) VALUES (:account_creation_date, :expiration_date, :username, :role)", params).unwrap();
    format!("200")
}
#[get("/verify?<username>")]
fn verify_user(username: String) -> String {
    let url = "mysql://root:admin@localhost:3306/users";
    let pool = Pool::new(url).unwrap();
    let mut conn = pool.get_conn().unwrap();
    let user_exists: bool = conn.exec_first(
        "SELECT COUNT(*) FROM userinfo WHERE username = :username",
        params! {
            "username" => username.clone(),
        }
    ).unwrap().unwrap_or((0,)).0 > 0;

    if !user_exists {
        return format!("404");
    }

    format!("200")
}
#[get("/dash?<username>")]
fn dash(username: String) -> String {
    let url = "mysql://root:admin@localhost:3306/users";
    let pool = Pool::new(url).unwrap();
    let mut conn = pool.get_conn().unwrap();
    let user_exists: bool = conn.exec_first(
        "SELECT COUNT(*) FROM userinfo WHERE username = :username",
        params! {
            "username" => username.clone(),
        }
    ).unwrap().unwrap_or((0,)).0 > 0;

    if !user_exists {
        return format!("404");
    }
    let (role,): (String,) = conn.exec_first(
        "SELECT role FROM userinfo WHERE username = :username",
        params! {
            "username" => username.clone(),
        }
    ).unwrap().unwrap_or((String::new(),));
    if role == "admin"|| role == "owner"{
        return format!("200");
    }else{
        return format!("403");
    }
}

fn main() {
    

    let url = "mysql://root:admin@localhost:3306/users";
    let pool = Pool::new(url).unwrap();
    let mut conn = pool.get_conn().unwrap();
    let table_exists = conn.query_first::<u8, _>("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'users' AND table_name = 'userinfo'")
    .unwrap()
    .unwrap_or(0) > 0;
    if !table_exists {
        conn.query_drop(
            "CREATE TABLE userinfo (
                id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                account_creation_date DATETIME NOT NULL,
                expiration_date DATETIME NOT NULL,
                username VARCHAR(255) UNIQUE NOT NULL,
                role VARCHAR(30) NOT NULL
            )"
        ).unwrap();
    }else{
        println!("Table users Found");
    }
    let rocket = rocket::ignite().mount("/", routes![add_user,verify_user,dash]);
    let bg_pool = pool.clone();
    thread::spawn(move || {
        loop {
            let mut bg_conn = bg_pool.get_conn().unwrap();
            let now = Utc::now().naive_utc();
            let expired_users: Vec<(String,)> = bg_conn.exec(
                "SELECT username FROM userinfo WHERE expiration_date < :now",
                params! {
                    "now" => now,
                }
            ).unwrap();

            for (username,) in expired_users {
                bg_conn.exec_drop(
                    "DELETE FROM userinfo WHERE username = :username",
                    params! {
                        "username" => username.clone(),
                    }
                ).unwrap();
                println!("Removed expired user: {}", username);
            }

            thread::sleep(Duration::from_secs(300)); // Check every 5 minutes
        }
    });
    rocket.launch();
}
