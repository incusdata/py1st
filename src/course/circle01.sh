#!/usr/bin/env sh
# Circle Calculator in UNIX Shell Script

printf "Radius? " ; read radius
circum=$(echo "scale=2; 2 * 3.14159 * $radius" | bc)
area=$(echo "scale=2; 3.14159 * ($radius * $radius)" | bc)

printf "Radius : %10.2f\n" $radius
printf "Circum.: %10.2f\n" $circum
printf "Area   : %10.2f\n" $area
