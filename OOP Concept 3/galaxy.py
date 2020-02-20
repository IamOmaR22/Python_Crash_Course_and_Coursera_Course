from galaxy_operation import planetofgalaxy as pg

omar=input("Enter planet name to know information :")
omar=omar.lower()
obj=pg(omar)
obj.planetname()
obj.information()
