##################################################
### Function for converting date into a number ###
##################################################

fechaNumero<-function(fechas){
	fechasNumeros<-unlist(lapply(fechas, function(x) as.POSIXct(as.character(x), format="%d/%m/%Y  %H:%M:%S")))
return(fechasNumeros)
}
