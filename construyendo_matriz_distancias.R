# Matriz de distancias
source("functions/geo.R")
db<-read.csv("datasets/aero.csv")
#require("dplyr")
#require("magrittr")
lat_lon<-na.omit(data.frame("name"=db$NOMBRE, "lat0"=as.numeric(as.character(db$LATITUD..)), "lat1"=as.numeric(as.character(db$LATITUD...1)), "lat2"=as.numeric(as.character(db$LATITUD...)), "lon0"=as.numeric(as.character(db$LONGITUD..)), "lon1"=as.numeric(as.character(db$LONGITUD...1)), "lon2"=as.numeric(as.character(db$LONGITUD...))))
indices<-c()
for(i in 1:nrow(lat_lon)){
	print(i)
	a<-grep(as.character(lat_lon[i,]),pattern="NO APLICA|PENDIENTE|NO DISPONIBLE")
	if(length(a)==0) indices[i]<-i 
}
lat_lon<-lat_lon[indices,]
lat_lon$latitud<-lat_lon$lat0+lat_lon$lat1/60+lat_lon$lat2/3600
lat_lon$longitud<-lat_lon$lon0+lat_lon$lon1/60+lat_lon$lon2/3600

lt_ln<-data.frame("name"=lat_lon$name, "lat"=lat_lon$latitud, "lon"=lat_lon$longitud)
set.seed(3141617)
dist_prueba<-round(GeoDistanceInMetresMatrix(lt_ln[sample(1:nrow(lt_ln),50),]) / 1000)
write.csv(dist_prueba, "datasets/dist_prueba.csv",row.names=F)

