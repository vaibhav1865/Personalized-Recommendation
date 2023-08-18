# Generate 4 Kinds of Data using LLM's

# Each should have 1000 entries
# 1. user[uid , location, gender , Age , signup_date , last_active_date]
# 2. Products[pid , category  , price , brand  , description , Rating , Reviews ]
# 3. Transaction[tid , uid , pid , transactionAmount , transactionDate , transactionTime , transactionLocation , transactionDevice]
# 4. interaction[uid , pid , stalk_time , wishtlisted , addCart-nobuy]


# Get Data from flipkart Website using Scrapy
# 1. Product Data
# 2. User Data
# 3. Transaction Data
# 4. Interaction Data

# Generate 4 Kinds of Data using LLM's
import random
import datetime
import time
import json
import os
import sys
import csv

def generate_user_data(): # generate 1000 use,r 
    userData = [
    [1001, "Mumbai", "Male", 28, "2023-01-15", "2023-08-10"],
    [1002, "Delhi", "Female", 35, "2022-09-20", "2023-08-11"],
    [1003, "Bangalore", "Non-Binary", 22, "2023-03-10", "2023-08-12"],
    [1004, "Chennai", "Male", 30, "2022-11-05", "2023-08-10"],
    [1005, "Kolkata", "Female", 45, "2023-02-18", "2023-08-13"],
    [1006, "Hyderabad", "Male", 26, "2023-06-08", "2023-08-11"],
    [1007, "Pune", "Female", 29, "2023-04-03", "2023-08-09"],
    [1008, "Ahmedabad", "Male", 33, "2023-01-22", "2023-08-12"],
    [1009, "Jaipur", "Female", 40, "2022-12-10", "2023-08-10"],
    [1010, "Lucknow", "Male", 27, "2023-05-11", "2023-08-08"],
    [1011, "Kochi", "Female", 24, "2023-02-03", "2023-08-14"],
    [1012, "Bhopal", "Male", 31, "2023-03-19", "2023-08-09"],
    [1013, "Indore", "Female", 38, "2023-04-27", "2023-08-15"],
    [1014, "Coimbatore", "Male", 29, "2023-06-30", "2023-08-08"],
    [1015, "Vadodara", "Female", 41, "2023-07-12", "2023-08-12"],
    [1016, "Nagpur", "Male", 25, "2023-01-08", "2023-08-11"],
    [1017, "Agra", "Female", 36, "2022-10-25", "2023-08-10"],
    [1018, "Surat", "Male", 28, "2023-03-15", "2023-08-09"],
    [1019, "Varanasi", "Female", 23, "2023-07-01", "2023-08-15"],
    [1020, "Patna", "Male", 32, "2023-06-12", "2023-08-11"],
    [1021, "Mangalore", "Female", 37, "2023-02-19", "2023-08-13"],
    [1022, "Ludhiana", "Male", 29, "2023-04-09", "2023-08-12"],
    [1023, "Gurgaon", "Female", 42, "2023-03-02", "2023-08-09"],
    [1024, "Kanpur", "Male", 26, "2023-07-20", "2023-08-08"],
    [1025, "Bhubaneswar", "Female", 39, "2023-01-29", "2023-08-14"],
    [1026, "Noida", "Male", 30, "2022-09-10", "2023-08-10"],
    [1027, "Jaipur", "Female", 31, "2023-02-22", "2023-08-15"],
    [1028, "Pune", "Male", 27, "2023-05-17", "2023-08-13"],
    [1029, "Chandigarh", "Female", 34, "2023-06-28", "2023-08-11"],
    [1030, "Ahmedabad", "Male", 22, "2023-07-03", "2023-08-12"],
    [1031, "Indore", "Female", 25, "2023-03-05", "2023-08-08"],
    [1032, "Bhopal", "Male", 33, "2022-12-08", "2023-08-14"],
    [1033, "Kolkata", "Female", 26, "2023-01-18", "2023-08-10"],
    [1034, "Mumbai", "Male", 39, "2023-06-21", "2023-08-09"],
    [1035, "Delhi", "Female", 29, "2023-07-07", "2023-08-13"],
    [1036, "Bangalore", "Male", 24, "2023-03-09", "2023-08-15"],
    [1037, "Chennai", "Female", 28, "2022-10-31", "2023-08-11"],
    [1038, "Hyderabad", "Male", 35, "2023-04-15", "2023-08-14"],
    [1039, "Pune", "Female", 31, "2023-01-23", "2023-08-10"],
    [1040, "Delhi", "Male", 26, "2023-06-17", "2023-08-09"],
    [1041, "Mumbai", "Female", 27, "2023-03-12", "2023-08-15"],
    [1042, "Bangalore", "Male", 36, "2022-09-05", "2023-08-12"],
    [1043, "Chennai", "Female", 23, "2023-04-20", "2023-08-10"],
    [1044, "Kolkata", "Male", 40, "2023-07-09", "2023-08-08"],
    [1045, "Hyderabad", "Female", 25, "2023-01-28", "2023-08-11"],
    [1046, "Pune", "Male", 31, "2023-03-16", "2023-08-09"],
    [1047, "Mumbai", "Female", 26, "2023-06-05", "2023-08-12"],
    [1048, "Delhi", "Male", 37, "2022-11-12", "2023-08-10"],
    [1049, "Bangalore", "Female", 29, "2023-02-28", "2023-08-15"],
    [1050, "Chennai", "Male", 24, "2023-05-22", "2023-08-14"],
    [1051, "Kolkata", "Female", 33, "2023-06-18", "2023-08-09"],
    [1052, "Hyderabad", "Male", 28, "2023-01-02", "2023-08-13"],
    [1053, "Pune", "Female", 27, "2023-04-14", "2023-08-11"],
    [1054, "Mumbai", "Male", 30, "2023-07-26", "2023-08-10"],
    [1055, "Delhi", "Female", 29, "2023-03-01", "2023-08-15"],
    [1056, "Bangalore", "Male", 32, "2023-06-09", "2023-08-09"],
    [1057, "Chennai", "Female", 35, "2022-12-17", "2023-08-14"],
    [1058, "Kolkata", "Male", 23, "2023-01-28", "2023-08-11"],
    [1059, "Hyderabad", "Female", 40, "2023-04-30", "2023-08-12"],
    [1060, "Pune", "Male", 26, "2023-07-08", "2023-08-09"],
    [1061, "Mumbai", "Female", 29, "2023-03-11", "2023-08-15"],
    [1062, "Delhi", "Male", 30, "2023-06-19", "2023-08-14"],
    [1063, "Bangalore", "Female", 34, "2023-02-02", "2023-08-10"],
    [1064, "Chennai", "Male", 28, "2022-09-22", "2023-08-11"],
    [1065, "Kolkata", "Female", 25, "2023-04-16", "2023-08-13"],
    [1066, "Hyderabad", "Male", 31, "2023-01-05", "2023-08-12"],
    [1067, "Pune", "Female", 27, "2023-06-23", "2023-08-10"],
    [1068, "Mumbai", "Male", 36, "2023-07-17", "2023-08-09"],
    [1069, "Delhi", "Female", 22, "2023-03-09", "2023-08-15"],
    [1070, "Bangalore", "Male", 33, "2022-10-12", "2023-08-12"],
    [1071, "Chennai", "Female", 28, "2023-02-28", "2023-08-13"],
    [1072, "Kolkata", "Male", 25, "2023-06-07", "2023-08-09"],
    [1073, "Hyderabad", "Female", 30, "2023-01-22", "2023-08-10"],
    [1074, "Pune", "Male", 29, "2023-04-19", "2023-08-11"],
    [1075, "Mumbai", "Female", 36, "2023-03-18", "2023-08-15"],
    [1076, "Delhi", "Male", 23, "2023-07-14", "2023-08-10"],
    [1077, "Bangalore", "Female", 28, "2023-06-05", "2023-08-09"],
    [1078, "Chennai", "Male", 32, "2022-11-30", "2023-08-14"],
    [1079, "Kolkata", "Female", 27, "2023-02-11", "2023-08-13"],
    [1080, "Hyderabad", "Male", 24, "2023-07-09", "2023-08-15"],
    [1081, "Pune", "Female", 35, "2023-04-03", "2023-08-12"],
    [1082, "Mumbai", "Male", 29, "2023-01-29", "2023-08-11"],
    [1083, "Delhi", "Female", 30, "2023-06-10", "2023-08-13"],
    [1084, "Bangalore", "Male", 38, "2023-03-05", "2023-08-14"],
    [1085, "Chennai", "Female", 26, "2023-01-18", "2023-08-09"],
    [1086, "Kolkata", "Male", 31, "2023-04-22", "2023-08-10"],
    [1087, "Hyderabad", "Female", 24, "2023-06-03", "2023-08-08"],
    [1088, "Pune", "Male", 29, "2022-12-20", "2023-08-09"],
    [1089, "Mumbai", "Female", 33, "2023-02-15", "2023-08-14"],
    [1090, "Delhi", "Male", 25, "2023-07-28", "2023-08-11"],
    [1091, "Bangalore", "Female", 26, "2023-06-01", "2023-08-12"],
    [1092, "Chennai", "Male", 34, "2023-03-14", "2023-08-09"],
    [1093, "Kolkata", "Female", 29, "2022-09-08", "2023-08-15"],
    [1094, "Hyderabad", "Male", 27, "2023-07-06", "2023-08-10"],
    [1095, "Pune", "Female", 28, "2023-03-21", "2023-08-11"],
    [1096, "Mumbai", "Male", 33, "2023-01-16", "2023-08-13"],
    [1097, "Delhi", "Female", 30, "2023-04-25", "2023-08-14"],
    [1098, "Bangalore", "Male", 26, "2023-06-09", "2023-08-10"],
    [1099, "Chennai", "Female", 31, "2023-02-10", "2023-08-12"],
    [1100, "Kolkata", "Male", 28, "2023-07-11", "2023-08-15"]
    ]
    
    # write in user.csv
