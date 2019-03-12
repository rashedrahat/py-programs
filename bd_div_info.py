# a program that will find how many total number of district, upazila and union are in each division of Bangladesh.

bd_div_info = {}
bd_div_info["Barishal"] = {"district": 6, "upazila": 39, "union": 333}
bd_div_info["Ctg"] = {"district": 11, "upazila": 97, "union": 336}
bd_div_info["Dhaka"] = {"district": 13, "upazila": 93, "union": 1833}
bd_div_info["Khulna"] = {"district": 10, "upazila": 59, "union": 270}
bd_div_info["Mymensingh"] = {"district": 4, "upazila": 34, "union": 350}
bd_div_info["Rajshahi"] = {"district": 8, "upazila": 70, "union": 558}
bd_div_info["Rangpur"] = {"district": 8, "upazila": 58, "union": 536}
bd_div_info["Sylhet"] = {"district": 4, "upazila": 38, "union": 334}

district = 0
upazila = 0
union = 0

for division in bd_div_info.keys():
	district = district + bd_div_info[division]["district"]
	upazila = upazila + bd_div_info[division]["upazila"]
	union = union + bd_div_info[division]["union"]

print("Total district in BD: ", district)
print("Total upazila in BD: ", upazila)
print("Total union in BD: ", union)