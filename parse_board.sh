#!/bin/bash

# 8万 6条 7饼  中  白  花 2饼 7万 
# 6万 9条  白 8条  发  白 4万 1万 
# 9饼 1条  白 3条  发 3万 8饼 1饼 
# 4饼 2万 7条  发 5万  发  中 2条 
#  中 9万 5条 5饼 3饼 4条  中 6饼 

input=$1
sed -e "s/\([0-9]\)/\1, /g" -e "s/饼/0/g" -e "s/条/1/g" -e "s/万/2/g" \
	-e "s/\([0-9]\), \([0-9]\)/Card(\2,\1)/g" \
	-e "s/ 中/Card(3,None)/g" -e "s/ 发/Card(4,None)/g" \
   	-e "s/ 白/Card(5,None)/g" -e "s/ 花/Card(6,None)/g" \
$input | perl -e '
my @table;
while(<>) {
	my @row = split " ", $_;
	push @table, \@row;
}
for(my $j = 0; $j <= $#{$table[0]}; $j++) {
	for(my $i = 0; $i <= $#table; $i++) {
		print "$table[$i]->[$j]";
		print " " if $i != $#table;
	}
	print "\n";
}
' | sed -e "s/^/[/" -e "s/$/],/" -e "s/ /,/g"
