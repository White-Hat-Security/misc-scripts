
#!/bin/bash

# Simple random password generator using openssl

read -p "Enter desired length of the password(s): " PASS_LENGTH
read -p "Enter number of passwords to generate: "   PASS_QUANTITY

for P in $(seq $PASS_QUANTITY); do
    
    # openssl will gen 26 random numbers, in base 64
    openssl rand -base64 26 | cut -c1-$PASS_LENGTH

done

