#!/usr/bin/swift

// Swift 4

import Foundation

let characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789§`[];'\\,./±!@£$%^&*()_+~{}:\"|<>?".map { String($0) }
let passwordLength = 12

var password = ""
for _ in 0..<passwordLength {
	let index = Int(arc4random_uniform(UInt32(characters.count)))
	password = password + characters[index]
}

print("\nNew random password:\n\(password)\n")

let entropy = log2(pow(Double(characters.count), Double(passwordLength)))
print("\nEntropy ≤ log2(size of character set ^ password length) ≤ \(entropy) bits")
