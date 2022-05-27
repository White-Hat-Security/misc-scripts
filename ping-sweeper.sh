
#!/bin/bash

# Simple ping sweeper

read -p "Enter the subnet (x.x.x ): " SUBNET

for IP in $(seq 1 254); do
    ping -c 1 $SUBNET.$IP

done

