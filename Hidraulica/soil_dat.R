# library to read netcdf files
library(ncdf4)
#library to plot maps with legend easily
library(fields)

# set wd to HadGEM2ES_Soil_Ancil.nc location
#setwd("C://Users//CBE//OneDrive - University of Exeter//soildata_hadgem")
# open netcdf
anci <- nc_open("HadGEM2ES_Soil_Ancil.nc")

# coordinates from where you want the data, example some site in amazon
lat <- -1.74
lon <- -51.46

# check variable names, units and file structure
# anci
# field342 - SATURATED SOIL WATER SUCTION 
# field332 - VOL SMC AT SATURATION AFTER TIMESTEP
# field1381 - CLAPP-HORNBERGER B COEFFICIENT

# The longitude in the hadgem file is in a weird format
# The greenwich meridian is 0, and then it increases to 360 to the east, see
b <- ncvar_get(anci, varid = "field1381")
image.plot(anci$dim$longitude$vals,
           anci$dim$latitude$vals,
           b)

# Function to convert the longitute from -180:180 to 0:360
conv_lon<-function(longitude) {
  x <- c(seq(181,360,by=0.5),seq(0,180,by=0.5))
  y <- seq(-180,180,by=0.5)
  return(x[which.min(abs(y - lon))])
}
lon360<-conv_lon(lon)

# extract the data from the nearest gridcell for your example site 
b <- ncvar_get(anci, varid = "field1381",count = c(1,1),
               start= c(which.min(abs(anci$dim$longitude$vals - lon360)), 
                        which.min(abs(anci$dim$latitude$vals - lat))))  
b<-c(b)

Psi_sat <- ncvar_get(anci, varid = "field342",count = c(1,1),
                     start= c(which.min(abs(anci$dim$longitude$vals - lon360)), 
                              which.min(abs(anci$dim$latitude$vals - lat))))  
Psi_sat_cm<-c(Psi_sat*100)# transform m to cm

smc_sat <- ncvar_get(anci, varid = "field332",count = c(1,1),
                     start= c(which.min(abs(anci$dim$longitude$vals - lon360)), 
                              which.min(abs(anci$dim$latitude$vals - lat))))  
smc_sat<-c(smc_sat)

# Example using Clapp & Hornberger (1978) equations to convert smc to Psi_soil
smc<-seq(0.1*smc_sat,smc_sat,length.out = 1000)# example smc vector
Psi_soil_cm<-Psi_sat_cm*(smc/smc_sat)^(-b)
Psi_soil<--Psi_soil_cm*98.04*1e-6# convert Psi_soil from cm to MPa
plot(Psi_soil~smc)
