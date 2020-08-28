#!/bin/bash
echo "X0R-ing images ...."
# convert flag.png lemur.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" key.png
convert flag.png lemur.png -evaluate-sequence Xor key.png