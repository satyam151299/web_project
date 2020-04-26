def data_base(status,name,date_essues,dlnumber,class_of_vahical,date_of_expire):
    d={"Driving License Number":dlnumber.text,"Date of Birth":dob}
    if status.text[16:]=="ACTIVE":
        d["holdername"]=name.text
        d["date_essues"]=date_essues.text
        d["class_of_vehicle"]=class_of_vahical.text
        d["date_of_expir"]=date_of_expire.text[3:]
    else:
        d["Status":None]
    return d
def data_json():
    import json                        
    with open("final.json","w")as file:
        json.dump(d,file)
data_json()        
        
