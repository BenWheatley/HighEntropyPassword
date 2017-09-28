#!/usr/bin/swift

// Swift 4

import Foundation

let characters = "0123456789".map { String($0) }
let pinLength = 4

var pin = ""
for _ in 0..<pinLength {
	let index = Int(arc4random_uniform(UInt32(characters.count)))
	pin = pin + characters[index]
}

print("\nNew random PIN:\n\(pin)\n")

let entropy = log2(pow(Double(characters.count), Double(pinLength)))
print("\nEntropy ≤ log2(size of character set ^ pin length) ≤ \(entropy) bits\n")
