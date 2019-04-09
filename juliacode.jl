# this is just for learning Purpose

import Pkg
Pkg.add("RDatasets")
Pkg.add("Statistics")
Pkg.add("Gadfly")

using RDatasets
using Statistics
using Gadfly

RDatasets.datasets()
iris = dataset("datasets", "iris") 
names(iris)						        #retrive name of the columns
size(iris) 							 # size of the dataset
head(iris)							 # top 10 rows of table
tail(iris, 10) 							 #last 10 rows of table
by(iris, :Species, nrow) 					#row count grouped by Species
describe(iris)   
describe(iris, stats=:all)

mean(iris[:SepalLength]) 
median(iris[:SepalLength])
std(iris[:SepalLength])
irisarr = convert(Array, iris[:,:])  				# convert the whole DataFrame to a matrix:

plot(iris, x=:SepalLength, y=:PetalLength, color=:Species)
plot(iris, x=:Species, y=:PetalLength, Geom.boxplot)
plot(iris, x=:PetalLength, color=:Species, Geom.histogram)
plot(iris, x=:PetalWidth, color=:Species, Geom.histogram)
plot(iris, x=:PetalWidth, y=:PetalLength, color=:Species)


test_data = iris[rand(150) .<= 0.1, [:PetalLength, :PetalWidth, :Species]]  
add CSV 
using CSV 
CSV.write("test_data.csv", test_data) 