from faker import Faker
import random
import datetime

def genUserData(n):
    fake = Faker()

    # Generate user dataset
    user_dataset = []

    for _ in range(n):
        user_id = fake.uuid4()
        # user_location = fake.city()
        user_location = random.choice([
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata", "Pune", "Jaipur", "Surat",
    "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal", "Pimpri-Chinchwad", "Patna", "Vadodara", "Ghaziabad",
    "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivali", "Vasai-Virar", "Varanasi",
    "Srinagar", "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad", "Ranchi", "Howrah", "Coimbatore",
    "Jabalpur", "Gwalior", "Vijayawada", "Jodhpur", "Madurai", "Raipur", "Kota", "Chandigarh", "Guwahati", "Solapur",
    "Hubballi-Dharwad", "Bareilly", "Moradabad", "Mysore", "Gurgaon", "Aligarh", "Jalandhar", "Tiruchirappalli",
    "Bhubaneswar", "Salem", "Mira-Bhayandar", "Warangal", "Thiruvananthapuram", "Guntur", "Bhiwandi", "Saharanpur",
    "Gorakhpur", "Bikaner", "Amravati", "Noida", "Jamshedpur", "Bhilai", "Cuttack", "Firozabad", "Kochi", "Nellore",
    "Bhavnagar", "Dehradun", "Durgapur", "Asansol", "Rourkela", "Nanded", "Kolhapur", "Ajmer", "Gulbarga", "Jamnagar",
    "Ujjain", "Loni", "Siliguri", "Jhansi", "Ulhasnagar", "Nellore", "Jammu", "Sangli-Miraj & Kupwad", "Belgaum", "Mangalore",
    "Ambattur", "Tirunelveli", "Malegaon", "Gaya", "Jalgaon", "Udaipur", "Maheshtala", "Davanagere", "Kozhikode", "Akola"
])
        gender = random.choice(['Male', 'Female', 'Other'])
        age = random.randint(18, 65)
        sign_up_date = fake.date_between(start_date='-5y', end_date='today')

        user_dataset.append({
            'user_id': user_id,
            'user_location': user_location,
            'gender': gender,
            'age': age,
            'sign_up_date': sign_up_date
        })

    with open('user_fake.csv', 'w',newline='') as user_file:
        writer = csv.DictWriter(user_file , user_dataset[0].keys())
        writer.writeheader()
        writer.writerows(user_dataset)




