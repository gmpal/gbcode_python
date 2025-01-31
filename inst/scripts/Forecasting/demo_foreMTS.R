rm(list=ls())
library("MTS")
library("VARshrink")
require(gbcode)
require(MTS)
library(keras)

# clothing          Cloth sales in China n=25
frequency=c(7)

data("mts-examples")
D=tenstocks[,2:11]
#D=ibmspko[,2:4]
data(Canada,package="vars")
D=Canada
print(dim(D))
visualize=TRUE
season=TRUE
execute=TRUE
methods=c("uni","VAR","VARs","dfm","dfml","multifs")
colors=c("red","green","magenta","cyan","orange","blue")
namefile="mts.Rdata"
if (execute){
  n=3
  N<-1000
  mmax<-30
  if (NROW(D)>N)
    D=D[1:N,]
  if (NCOL(D)>mmax)
    D=D[,sample(1:NCOL(D),mmax)]
  D=scale(D)
  m=NCOL(D)
  N=NROW(D)
  H=20
  SeasP<-NULL
  Ntr=N-H
  N=NROW(D)
  if (season){
    X=NULL
    bestS=NULL
    for (i in 1:m){
      S=detectSeason(D[1:Ntr,i],Ls=N,pmin=0.2)
      X=cbind(X,D[,i]-S$spattern-S$strend)
      SeasP<-cbind(SeasP,S$spattern+S$strend)
      bestS<-c(bestS,S$best)
    }
  } else {
    X=D
  }
  
  
  Xtr=X[1:Ntr,]
  Xts=D[(Ntr+1):N,]
  if (season){
    SPts=SeasP[(Ntr+1):N,]
  } 
  
  Xtr=X[1:Ntr,]
  Xtr=X[1:Ntr,]
  Xts=D[(Ntr+1):N,]
  
  Xhat1=MmultiplestepAhead(Xtr,n,H,multi=methods[1],uni=c("lazyiter"))
  cat(".")
  Xhat2=MmultiplestepAhead(Xtr,n,H,multi=methods[2])
  cat(".")
  Xhat3=MmultiplestepAhead(Xtr,n,H,multi=methods[3])
  cat(".")
  Xhat4=MmultiplestepAhead(Xtr,n,H,multi=methods[4])
  cat(".")
  Xhat5=MmultiplestepAhead(Xtr,n,H,multi=methods[5],cdfml=3,
                           dfmlmodels=c("lindirect","stat_comb"))
  cat(".")
  Xhat6=MmultiplestepAhead(Xtr,n,H,multi=methods[6],mod="rf")
  cat(".")
  save(file=namefile,list=c("methods","H","X","m","Xts","Xhat1","Xhat2",
                            "Xhat3","Xhat4","Xhat5","Xhat6"))
} else
  load(namefile)
if (season){
  Xhat1=Xhat1+SPts
  Xhat2=Xhat2+SPts
  Xhat3=Xhat3+SPts
  Xhat4=Xhat4+SPts
  Xhat5=Xhat5+SPts
  Xhat6=Xhat6+SPts
}
m=NCOL(X)
e.hat1=apply((Xts-Xhat1)^2,2,mean)
e.hat2=apply((Xts-Xhat2)^2,2,mean)
e.hat3=apply((Xts-Xhat3)^2,2,mean)
e.hat4=apply((Xts-Xhat4)^2,2,mean)
e.hat5=apply((Xts-Xhat5)^2,2,mean)
e.hat6=apply((Xts-Xhat6)^2,2,mean)

cat( methods[1],":",mean(e.hat1)," | ")
cat( methods[2],":",mean(e.hat2)," | ")
cat( methods[3],":",mean(e.hat3)," | ")
cat( methods[4],":",mean(e.hat4)," | ")
cat( methods[5],":",mean(e.hat5)," |")
cat( methods[6],":",mean(e.hat6),"\n")


if (visualize){
  for (ns in 1:m){
    e.hat1=mean((Xts[,ns]-Xhat1[,ns])^2)
    e.hat2=mean((Xts[,ns]-Xhat2[,ns])^2)
    e.hat3=mean((Xts[,ns]-Xhat3[,ns])^2)
    e.hat4=mean((Xts[,ns]-Xhat4[,ns])^2)
    e.hat5=mean((Xts[,ns]-Xhat5[,ns])^2)
    e.hat6=mean((Xts[,ns]-Xhat6[,ns])^2)
    plot(Xts[,ns],type="l",col="black",lwd=3,ylab=paste("ts.",ns),
         main=paste( methods[1],":",round(mean(e.hat1),2)," | ",
                     methods[2],":",round(mean(e.hat2),2)," | ",
                     methods[3],":",round(mean(e.hat3),2)," | ",
                     methods[4],":",round(mean(e.hat4),2)," | ",
                     methods[5],":",round(mean(e.hat5),2)," |",
                     methods[6],":",round(mean(e.hat6),2),"\n"),
                     ylim=range(Xts[,ns])+c(-1,1),
         cex.main=0.5)
    lines(Xhat1[,ns],col=colors[1])
    lines(Xhat2[,ns],col=colors[2])
    lines(Xhat3[,ns],col=colors[3])
    lines(Xhat4[,ns],col=colors[4])
    lines(Xhat5[,ns],col=colors[5])
    lines(Xhat6[,ns],col=colors[6])
    legend("topleft",
           c("real",methods),
           col=c("black",colors),lty=1,cex=0.3)
    browser()
  }
}


