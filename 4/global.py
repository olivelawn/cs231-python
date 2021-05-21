#!/usr/local/bin/python3

print ('According to wikipedia.org (https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations):')

chinapop=1433783686
uspop=329064917
russiapop=145872256
ukpop=67530172
francepop=65129728
permanentpop=chinapop+uspop+russiapop+ukpop+francepop

globalpop=7713468100

percent_perm_to_global=100 * float(permanentpop)/float(globalpop)

print ('The permanent members of the United Nations security council are China, the US, Russia, United Kingdom, and France. They have populations of %d, %d, %d, %d, %d, respectively (in order of greatest to leastest), and total %d. The total world population is %d. Thus, %f%% of the global population is represented by the permanent members of the UN security council.' %(chinapop,uspop,russiapop,ukpop,francepop,permanentpop,globalpop,percent_perm_to_global))



#print feels like c's printf above!
