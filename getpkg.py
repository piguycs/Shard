#!/usr/bin/python3

def get_version(name):
  dimensions = "TBD"
  dimensions.read("/usr/spark/dimensions/dimensions.config")
  for source in dimensions.datajson['sources']:
    #print(fail+source['name']+reset,"has:")
    for pack in source['packs']:
      if pack['name'].lower() == name.lower():
        return pack['version']
      else:
        #print(pack['name'],name,"no match")
        continue
  return False
