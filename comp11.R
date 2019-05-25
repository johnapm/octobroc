# Create a frequency table
d<-floor(runif(100, min=1, max=11))
a<-table(d)
t<-as.data.frame(a)
f<-t$Freq
k<-c(2:10)
p<-choose(k-1,1)*(0.5)^(2)*(0.2)^(k-2)
p
exp<-round(100*p)
exp

r= 10000;
n=200
M=matrix(0,n,r)
Xbar=rep(0,r);
for(i in 1:r){
  M[,i]=rnorm(n,3,2);
}
for(i in 1:r){
  Xbar[i]=sd(M[,i])
}
sd(Xbar)
# mean(Xbar)=3.0027, indicating the means of the means of a normal distribution is also normally distibuted. (the mean is also )
