#!/bin/sh
#
#simple script to get: avg, medain, min, and max
#
sort -n | \
awk 'BEGIN{c=0;sum=0;}
        /^[^#]/{a[c++]=$1;sum+=$1;}
    END{avg=sum/c;
        if((c%2)==1){
            median=a[int(c/2)];
        }
        else{
            median=(a[c/2]+a[c/2-1])/2;
        }
    print avg,"\t",median,"\t",a[0],"\t",a[c-1]}'