def processCategory(categoryTree):
    # check if it convertable to json
    # categoryTree
    # print(categoryTree) 
    productCategoryTree = json.loads(categoryTree)
    if "," in productCategoryTree[0]:
        productCategoryTree = productCategoryTree[0].split(",")
    i = 0
    for cat in productCategoryTree:
        productCategoryTree[i] = cat.split(">>")[0].strip()
        i = i + 1
    return productCategoryTree
    


def process(row):
# uniq_id,crawl_timestamp,product_url,product_name,product_category_tree,pid,retail_price,discounted_price,image,is_FK_Advantage_product,description,product_rating,overall_rating,brand,product_specifications
# c2d766ca982eca8304150849735ffef9,2016-03-25 22:59:23 +0000,http://www.flipkart.com/alisha-solid-women-s-cycling-shorts/p/itmeh2ffvzetthbb?pid=SRTEH2FF9KEDEFGF,Alisha Solid Women's Cycling Shorts,"[""Clothing >> Women's Clothing >> Lingerie, Sleep & Swimwear >> Shorts >> Alisha Shorts >> Alisha Solid Women's Cycling Shorts""]",SRTEH2FF9KEDEFGF,999,379,"[""http://img5a.flixcart.com/image/short/u/4/a/altht-3p-21-alisha-38-original-imaeh2d5vm5zbtgg.jpeg"", ""http://img5a.flixcart.com/image/short/p/j/z/altght4p-26-alisha-38-original-imaeh2d5kbufss6n.jpeg"", ""http://img5a.flixcart.com/image/short/p/j/z/altght4p-26-alisha-38-original-imaeh2d5npdybzyt.jpeg"", ""http://img5a.flixcart.com/image/short/z/j/7/altght-7-alisha-38-original-imaeh2d5jsz2ghd6.jpeg""]",false,"Key Features of Alisha Solid Women's Cycling Shorts Cotton Lycra Navy, Red, Navy,Specifications of Alisha Solid Women's Cycling Shorts Shorts Details Number of Contents in Sales Package Pack of 3 Fabric Cotton Lycra Type Cycling Shorts General Details Pattern Solid Ideal For Women's Fabric Care Gentle Machine Wash in Lukewarm Water, Do Not Bleach Additional Details Style Code ALTHT_3P_21 In the Box 3 shorts",No rating available,No rating available,Alisha,"{""product_specification""=>[{""key""=>""Number of Contents in Sales Package"", ""value""=>""Pack of 3""}, {""key""=>""Fabric"", ""value""=>""Cotton Lycra""}, {""key""=>""Type"", ""value""=>""Cycling Shorts""}, {""key""=>""Pattern"", ""value""=>""Solid""}, {""key""=>""Ideal For"", ""value""=>""Women's""}, {""value""=>""Gentle Machine Wash in Lukewarm Water, Do Not Bleach""}, {""key""=>""Style Code"", ""value""=>""ALTHT_3P_21""}, {""value""=>""3 shorts""}]}"
    # print(type(row))
    # uniq_id	crawl_timestamp	product_url	product_name	product_category_tree	pid	retail_price	discounted_price	image	is_FK_Advantage_product	description	product_rating	overall_rating	brand	product_specifications

    newRow = []
    # uniqId = row[0]
    pid = row[5]
    crawlTimestamp = row[1]
    productUrl = row[2]
    productName = row[3]
    productCategoryTree = processCategory(row[4])
    retailPrice = row[6]
    discountedPrice = row[7]
    image = row[8]
    # isFKAdvantageProduct = row[9]
    description = row[10]
    productRating = row[11]
    # overallRating = row[12]
    brand = row[13]
    # productSpecifications = processSpecifications(row[14])
    # print
    newRow.append([pid , crawlTimestamp , productUrl ,brand, productName , productCategoryTree  , retailPrice , discountedPrice , image  , description , productRating   ])
    return newRow

    # print( productCategoryTree[0] , len(productCategoryTree))
    # productCategoryTree = processCategory(row[4])



