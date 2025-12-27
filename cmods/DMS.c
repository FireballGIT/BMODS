#include <math.h>
#include <stdio.h>

long fact(int n){
    if(n<0) return -1;
    long r=1;
    for(int i=2;i<=n;i++) r*=i;
    return r;
}

double mean(double* d,int n){
    if(n==0) return 0;
    double s=0;
    for(int i=0;i<n;i++) s+=d[i];
    return s/n;
}

double median(double* d,int n){
    if(n==0) return 0;
    for(int i=0;i<n-1;i++)
      for(int j=i+1;j<n;j++)
        if(d[i]>d[j]){double t=d[i];d[i]=d[j];d[j]=t;}
    return n%2?d[n/2]:(d[n/2-1]+d[n/2])/2;
}

double stddev(double* d,int n){
    if(n<2) return 0;
    double avg=mean(d,n),v=0;
    for(int i=0;i<n;i++) v+=(d[i]-avg)*(d[i]-avg);
    return sqrt(v/(n-1));
}
