dic = {}
dic["sandeep"]={"age":22,"phone":8610084418}
dic["ajay"]={"age":21,"phone":9564215365}
import json
s = json.dumps(dic)
with open ("jsonfile.txt","w") as f:
    f.write(s)