def product_data(n):
# uniq_id,crawl_timestamp,product_url,product_name,product_category_tree,pid,retail_price,discounted_price,image,is_FK_Advantage_product,description,product_rating,overall_rating,brand,product_specifications
# c2d766ca982eca8304150849735ffef9,2016-03-25 22:59:23 +0000,http://www.flipkart.com/alisha-solid-women-s-cycling-shorts/p/itmeh2ffvzetthbb?pid=SRTEH2FF9KEDEFGF,Alisha Solid Women's Cycling Shorts,"[""Clothing >> Women's Clothing >> Lingerie, Sleep & Swimwear >> Shorts >> Alisha Shorts >> Alisha Solid Women's Cycling Shorts""]",SRTEH2FF9KEDEFGF,999,379,"[""http://img5a.flixcart.com/image/short/u/4/a/altht-3p-21-alisha-38-original-imaeh2d5vm5zbtgg.jpeg"", ""http://img5a.flixcart.com/image/short/p/j/z/altght4p-26-alisha-38-original-imaeh2d5kbufss6n.jpeg"", ""http://img5a.flixcart.com/image/short/p/j/z/altght4p-26-alisha-38-original-imaeh2d5npdybzyt.jpeg"", ""http://img5a.flixcart.com/image/short/z/j/7/altght-7-alisha-38-original-imaeh2d5jsz2ghd6.jpeg""]",false,"Key Features of Alisha Solid Women's Cycling Shorts Cotton Lycra Navy, Red, Navy,Specifications of Alisha Solid Women's Cycling Shorts Shorts Details Number of Contents in Sales Package Pack of 3 Fabric Cotton Lycra Type Cycling Shorts General Details Pattern Solid Ideal For Women's Fabric Care Gentle Machine Wash in Lukewarm Water, Do Not Bleach Additional Details Style Code ALTHT_3P_21 In the Box 3 shorts",No rating available,No rating available,Alisha,"{""product_specification""=>[{""key""=>""Number of Contents in Sales Package"", ""value""=>""Pack of 3""}, {""key""=>""Fabric"", ""value""=>""Cotton Lycra""}, {""key""=>""Type"", ""value""=>""Cycling Shorts""}, {""key""=>""Pattern"", ""value""=>""Solid""}, {""key""=>""Ideal For"", ""value""=>""Women's""}, {""value""=>""Gentle Machine Wash in Lukewarm Water, Do Not Bleach""}, {""key""=>""Style Code"", ""value""=>""ALTHT_3P_21""}, {""value""=>""3 shorts""}]}"

    productData = []
    i = 0
    with open('flipkart_com-ecommerce_sample.csv', 'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            newRow = process(row)
            i = i + 1
            if i == n:
                break
            productData.append(newRow)
    
    # print(productData[0])
    # print(len(productData))
    with open('product.csv', 'w',encoding='utf-8', newline='') as f:
        write = csv.writer(f)
        # write header
        # [pid , crawlTimestamp , productUrl ,brand, productName , productCategoryTree  , retailPrice , discountedPrice , image  , description , productRating 
        header = ["PID" , "Timestamp" , "ProductUrl" , "Brand" , "ProductName" , "ProductCategoryTree" , "RetailPrice" , "DiscountedPrice" , "Image" , "Description" , "ProductRating"]
        write.writerow(header)
        # i = 0
        for row in productData:
            write.writerows(row)

    

def genTransData(n):
    # for every user generate [4- 15] transactions such that each trancsaction record has
    # tid , uid , pid , transactionAmount , TimeStamp  , transactionDevice
    userData = []
    with open('user_fake.csv', 'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            userData.append(row)
    product_data = []
    with open('product.csv', 'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            product_data.append(row)
    
    transcationData = []
    for user in userData:
        uid = user[0]
        signUpdate = user[4]
        noofTrans = random.randint(4,15)
        products = random.sample(product_data , noofTrans)
        for product in products:
            pid = product[0]
            transactionAmount = product[7]
            transactionDate = random.choice([signUpdate , datetime.datetime.strptime(signUpdate, '%Y-%m-%d') + datetime.timedelta(days=random.randint(1, 365))])
            transactionDate = str(transactionDate).split(" ")[0]
            transactionTime = random.choice(["00:00:00" , "01:00:00" , "02:00:00" , "03:00:00" , "04:00:00" , "05:00:00" , "06:00:00" , "07:00:00" , "08:00:00" , "09:00:00" , "10:00:00" , "11:00:00" , "12:00:00" , "13:00:00" , "14:00:00" , "15:00:00" , "16:00:00" , "17:00:00" , "18:00:00" , "19:00:00" , "20:00:00" , "21:00:00" , "22:00:00" , "23:00:00"])
            transactionTimeStamp = str(transactionDate) + " " + transactionTime
            transactionDevice = random.choice(["Mobile" , "Laptop" , "Tablet" , "Desktop"])
            transcationData.append([uid , pid , transactionAmount , transactionTimeStamp , transactionDevice])
            
    
    with open('transaction.csv', 'w',encoding='utf-8', newline='') as f:
        write = csv.writer(f)
        # write header
        header = ["UID" , "PID" , "TransactionAmount" , "TransactionTimeStamp" , "TransactionDevice"]
        write.writerow(header)
        write.writerows(transcationData)



def genInteractionData(n):
    # for every user generate [10 - 50] interactions such that each interaction record has
    # uid , pid , stalk_time , wishtlisted , addCart-nobuy
    userData = []
    with open('user_fake.csv', 'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            userData.append(row)
    product_data = []
    with open('product.csv', 'r',encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            product_data.append(row)
    
    interactionData = []
    for user in userData:
        uid = user[0]
        noofInteractions = random.randint(10,50)
        products = random.sample(product_data , noofInteractions)
        for product in products:
            pid = product[0]
            # stalk time in days:h:m:s
            stalk_time_hrs = random.randint(0,23)
            stalk_time_mins = random.randint(0,59)
            stalk_time_secs = random.randint(0,59)
            stalk_time = str(stalk_time_hrs) + ":" + str(stalk_time_mins) + ":" + str(stalk_time_secs)
            wishtlisted = random.choice([True , False])
            addCart_nobuy = random.choice([True , False])
            interactionData.append([uid , pid , stalk_time , wishtlisted , addCart_nobuy])
    
    with open('interaction.csv', 'w',encoding='utf-8', newline='') as f:
        write = csv.writer(f)
        # write header
        header = ["UID" , "PID" , "StalkTime" , "Wishtlisted" , "AddCart-nobuy"]
        write.writerow(header)
        write.writerows(interactionData)
    




# product_data(10000)
# genUserData(5000)
# genTransData(10000)
# generate_user_data()
genInteractionData(10000)