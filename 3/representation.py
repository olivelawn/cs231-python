#!/usr/local/bin/python3

print ('According to countryeconomy.com (https://countryeconomy.com/countries/usa-states/compare/idaho/florida):')

idahopop=1754208
floridapop=21299325

print ('Idaho has a population of %d, wheras Florida has a population of %d' %(idahopop,floridapop))

senators_per_state=2
idahopoprep=idahopop/senators_per_state
floridapoprep=floridapop/senators_per_state

print ('Both states have %d senators. In Idaho, each senator represents %d people, wheras in Florida each senator represents %d people. By that math, each resident of Idaho has approximately %f times the senate representation compared to a resident of Florida.' %(senators_per_state,idahopoprep,floridapoprep,floridapoprep/idahopoprep))

#print feels like c's printf above!
