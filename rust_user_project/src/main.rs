use serde::{Deserialize, Serialize};
use std::fs::File;
use std::io::Write;
use uuid::Uuid;

#[derive(Serialize, Deserialize, Debug)]
struct User {
    name: String,
    age: u32,
}

fn main() {
    // Create an instance of User
    let user = User {
        name: "Alice".to_string(),
        age: 30,
    };

    // Serialize the User instance to JSON
    let serialized_user = serde_json::to_string_pretty(&user).unwrap();
    println!("Serialized User:\n{}", serialized_user);

    // Generate a random UUID for the filename
    let random_id = Uuid::new_v4();
    let filename = format!("user_{}.json", random_id);

    // Write the serialized data to the file
    let mut file = File::create(&filename).unwrap();
    file.write_all(serialized_user.as_bytes()).unwrap();

    println!("User data saved to {}", filename);
}