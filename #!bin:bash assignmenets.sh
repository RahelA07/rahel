#!bin/bash 

eco-n"hello,do have a dog? "
value=1
while
[ $value == 1 ]
do

	read ans
	case $ans in
	yes|YES|y|Y )	echo "yes"
					echo "how many?"
					echo "oops thats a lot"
					echo "eneter the number again"
					value=1
					;;
	[nN][oO] ) 		echo "Thank you for letting me"
					echo "If you wish to buy a cat let us know"
					echo "re enter the number"
					echo "Have a nice day too."
					value=1
					;;
	* 				) echo Yes or No some form please;;
	vas
esac
done