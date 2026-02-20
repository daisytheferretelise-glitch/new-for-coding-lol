print("Bob needed too find pepole to work at his hotel, come join him to find the right pepole too hire")

worker_data = {
    "id1":{"name":"sigma_ohio_rizzler", "class":"v","subject-intergration":"waiter"},
    "id2":{"name":"Kate", "class":"v","subject-intergration":"waiter"},
"id3":{"name":"Slay_Queen", "class":"v","subject-intergration":"waiter"},
"id4":{"name":"Rizz", "class":"v","subject-intergration":"waiter"},
"id5":{"name":"sigma_ohio_rizzler", "class":"v","subject-intergration":"waiter"},
"id6":{"name":"ohio", "class":"v","subject-intergration":"waiter"},
}
result = {}
seen = set()

for worker_id, detail in worker_data.items():
    unique_key=(detail["name"],detail["class"], detail["subject-intergration"])
    if unique_key not in seen:
        seen.add(unique_key)
        result[worker_id]= detail

for k,v in result.items():
    print(k,":",v)