#!/bin/bash
# simple-interest.sh
# Formula: SI = (P * R * T) / 100

echo "Enter Principal amount:"
read P
echo "Enter Rate of Interest (in %):"
read R
echo "Enter Time (in years):"
read T

SI=$(echo "scale=2; ($P * $R * $T)/100" | bc)
echo "Simple Interest = $SI"
