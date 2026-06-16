from flask import Flask, jsonify, request
import mysql.connector
import json
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# 建立MySQL連線
conn = mysql.connector.connect(
    host='140.127.208.120',           
    user='root',                   
    password='nukcsie114', 
)
cursor = conn.cursor()



# 建立MySQL連線
conn = mysql.connector.connect(
    host='140.127.208.120',           
    user='root',                   
    password='nukcsie114', 
    database='final_project'
)
cursor = conn.cursor()
CORS(app)

@app.route('/')
def hello():
    cursor = conn.cursor()

    # 使用資料庫
    cursor.execute("USE final_project;")

    # 查詢資料
    cursor.execute("SELECT * FROM account;")

    # 將查詢資料傳至Python
    result = cursor.fetchall()
    # 關閉資料庫連線
    #conn.close()

    return jsonify(result)

@app.route('/api/get_all_advertisement', methods=['GET'])
def get_all_advertisement():
    try:
        cursor.execute("USE final_project;")
        sql = f"SELECT ad_id,title FROM advertisement;"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for result in result:
                info = {
                    'ad_id': result[0],
                    'title': result[1],
                }
                infos.append(info)
            return jsonify({'ad_info': infos})
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)

@app.route('/api/delete_comment/<input_string>', methods=['GET'])
def delete_comment(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"DELETE FROM comment WHERE comment_id = '{input_string}';"
        cursor.execute(sql)
        result = cursor.fetchall()
        result = [result[i][0] for i in range(len(result))]
        
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

@app.route('/api/update_post/<input_string>', methods=['GET'])
def update_post(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")

        sql = f"UPDATE post SET post_detail='{input_string[1]}' where post_id ='{input_string[0]}';"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

@app.route('/api/delete_post/<input_string>', methods=['GET'])
def delete_post(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"SELECT comment_id FROM comment WHERE post_id = '{input_string}';"
        cursor.execute(sql)
        result = cursor.fetchall()
        result = [result[i][0] for i in range(len(result))]
        #print(result)
        for i in result:
            sql = f"DELETE FROM comment WHERE comment_id = '{i}';"
            cursor.execute(sql)
            conn.commit()  # Commit the changes to the database
        sql = f"DELETE FROM post WHERE post_id = '{input_string}';"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

@app.route('/api/update_comment/<input_string>', methods=['GET'])
def update_comment(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")

        sql = f"UPDATE comment SET comment_detail='{input_string[1]}' where comment_id ='{input_string[0]}';"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

@app.route('/api/advertisement/update_advertisement/<input_string>', methods=['GET'])
def update_advertisement(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        sql = f"UPDATE advertisement SET title='{input_string[1]}', ad_description='{input_string[2]}' WHERE ad_id ='{input_string[0]}';"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database

        sql = f"SELECT rent_id FROM advertisement WHERE ad_id ='{input_string[0]}';"
        cursor.execute(sql)
        result = cursor.fetchall()
        rent_id = result[0][0]

        sql = f"UPDATE rent_information SET rent='{input_string[3]}', address='{input_string[4]}' WHERE rent_id ='{rent_id}';"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

@app.route('/api/delete_advertisement/<input_string>', methods=['GET'])
def delete_advertisement(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"DELETE FROM advertisement WHERE ad_id = '{input_string}';"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)
    
#用法: 回傳所有的comment
@app.route('/api/administrator/get_all_comment', methods=['GET'])
def get_all_comment():
    try:
        cursor.execute("USE final_project;")
        sql = f'select * from comment;'
        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for result in result:
                info = {
                    'comment_id': result[0],
                    'post_id': result[2],
                    'comment_detail': result[3]
                }
                infos.append(info)
            return jsonify({'post_info': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)
    
# #登陸驗證api，用法: 傳入管理員id和name,email,phone ，修改管理員的個人資訊(name,email,phone)，回傳修改結果(success,error)
# @app.route('/api/administrator/get_all_ad', methods=['GET'])
# def administrator_modify_information(input_string):
#     try:
#         input_string = input_string.split(',')
#         cursor.execute("USE final_project;")
#         sql = f"UPDATE administrator SET name='{input_string[1]}', email='{input_string[2]}',phone='{input_string[3]}' WHERE id ='{input_string[0]}';"
#         #sql = f"SELECT * FROM  administrator where id='{input_string}';"
#         #print(sql)
#         cursor.execute(sql)
#         conn.commit()  # Commit the changes to the database
#         if cursor.rowcount > 0:
#             result = "success"
#         else:
#             result = "error"
#         return jsonify(result)

#     except:
#         result = "error"
#         return jsonify(result)

#用法: 傳入管理員id和name,email,phone ，修改管理員的個人資訊(name,email,phone)，回傳修改結果(success,error)
@app.route('/api/teacher/teacher_modify_information/<input_string>', methods=['GET'])
def teacher_modify_information(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        sql = f"UPDATE teacher SET name='{input_string[1]}', email='{input_string[2]}',level='{input_string[3]}',phone='{input_string[4]}',office_address='{input_string[5]}',office_phone='{input_string[6]}' WHERE id ='{input_string[0]}';"
        #sql = f"SELECT * FROM  administrator where id='{input_string}';"
        #print(sql)
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)
    
#用法: 傳入管理員id和name,email,phone ，修改管理員的個人資訊(name,email,phone)，回傳修改結果(success,error)
@app.route('/api/student/student_modify_information/<input_string>', methods=['GET'])
def student_modify_information(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        sql = f"UPDATE student SET name='{input_string[1]}', email='{input_string[2]}',grade='{input_string[3]}',phone='{input_string[4]}',home_address='{input_string[5]}',home_phone='{input_string[6]}',home_contact='{input_string[7]}' WHERE id ='{input_string[0]}';"
        #sql = f"SELECT * FROM  administrator where id='{input_string}';"
        #print(sql)
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)

       
#用法: 傳入管理員id和name,email,phone ，修改管理員的個人資訊(name,email,phone)，回傳修改結果(success,error)
@app.route('/api/administrator/administrator_modify_information/<input_string>', methods=['GET'])
def administrator_modify_information(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        sql = f"UPDATE administrator SET name='{input_string[1]}', email='{input_string[2]}',phone='{input_string[3]}' WHERE id ='{input_string[0]}';"
        #sql = f"SELECT * FROM  administrator where id='{input_string}';"
        #print(sql)
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)

#用法: 回傳所有的post
@app.route('/api/post/get_all_post', methods=['GET'])
def get_all_post():
    try:
        cursor.execute("USE final_project;")
        sql = f'select post_id from post;'
        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for result in result:
                info = {
                    'post_id': result[0],
                    # 'id': result[1],
                    # 'post_detail': result[2],
                    # 'picture': result[3],
                }
                infos.append(info)
            return jsonify({'post_info': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)


#登陸驗證api，用法: 給Post_id回傳所有的該Post的留言
@app.route('/api/comment/get_all_samepost_comment/<input_string>', methods=['GET'])
def get_all_samepost_comment(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f'select * from comment where post_id="{input_string}";'
        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for result in result:
                info = {
                    'comment_id': result[0],
                    'id': result[1],
                    'post_id': result[2],
                    'comment_detail': result[3],
                    'picture': result[4],
                }
                infos.append(info)
            return jsonify({'comment_info': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)
    
    
#用法: 傳入角色類別(0是管理員、1是房東、2是老師、3是學生)，回傳所有id的id和名字 
@app.route('/api/administrator/get_idandnames/<input_string>', methods=['GET'])
def get_idandnames(input_string):
    try:
        input_string = int(input_string)
        cursor.execute("USE final_project;")
        if(input_string == 0):         
            sql = f'''SELECT account.id,administrator.name FROM account,administrator WHERE account.id=administrator.id;'''
        elif(input_string == 1):
            sql = f'''SELECT account.id,landlord.name FROM account,landlord WHERE account.id=landlord.id;'''
        elif(input_string == 2):
            sql = f'''SELECT account.id,teacher.name FROM account,teacher WHERE account.id=teacher.id;'''
        elif(input_string == 3):
            sql = f'''SELECT account.id,student.name FROM account,student WHERE account.id=student.id;'''
        #print(sql)
        cursor.execute(sql)
        results = cursor.fetchall()
        if results == []:
            results = "error"
            jsonify(results)
        elif results:
            infos = []
            for result in results:
                info = {
                    'id': result[0],
                    'name': result[1],
                }
                infos.append(info)
            return jsonify({'all_idandnames_info': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)
    
#登陸驗證api，用法: 傳入老師id ，回傳老師的個人資訊
@app.route('/api/teacher/teacher_information/<input_string>', methods=['GET'])
def teacher_information(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"SELECT * FROM  teacher where id='{input_string}';"
        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            return jsonify(result)
        elif result:
            infos = []
            for result in result:
                info = {
                    'id': result[0],
                    'name': result[2],
                    'email': result[3],
                    'gender': result[4],
                    'level': result[5],
                    'phone': result[6],
                    'office_address': result[7],
                    'office_phone': result[8],
                }
                infos.append(info)
            return jsonify({'teacher_information': infos})
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)

#登陸驗證api，用法: 傳入老師id ，回傳老師的個人資訊
@app.route('/api/student/student_information/<input_string>', methods=['GET'])
def student_information(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"SELECT * FROM  student where id='{input_string}';"
        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            return jsonify(result)
        elif result:
            infos = []
            for result in result:
                info = {
                    'id': result[0],
                    'name': result[2],
                    'email': result[3],
                    'grade': result[4],
                    'gender': result[5],
                    'phone': result[7],
                    'home_address': result[8],
                    'home_phone': result[9],
                    'home_contact': result[10],
                }
                infos.append(info)
            return jsonify({'student_information': infos})
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)    
       
#登陸驗證api，用法: 傳入管理員id ，回傳管理員的個人資訊
@app.route('/api/administrator/administrator_information/<input_string>', methods=['GET'])
def administrator_information(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"SELECT * FROM  administrator where id='{input_string}';"
        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            return jsonify(result)
        elif result:
            infos = []
            for result in result:
                info = {
                    'id': result[0],
                    'name': result[2],
                    'email': result[3],
                    'gender': result[4],
                    'phone': result[5],
                }
                infos.append(info)
            return jsonify({'administrator_information': infos})
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)

@app.route('/api/reported_comment', methods=['GET'])
def reported_comment():
    try:
        cursor.execute("USE final_project;")
        sql = f"""
        SELECT * FROM comment WHERE report = '1';
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for resultt in result:
                info = {
                    'comment_id': resultt[0],
                    'post_id': resultt[2],
                    'comment_detail': resultt[3]
                }
                infos.append(info)
            return jsonify({'comment_report': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)
    
@app.route('/api/reported_post', methods=['GET'])
def reported_post():
    try:
        cursor.execute("USE final_project;")
        sql = f"""
        SELECT post_id FROM post WHERE report = '1';
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for resultt in result:
                info = {
                    'post_id': resultt[0]
                }
                infos.append(info)
            return jsonify({'post_report': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

@app.route('/api/reported_advertisement', methods=['GET'])
def reported_advertisement():
    try:
        cursor.execute("USE final_project;")
        sql = f"""
        SELECT ad_id,ad_description FROM advertisement WHERE report = '1';
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for resultt in result:
                info = {
                    'repair_id': resultt[0],
                    'repair_descrition': resultt[1]
                }
                infos.append(info)
            return jsonify({'ad_report': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)


############################################################################################################

#用法: 傳入房東id ，回傳房東的個人資訊
@app.route('/api/landlord/add_new_contract/<input_string>', methods=['GET'])
def add_new_contract(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        sql = f"SELECT contract_id FROM contract;"
        cursor.execute(sql)
        result = cursor.fetchall()
        no_in = "C001"
        result = [result[i][0] for i in range(len(result))]
        for i in range(1,1000):
            x = "C"
            x+=str(i).zfill(3)
            if x not in result:
                no_in = x
                break
        #print(no_in)
        sql = f"INSERT INTO contract VALUES ('{no_in}','{input_string[0]}','{input_string[1]}', '{input_string[2]}','{input_string[3]}','{input_string[4]}');"
        print(sql)
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)
    
@app.route('/api/landlord/update_contract/<input_string>', methods=['GET'])
def update_contract(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        sql = f"""
        UPDATE contract SET contract_time='{input_string[1]}',deposit='{input_string[2]}',address='{input_string[3]}',rent='{input_string[4]}' WHERE contract_id = '{input_string[0]}';
        """
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

@app.route('/api/landlord/delete_contract/<input_string>', methods=['GET'])
def delete_contract(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"""
        DELETE FROM contract WHERE contract_id = '{input_string}';
        """
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)        
    
#用法: 傳入房東id ，回傳房東的個人資訊
@app.route('/api/landlord/landlord_information/<input_string>', methods=['GET'])
def landlord_information(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"SELECT * FROM landlord where id='{input_string}';"
        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for result in result:
                info = {
                    'id': result[0],
                    'name': result[2],
                    'email': result[3],
                    'gender': result[4],
                    'phone': result[5],
                }
                infos.append(info)
            return jsonify({'landlord_information': infos})
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)


#用法: 傳入房東id ，回傳合約資訊
@app.route('/api/landlord/renter_information/<input_string>', methods=['GET'])
def renter_information(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"""SELECT student.name,student.id,student.grade
        ,teacher.name,student.gender,student.email,student.phone,student.home_address
        ,student.home_phone,student.home_contact,contract.contract_id,landlord.name,
        contract.contract_time,contract.deposit,contract.address,contract.rent FROM student INNER JOIN contract ON student.id = contract.student_id INNER JOIN teacher ON teacher.id = student.teacher_id INNER JOIN landlord ON landlord.landlord_id = contract.landlord_id WHERE contract.landlord_id = '{input_string}';
        """
        #print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for resultt in result:
                info = {
                    'name': resultt[0],
                    'studentId': resultt[1],
                    'grade': resultt[2],
                    'advisor': resultt[3],
                    'gender': resultt[4],
                    'email': resultt[5],
                    'phone': resultt[6],
                    'homeAddress': resultt[7],
                    'homePhone': resultt[8],
                    'homeContact': resultt[9],
                    'contract_id': resultt[10],
                    'Landlord': resultt[11],
                    'RentTime': resultt[12],
                    'deposit': resultt[13],
                    'address': resultt[14],
                    'Rent': resultt[15],
                }
                infos.append(info)
            return jsonify({'renter_information': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

#用法: 輸入repair_id,response的值 變更該response的資訊
@app.route('/api/make_report_0/<input_string>', methods=['GET'])
def make_report_0(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        if input_string[1] == 'comment':
            sql = f"UPDATE comment SET report='0' WHERE comment_id ='{input_string[0]}';"
        elif input_string[1] == 'post':
            sql = f"UPDATE post SET report='0' WHERE post_id ='{input_string[0]}';"
        elif input_string[1] == 'advertisement':
            sql = f"UPDATE advertisement SET report='0' WHERE ad_id ='{input_string[0]}';"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)
    
#用法: 輸入repair_id,response的值 變更該response的資訊
@app.route('/api/landlord/response_to_repair/<input_string>', methods=['GET'])
def response_to_repair(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        sql = f"UPDATE repair SET repair_response='1' WHERE repair_id ='{input_string[0]}';"
        #sql = f"SELECT * FROM  administrator where id='{input_string}';"
        #print(sql)
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)

#用法: 傳入房東id ，回傳合約資訊
@app.route('/api/landlord/return_repair_id/<input_string>', methods=['GET'])
def return_repair_id(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"SELECT repair_id,student.name,repair_detail FROM repair INNER JOIN student ON repair.student_id = student.student_id WHERE landlord_id = '{input_string}';"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for resultt in result:
                info = {
                    'id': resultt[0],
                    'reporter': resultt[1],
                    'description': resultt[2]
                }
                infos.append(info)
            return jsonify({'people_call_for_repair': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

#用法: 傳入房東id ，回傳合約資訊
@app.route('/api/landlord/return_response_equal_0/<input_string>', methods=['GET'])
def return_response_equal_0(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"""
        SELECT repair.repair_id,student.name,repair.repair_detail FROM repair INNER JOIN student ON repair.student_id = student.id 
        WHERE repair.landlord_id = '{input_string}' AND repair.repair_response = '0';
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for resultt in result:
                info = {
                    'id': resultt[0],
                    'reporter': resultt[1],
                    'description': resultt[2]
                }
                infos.append(info)
            return jsonify({'repair_response_0': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

#用法: 傳入房東id ，回傳合約資訊
@app.route('/api/landlord/return_response_equal_1/<input_string>', methods=['GET'])
def return_response_equal_1(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"""
        SELECT repair.repair_id,student.name,repair.repair_detail FROM repair INNER JOIN student ON repair.student_id = student.id 
        WHERE repair.landlord_id = '{input_string}' AND repair.repair_response = '1';
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        elif result:
            infos = []
            for resultt in result:
                info = {
                    'id': resultt[0],
                    'reporter': resultt[1],
                    'description': resultt[2]
                }
                infos.append(info)
            return jsonify({'repair_response_1': infos})
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)

#用法: 傳入房東id ，回傳合約資訊
@app.route('/api/landlord/delete_repair/<input_string>', methods=['GET'])
def delete_repair(input_string):
    try:
        cursor.execute("USE final_project;")
        sql = f"""
        DELETE FROM repair WHERE repair_id = '{input_string}';
        """
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)
    
    

#登陸驗證api，用法: 傳入要修改的房東id和name,email,phone ，修改房東的個人資訊(name,email,phone)，回傳修改結果(success,error)
@app.route('/api/landlord/landlord_modify_information/<input_string>', methods=['GET'])
def landlord_modify_information(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        sql = f"UPDATE landlord SET name='{input_string[1]}', email='{input_string[2]}',phone='{input_string[3]}' WHERE id ='{input_string[0]}';"
        #sql = f"SELECT * FROM  administrator where id='{input_string}';"
        #print(sql)
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)
    
####################################################################################################################

#登陸驗證api，用法: 傳入帳號,密碼 ，回傳帳號類型
@app.route('/api/all/check_login/<input_string>', methods=['GET'])# 用法是運行後在網址後面加上/data/要查詢的資料表名稱，例如127.0.0.1:5000/data/account
def checklog(input_string):
    try:
        input_string = input_string.split(',')
        # 使用資料庫
        cursor.execute("USE final_project;")
        sql = f"SELECT usertype FROM account where id='{input_string[0]}' and password='{input_string[1]}';"
        # 查詢資料
        #print(sql)
        cursor.execute(sql)

        # 將查詢資料傳至Python
        result = cursor.fetchall()
        if result == []:
            result = "error"
            jsonify(result)
        return jsonify(result)

    except:
        result = "error"
        return jsonify(result)

@app.route('/test_function/<input_string>', methods=['GET'])# 用法是運行後在網址後面加上/data/要查詢的資料表名稱，例如127.0.0.1:5000/data/account
def queryDataMessageByName(input_string): 
    print("type(name) : ", type(input_string))
    #return 'String => {}'.format(name)
    print("input",input_string)
    input_string = input_string.split(',')

    # 使用資料庫
    cursor.execute("USE final_project;")

    # 查詢資料
    cursor.execute(f"SELECT * FROM {input_string[0]};")

    # 將查詢資料傳至Python
    result = cursor.fetchall()

    # 印出查詢結果
    for x in result:
        print(x)

    # 關閉資料庫連線
    #conn.close()
    return jsonify(result)


@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        cursor.execute("SELECT * FROM final_project.account WHERE id = %s AND password = %s", (username, password))
        result = cursor.fetchall()
        response_object = {'status': 'success'}
        if len(result) == 0:
            response_object['status'] = 'fail'
            return jsonify(response_object)
        else:
            response_object['status'] = 'success'
            for row in result:
                response_object['data'] = row[2]
            return jsonify(response_object)
    except Exception as e:
        print(e)
        return jsonify({'status': 'fail'})
    
@app.route('/api/advertisement', methods=['GET','POST'])
def advertisement():
    try:
        cursor.execute("SELECT advertisement.title,advertisement.ad_description,rent_information.picture,rent_information.rent,rent_information.address,landlord.id,landlord.phone,advertisement.ad_id FROM advertisement INNER JOIN rent_information ON advertisement.rent_id=rent_information.rent_id INNER JOIN landlord ON rent_information.landlord_id = landlord.landlord_id")
        result = cursor.fetchall()
        response_object = {'status': 'success'}
        response_object['data'] = []
        for row in result:
            response_object['data'].append({'title': row[0], 'description': row[1], 'image': row[2], 'price': row[3],'address': row[4],'landlord': row[5],'phone':row[6],'ad_id':row[7]})
        return jsonify(response_object)
    except Exception as e:
        print(e)
        return jsonify({'status': 'fail'})

    
@app.route('/api/post', methods=['GET','POST'])
def getPost():
    try:
        cursor.execute("SELECT a.post_id AS post_id ,a.id AS poster_id,a.post_detail AS content,a.picture AS post_pic, a.report AS report, COALESCE(ad.name, l.name, s.name, t.name) AS poster_name, COALESCE(ad.personal_pic, l.personal_pic, s.personal_pic, t.personal_pic) AS poster_pic FROM post a LEFT JOIN administrator ad ON a.id = ad.id LEFT JOIN landlord l ON a.id = l.id LEFT JOIN student s ON a.id = s.id LEFT JOIN teacher t ON a.id = t.id;")
        result = cursor.fetchall()
        response_object = {'status': 'success'}
        response_object['data'] = []
        for row in result:
            response_object['data'].append({"avatar": row[6], "image": row[3], "content": row[2], "username": row[5], "post_id": row[0],"avatar_id":row[1]})
        response_object['status'] = 'success'
        print(response_object)
        return jsonify(response_object)
    except Exception as e:
        print(e)
        return jsonify({'status': 'fail'})
    
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        print(data)
        userid = data["userid"]
        username = data["username"]
        password = data["password"]
        role = data["role"]
        gender = data["gender"]
        email = data["email"]
        phone = data["phone"]

        if(role=='landlord'):
            role='房東'
        elif(role=='student'):
            role='學生'
        elif(role=='teacher'):
            role='老師'

        #for r in role:
        print(role)
        if role == '房東':
                if gender =='male':
                    gender='1'
                else:
                    gender='0'
                cursor.execute("INSERT INTO final_project.account (id,password,usertype) VALUES (%s,%s,%s)", (userid, password, role))
                cursor.execute("INSERT INTO final_project.landlord (id,landlord_id,name,email,gender,phone) VALUES (%s,%s,%s,%s,%s,%s)", (userid, userid, username, email, gender, phone))
                conn.commit()
        if role == '學生':
                if gender =='male':
                    gender=1
                else:
                    gender=0
                # 檢查資料庫中是否已經有 password
                cursor.execute("SELECT password FROM final_project.account WHERE id = %s", (userid,))
                existing_password = cursor.fetchone()
                
                if existing_password and existing_password[0]:  # 如果 password 不為空
                    return jsonify({'status': 'fail'})
                
                cursor.execute("UPDATE final_project.account SET password = %s, usertype = %s WHERE id = %s", (password, role, userid))
                cursor.execute("UPDATE final_project.student SET name = %s, email = %s, gender = %s, phone = %s, home_address = %s, home_phone = %s, home_contact = %s WHERE id = %s", 
                               (username, email, gender, phone, '-', '-', '-', userid))
                conn.commit()
        if role == '老師':
                if gender =='male':
                    gender=1
                else:
                    gender=0
                cursor.execute("SELECT password FROM final_project.account WHERE id = %s", (userid,))
                existing_password = cursor.fetchone()
                
                if existing_password and existing_password[0]:  # 如果 password 不為空
                    return jsonify({'status': 'fail'})
                
                cursor.execute("UPDATE final_project.account SET password = %s, usertype = %s WHERE id = %s", (password, role, userid))
                cursor.execute("UPDATE final_project.teacher SET name = %s, email = %s, gender = %s, phone = %s, office_address = %s, office_phone = %s WHERE id = %s", 
                               (username, email, gender, phone, '-', '-', userid))   
        
        conn.commit()
        response_object = {'status': 'success'}
        return jsonify(response_object)
    except Exception as e:
        print(e)
        return jsonify({'status': 'fail'})

#--------------------------------------------------------------TCS----------------------------------------------------------------
@app.route('/TCS_info/<string:id>', methods=['GET', 'POST'])
def get_and_update_info_tcs(id):
    try:
        if request.method == 'GET':
            # 查詢資料
            cursor.execute(f"SELECT * FROM teacher WHERE id = '{id}'")
            result = cursor.fetchone()

            if result:
                info = {
                    'id': result[0],
                    'name': result[2],
                    'position': result[5],
                    'contactNumber': result[6],
                    'email': result[3],
                    'officeAddress': result[7],
                    'officePhone': result[8]
                }
                return jsonify({'TCS_info': info})
            else:
                return jsonify({'message': 'Info not found'}), 404

        elif request.method == 'POST':
            update_info = {
                'id': id,
                'name': request.json.get('name'),
                'position': request.json.get('position'),
                'contactNumber': request.json.get('contactNumber'),
                'email': request.json.get('email'),
                'officeAddress': request.json.get('officeAddress'),
                'officePhone': request.json.get('officePhone')
            }

            # 更新資料庫中的資料
            cursor.execute(f"""
                UPDATE teacher
                SET name = %s, level = %s, phone = %s, email = %s, office_address = %s, office_phone = %s
                WHERE id = '{id}'
            """, (update_info['name'], update_info['position'], update_info['contactNumber'], update_info['email'], update_info['officeAddress'], update_info['officePhone']))

            # 提交變更
            conn.commit()

            return jsonify({'message': 'Info updated successfully', 'TCS_info': update_info})

    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500



@app.route('/SelectName/<string:id>', methods=['GET', 'POST'])
def select_name(id):
    try:
        if request.method == 'GET':
            # 查詢資料
            cursor.execute(f"SELECT student_id, name FROM `student` WHERE teacher_id='{id}'")
            results = cursor.fetchall()
            if results:
                names = []
                for result in results:
                    student_id = result[0]
                    name = result[1]
                    if name is not None and name != '':
                        name_data = {
                            'student_id': student_id,
                            'name': name
                        }
                        names.append(name_data)
                return jsonify({'names': names})
            else:
                return jsonify({'message': 'Name not found'}), 404
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@app.route('/stu_info/<string:id>', methods=['GET', 'POST'])
def get_and_update_info(id):
    try:
        if request.method == 'GET':
            # 查詢資料
            cursor.execute(f"SELECT * FROM student WHERE id = '{id}'")
            result = cursor.fetchone()

            if result:
                st_info = {
                    'id': result[0],
                    'student_id': result[1],
                    'name': result[2],
                    'email': result[3],
                    'grade': result[4],
                    'gender': result[5],
                    'teacher_id': result[6],
                    'phone': result[7],
                    'home_address': result[8],
                    'home_phone': result[9],
                    'home_contact': result[10]
                }
                return jsonify({'stu_info': st_info})
            else:
                return jsonify({'message': 'Info not found'}), 404

    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500
        
@app.route('/tcs_TeaName/<string:id>', methods=['GET'])
def Find_TeaName(id):
    try:
        if request.method == 'GET':
            # 查詢資料
            cursor.execute(f"SELECT name FROM `teacher` WHERE teacher_id='{id}'")
            results = cursor.fetchall()
            if results:
                tea_names = []
                for result in results:
                    name = {
                        'tea_name': result[0],
                    }
                    tea_names.append(name)
                return jsonify({'names': tea_names})
            else:
                return jsonify({'message': 'Name not found'}), 404
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@app.route('/tcs_StuAcc/<string:id>/<string:year>/<string:semaster>', methods=['GET'])
def Find_StuAcc(id,year,semaster):
    try:
        if request.method == 'GET':
            # 查詢資料
            
            cursor.execute(f"SELECT * FROM `accommodation_st` WHERE studentId='{id}' AND academicYear='{year}' AND semaster='{semaster}'")
            results = cursor.fetchall()
            if results:
                Stu_acc = []
                for result in results:
                    Stu_acc_info = {
                        'studentId': result[0],
                        'address': result[1],
                        'roomates': result[2],
                        'landlordName': result[3],
                        'landlordPhone': result[4],
                        'rent': result[5],
                        'academicYear': result[6],
                        'semaster': result[7]
                    }
                    Stu_acc.append(Stu_acc_info)
                return jsonify({'acc_info': Stu_acc})
            else:
                return jsonify({'message': 'Name not found'}), 404
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

@app.route('/get_TeaRecord/<string:id>/<int:year>/<string:semaster>/<string:tid>', methods=['GET', 'POST'])
def get_TeaRecord(id, year, semaster,tid):
    try:
        if request.method == 'GET':
            # 將民國年轉換成西元年
            year = year + 1911
            
            # 計算學年學期的日期區間
            start_date, end_date = get_semester_date_range_t(year, semaster)

            # 查詢資料
            cursor.execute(f"SELECT date, tea_detail, visit_id, teacher_id FROM visit_detail WHERE student_id='{id}' AND date BETWEEN '{start_date}' AND '{end_date}'")
            results = cursor.fetchall()
            
            if results:
                Tea_Rec = []
                for result in results:
                    detail_fields = result[1].split('%')
                    
                    # 處理 visitResult 欄位
                    visit_result = detail_fields[6]
                    visit_result_details = ''
                    if visit_result.startswith('其他'):
                        visit_result_details = visit_result.split('(')[1].strip(')')
                        visit_result = '其他'

                    visit_staus = detail_fields[4]
                    visit_staus_details = ''
                    if visit_staus.startswith('待加強'):
                        visit_staus_details = visit_staus.split('(')[1].strip(')')
                        visit_staus = '待加強'

                    facilities_n=detail_fields[3]
                    facilities_details = ''
                    if facilities_n.startswith('欠佳'):
                        facilities_details = facilities_n.split('(')[1].strip(')')
                        facilities_n = '欠佳'
                    
                    environment_n=detail_fields[2]
                    environment_details = ''
                    if environment_n.startswith('欠佳'):
                        environment_details = environment_n.split('(')[1].strip(')')
                        environment_n = '欠佳'
                    
                    Tea_Rec_info = {
                        'date': result[0],
                        'deposit': detail_fields[0],
                        'bill': detail_fields[1],
                        'environment': environment_n,
                        'environmentDetails': environment_details,
                        'facilities': facilities_n,
                        'facilitiesDetails':facilities_details,
                        'visitStatus': visit_staus,
                        'visitStatusDetails': visit_staus_details,
                        'well': detail_fields[5],
                        'visitResult': visit_result,
                        'visitResultDetails': visit_result_details,
                        'visitResultOthers': detail_fields[7],
                        'visit_id': result[2],
                        'teacher_id': result[3],
                    }
                    
                    Tea_Rec.append(Tea_Rec_info)
                
                return jsonify({'teaRecord_info': Tea_Rec})
            else:
                return jsonify({'message': 'Name not found'}), 404
        
        elif request.method == 'POST':
             # 将民國年轉換成西元年
            year = year + 1911

            # 計算學年學期的日期區間
            start_date, end_date = get_semester_date_range_t(year, semaster)
            cursor.execute(f"SELECT date, tea_detail, visit_id, teacher_id FROM visit_detail WHERE student_id='{id}' AND date BETWEEN '{start_date}' AND '{end_date}'")
            results = cursor.fetchall()
            # 查詢資料
            if results:
                data = request.get_json()
                #檢查date是否在112年第二學期
                date = data['date']
                deposit = data['deposit']
                bill = data['bill']
                environment = data['environment']
                facilities = data['facilities']
                visitStatus = data['visitStatus']
                well = data['well']
                visitResult = data['visitResult']
                visitResultDetails = data['visitResultDetails']
                visitResultOthers = data['visitResultOthers']
                #teacher_id = data['teacher_id']
                environmentDetails=data['environmentDetails']
                facilitiesDetails=data['facilitiesDetails']
                visitStatusDetails=data['visitStatusDetails']
                
                # 若visitResultDetails不為空，將visitResult設為其他()，並將visitResultDetails放入()中
                if visitResultDetails != '':
                    visitResult = f"其他({visitResultDetails})"

                if environmentDetails != '':
                    environment = f"欠佳({environmentDetails})"
                
                if facilitiesDetails != '':
                    facilities = f"欠佳({facilitiesDetails})"
                
                if visitStatusDetails != '':
                    visitStatus = f"待加強({visitStatusDetails})"
                
                # 組合完整的茶訪細節
                tea_detail = f"{deposit}%{bill}%{environment}%{facilities}%{visitStatus}%{well}%{visitResult}%{visitResultOthers}"
                
                # 更新資料到資料庫
                cursor.execute(
                    "UPDATE visit_detail SET date = %s, tea_detail = %s WHERE visit_id = %s",
                    (date, tea_detail, results[0][2])
                )
                conn.commit()
                
                return jsonify({'message': 'Record updated successfully'}), 201
            else:
                data = request.get_json()
                date = data['date']
                deposit = data['deposit']
                bill = data['bill']
                environment = data['environment']
                facilities = data['facilities']
                visitStatus = data['visitStatus']
                well = data['well']
                visitResult = data['visitResult']
                visitResultOthers = data['visitResultOthers']


                if 'visitResultDetails' in data:
                    visitResultDetails = data['visitResultDetails']
                else:
                    visitResultDetails = ''   

                if 'environmentDetails' in data:
                    environmentDetails = data['environmentDetails']
                else:
                    environmentDetails = ''
                
                if 'facilitiesDetails' in data:
                    facilitiesDetails = data['facilitiesDetails']
                else:
                    facilitiesDetails = ''
                
                if 'visitStatusDetails' in data:
                    visitStatusDetails = data['visitStatusDetails']
                else:
                    visitStatusDetails = ''

                if visitResultDetails != '':
                    visitResult = f"其他({visitResultDetails})"

                if environmentDetails != '':
                    environment = f"欠佳({environmentDetails})"
                
                if facilitiesDetails != '':
                    facilities = f"欠佳({facilitiesDetails})"
                
                if visitStatusDetails != '':
                    visitStatus = f"待加強({visitStatusDetails})"             
                # Determine the new visit_id
                cursor.execute("SELECT MAX(visit_id) FROM visit_detail")
                last_visit_id = cursor.fetchone()[0]
                if last_visit_id:
                    new_visit_id = str(int(last_visit_id) + 1)
                else:
                    new_visit_id = '1'

                tea_detail = f"{deposit}%{bill}%{environment}%{facilities}%{visitStatus}%{well}%{visitResult}%{visitResultOthers}"
                
                # Insert the new record into the database
                cursor.execute(
                    "INSERT INTO visit_detail (visit_id, teacher_id, student_id, date, tea_detail, stu_detail) VALUES (%s, %s, %s, %s, %s, %s)",
                    (new_visit_id, tid, id, date, tea_detail, '')
                )
                conn.commit()

                return jsonify({'message': 'Record inserted successfully'}), 201

    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

def get_semester_date_range_t(year, semaster):
    """
    計算給定學年和學期的日期區間。
    """
    if semaster == '1':
        start_date = f"{year}-09-01"
        end_date = f"{year + 1}-01-31"
    elif semaster == '2':
        start_date = f"{year + 1}-02-01"
        end_date = f"{year + 1}-08-31"
    else:
        raise ValueError("Invalid semester value")
    return start_date, end_date

@app.route('/get_StuRecord/<string:id>/<int:year>/<string:semaster>', methods=['GET'])
def get_StuRecord(id, year, semaster):
    try:
        if request.method == 'GET':
            # 將民國年轉換成西元年
            year = year + 1911
            
            # 計算學年學期的日期區間
            start_date, end_date = get_semester_date_range(year, semaster)

            # 查詢資料
            cursor.execute(f"SELECT date,stu_detail FROM visit_detail WHERE student_id='{id}' AND date BETWEEN '{start_date}' AND '{end_date}'")
            results = cursor.fetchall()
            
            if results:
                Stu_Rec = []
                for result in results:
                    detail_fields = result[1].split('%')
                    
                    
                    Stu_Rec_info = {
                        # 'date': result[0],
                        'teacherPhone': detail_fields[0],
                        'landlordName': detail_fields[1],
                        'landlordPhone': detail_fields[2],
                        'studentAddress': detail_fields[3],
                        'monthlyRent': detail_fields[4],
                        'deposit_s': detail_fields[5],
                        'houseType': detail_fields[6],
                        'roomType': detail_fields[7],
                        'Recommend': detail_fields[8],
                        'woodStructure': detail_fields[9] ,
                        'fireAlarm': detail_fields[10] ,
                        'escapeRoute': detail_fields[11] ,
                        'lockManagement': detail_fields[12] ,
                        'lighting': detail_fields[13] ,
                        'circuitSafety': detail_fields[14],
                        'emergencyContacts': detail_fields[15] ,
                        'electricEquipment': detail_fields[16] ,
                        'fireExtinguisher': detail_fields[17] ,
                        'hotWater': detail_fields[18] ,
                        'roomBed': detail_fields[19],
                        'CCTV': detail_fields[20],
                        'law': detail_fields[21],
                    }
                    
                    Stu_Rec.append(Stu_Rec_info)
                
                return jsonify({'stuRecord_info': Stu_Rec})
            else:
                return jsonify({'message': 'Name not found'}), 404
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500

def get_semester_date_range(year, semaster):
    """
    計算給定學年和學期的日期區間。
    """
    if semaster == '1':
        start_date = f"{year}-09-01"
        end_date = f"{year + 1}-01-31"
    elif semaster == '2':
        start_date = f"{year + 1}-02-01"
        end_date = f"{year + 1}-08-31"
    else:
        raise ValueError("Invalid semester value")
    return start_date, end_date



###############################################################3STUDENT
@app.route('/info/<string:id>', methods=['GET', 'POST'])
def get_and_update_info_st(id):
    try:
        if request.method == 'GET':
            # 查詢資料
            cursor.execute(f"SELECT * FROM student WHERE id = '{id}'")
            result = cursor.fetchone()

            if result:
                info = {
                    'id': result[0],
                    'student_id': result[1],
                    'name': result[2],
                    'email': result[3],
                    'grade': result[4],
                    'gender': result[5],
                    'teacher_id': result[6],
                    'phone': result[7],
                    'home_address': result[8],
                    'home_phone': result[9],
                    'home_contact': result[10]
                }
                return jsonify({'info': info})
            else:
                return jsonify({'message': 'Info not found'}), 404

        elif request.method == 'POST':
            update_info = {
                'id': id,
                'name': request.json.get('name'),
                'student_id': request.json.get('student_id'),
                'email': request.json.get('email'),
                'grade': request.json.get('grade'),
                'gender': request.json.get('gender'),
                'teacher_id': request.json.get('teacher_id'),
                'phone': request.json.get('phone'),
                'home_address': request.json.get('home_address'),    
                'home_phone': request.json.get('home_phone'),
                'home_contact': request.json.get('home_contact')
            }

            # 更新資料庫中的資料
            cursor.execute(f"""
                UPDATE student
                SET id=%s, name=%s, student_id=%s, email=%s, grade=%s, gender=%s, teacher_id=%s, phone=%s, home_address=%s, home_phone=%s, home_contact=%s
                WHERE id = '{id}'
            """, (update_info['id'],update_info['name'],update_info['student_id'],update_info['email'],update_info['grade'],update_info['gender'],update_info['teacher_id'],update_info['phone'],update_info['home_address'],update_info['home_phone'],update_info['home_contact']))

            # 提交變更
            conn.commit()

            return jsonify({'message': 'Info updated successfully', 'info': update_info})

    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500


@app.route('/accommodation_st/<string:studentId>/<string:academicYear>/<string:semaster>', methods=['GET', 'POST'])
def get_and_update_accommodation_st(studentId,academicYear,semaster):
    try:
        app.logger.debug(f"Request method A: {request.method}")
        if request.method == 'GET':
            
            # 查询数据
            cursor.execute(f"SELECT * FROM accommodation_st WHERE studentId = '{studentId}' AND academicYear = '{academicYear}' AND semaster = '{semaster}'")
            app.logger.debug("yes if")
            result = cursor.fetchone()

            if result:
                accommodation_st = {
                    'studentId': result[0],
                    'address': result[1],
                    'roomates': result[2],
                    'landlordName': result[3],
                    'landlordPhone': result[4],
                    'rent': result[5],
                    'academicYear': result[6],
                    'semaster': result[7]
                }
                return jsonify({'accommodation_st': accommodation_st})
            else:
                return jsonify({'message': 'Accommodation not found'}), 404

        elif request.method == 'POST':
            new_accommodation_st = {
                'studentId': studentId,
                'address': request.json.get('address'),
                'roomates': request.json.get('roomates'),
                'landlordName': request.json.get('landlordName'),
                'landlordPhone': request.json.get('landlordPhone'),
                'rent': request.json.get('rent'),
                'academicYear': request.json.get('academicYear'),
                'semaster': request.json.get('semaster')
            }

            cursor.execute(f"SELECT * FROM accommodation_st WHERE studentId = '{studentId}' AND academicYear = '{academicYear}' AND semaster = '{semaster}'")
            existing_record = cursor.fetchone()

            if existing_record:
                # 更新现有记录
                cursor.execute("""
                    UPDATE accommodation_st
                    SET address=%s, roomates=%s, landlordName=%s, landlordPhone=%s, rent=%s
                    WHERE studentId = %s AND academicYear = %s AND semaster = %s
                """, (new_accommodation_st['address'], new_accommodation_st['roomates'], new_accommodation_st['landlordName'], new_accommodation_st['landlordPhone'], new_accommodation_st['rent'], studentId, academicYear, semaster))
            else:
                # 插入新记录
                cursor.execute("""
                    INSERT INTO accommodation_st (studentId, address, roomates, landlordName, landlordPhone, rent, academicYear, semaster)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (new_accommodation_st['studentId'], new_accommodation_st['address'], new_accommodation_st['roomates'], new_accommodation_st['landlordName'], new_accommodation_st['landlordPhone'], new_accommodation_st['rent'], new_accommodation_st['academicYear'], new_accommodation_st['semaster']))

            # 提交更改
            conn.commit()

            return jsonify({'message': 'Accommodation inserted successfully', 'accommodation_st': new_accommodation_st})

    except Exception as e:
        app.logger.debug(f"Request method: {request.method}")
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500


@app.route('/visittime_st/<string:studentId>', methods=['GET', 'POST'])
def get_and_update_visittime_st(studentId):
    try:
        app.logger.debug(f"Request method A: {request.method}")
        if request.method == 'GET':
            
            # 查询数据
            cursor.execute(f"SELECT * FROM visittime_st WHERE studentId = '{studentId}' ")
            app.logger.debug("yes if")
            result = cursor.fetchone()
            available_time_str = result[3].strftime('%Y-%m-%d') if result[3] else None

            if result:
                visittime_st = {
                    'studentId': result[0],
                    'name': result[1],
                    'address': result[2],
                    'available_time': available_time_str
                }
                print(result[3])
                return jsonify({'visittime_st': visittime_st})
            else:
                return jsonify({'message': 'Accommodation not found'}), 404

        elif request.method == 'POST':
            new_visittime_st = {
                'studentId': studentId,
                'name': request.json.get('name'),
                'address': request.json.get('address'),
                'available_time': request.json.get('available_time')
                # 'available_date': datetime.strptime(request.json.get('available_date'), '%Y-%m-%d').date()
            }
            print(new_visittime_st)
            cursor.execute(f"SELECT * FROM visittime_st WHERE studentId = '{studentId}' ")
            existing_record = cursor.fetchone()

            if existing_record:
                #
                cursor.execute("""
                    UPDATE visittime_st
                    SET name=%s, available_time=%s, address=%s 
                    WHERE studentId = %s
                """, (new_visittime_st['name'],new_visittime_st['available_time'], new_visittime_st['address'],studentId ))
            else:
                # 
                cursor.execute("""
                    INSERT INTO visittime_st (studentId, name, address, available_time)
                    VALUES (%s,%s, %s, %s)
                """, (new_visittime_st['studentId'],new_visittime_st['name'], new_visittime_st['address'], new_visittime_st['available_time']))

            # 提交更改
            conn.commit()

            return jsonify({'message': 'Accommodation inserted successfully', 'visittime_st': new_visittime_st})

    except Exception as e:
        app.logger.debug(f"Request method: {request.method}")
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500    


@app.route('/repair_st/<string:studentId>/<string:address>', methods=['GET', 'POST'])
def get_and_update_repair_st(studentId, address):
    try:
        app.logger.debug(f"Request method: {request.method}")
        
        if request.method == 'GET':
            # 查询数据
            cursor.execute("SELECT * FROM repair_st WHERE studentId = %s AND address = %s", (studentId, address))
            app.logger.debug("GET request executed")
            result = cursor.fetchone()
            
            if result:
                repair_date_str = result[5].strftime('%Y-%m-%d') if result[5] else None
                
                repair_st = {
                    'name': result[0],
                    'email': result[1],
                    'phone': result[2],
                    'address': result[3],
                    'problem_description': result[4],
                    'problem_date': repair_date_str,
                    'studentId': result[6]
                }
                app.logger.debug(f"GET result: {repair_st}")
                return jsonify({'repair_st': repair_st})
            else:
                return jsonify({'message': 'Accommodation not found'}), 404

        elif request.method == 'POST':
            new_repair_st = {
                'name': request.json.get('name'),
                'email': request.json.get('email'),
                'phone': request.json.get('phone'),
                'address': request.json.get('address'),
                'problem_description': request.json.get('problem_description'),
                'problem_date': request.json.get('problem_date'),
                'studentId': studentId
            }

            cursor.execute("SELECT * FROM repair_st WHERE studentId = %s AND address = %s", (studentId, address))
            existing_record = cursor.fetchone()

            if existing_record:
                cursor.execute("""
                    UPDATE repair_st
                    SET name=%s, email=%s, phone=%s, problem_description=%s, problem_date=%s
                    WHERE studentId = %s AND address = %s
                """, (new_repair_st['name'], new_repair_st['email'], new_repair_st['phone'], new_repair_st['problem_description'], new_repair_st['problem_date'], studentId, address))
            else:
                cursor.execute("""
                    INSERT INTO repair_st (name, email, phone, address, problem_description, problem_date, studentId)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (new_repair_st['name'], new_repair_st['email'], new_repair_st['phone'], new_repair_st['address'], new_repair_st['problem_description'], new_repair_st['problem_date'], new_repair_st['studentId']))

            # 提交更改
            conn.commit()

            return jsonify({'message': 'Repair record inserted or updated successfully', 'repair_st': new_repair_st})

    except Exception as e:
        app.logger.debug(f"Request method: {request.method}")
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500


@app.route('/repair/<string:student_id>', methods=['GET', 'POST'])
def get_and_update_repair(student_id):
    try:
        app.logger.debug(f"Request method A: {request.method}")
        if request.method == 'GET':
            # 查询数据
            cursor.execute("SELECT landlordName FROM accommodation_st WHERE studentId = %s AND academicYear = %s AND semaster = %s", (student_id,'112','2'))
            landlordName = cursor.fetchone()
            app.logger.debug(f"landlordName: {landlordName}")
            cursor.execute("SELECT landlord_id FROM landlord WHERE name = %s", (landlordName))
            landlord_id = cursor.fetchone()
            app.logger.debug(f"landlord_id: {landlord_id}")

            
            if landlord_id:
                repair={
                'landlord_id':landlord_id[0]
                }
                return jsonify({'repair': repair})
            else:
                return jsonify({'message': 'Info not found'}), 404

        elif request.method == 'POST':
            cursor.execute("SELECT repair_id FROM repair ORDER BY repair_id DESC LIMIT 1")
            last_repair_id = cursor.fetchone()

            if last_repair_id:
                # Extract the numerical part and increment it
                last_repair_id_num = int(last_repair_id[0][1:])
                new_repair_id_num = last_repair_id_num + 1
            else:
                # If there are no records yet, start with 1
                new_repair_id_num = 1

            # Format the new repair_id
            repair_id = f"r{new_repair_id_num:03d}"
            # 更新資料
            data = request.get_json()
            landlord_id = data['landlord_id']
            repair_detail = data['repair_detail']
            cursor.execute("Insert into repair (repair_id,student_id,landlord_id,repair_detail,repair_response) values (%s,%s,%s,%s,%s)", (repair_id,student_id,landlord_id,repair_detail,'0'))
            conn.commit()
            return jsonify({'message': 'Info updated successfully', 'repair': data})
        
    except Exception as e:
        app.logger.debug(f"Request method: {request.method}")
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500  


@app.route('/get_StRecord/<string:id>', methods=['GET', 'POST'])
def get_StRecord(id):
    try:
        if request.method == 'GET':
            # 查詢資料
            cursor.execute("SELECT date, stu_detail, visit_id, student_id, teacher_id FROM visit_detail WHERE student_id=%s AND date BETWEEN '2024-02-01' AND '2024-08-31'", (id,))
            results = cursor.fetchall()
            app.logger.debug(f"results: {results}")

            if results:
                St_Rec = []
                for result in results:
                    app.logger.debug(f"result: {result}")
                    detail_fields = result[1].split('%')
                    
                    St_Rec_info = {
                        'phone': detail_fields[0],
                        'landlordName': detail_fields[1],
                        'landlordPhone': detail_fields[2],
                        'studentAddress': detail_fields[3],
                        'monthlyRent': detail_fields[4],
                        'deposit': detail_fields[5],
                        'houseType': detail_fields[6],
                        'roomType': detail_fields[7],
                        'recommend': detail_fields[8],
                        'woodStructure': detail_fields[9],
                        'fireAlarm': detail_fields[10],
                        'escapeRoute': detail_fields[11],
                        'lockManagement': detail_fields[12],
                        'lighting': detail_fields[13],
                        'circuitSafety': detail_fields[14],
                        'emergencyContacts': detail_fields[15],
                        'electricEquipment': detail_fields[16],
                        'fireExtinguisher': detail_fields[17],
                        'hotwater': detail_fields[18],
                        'roombed': detail_fields[19],
                        'CCTVyes': detail_fields[20],
                        'law': detail_fields[21]
                    }
                    
                    St_Rec.append(St_Rec_info)
                
                return jsonify({'stRecord_info': St_Rec})
            else:
                return jsonify({'message': 'Name not found'}), 404
        
        elif request.method == 'POST':
            data = request.get_json()
            cursor.execute("SELECT date, stu_detail, visit_id, teacher_id FROM visit_detail WHERE student_id=%s AND date BETWEEN '2024-02-01' AND '2024-08-31'", (id,))
            results = cursor.fetchall()
            
            if results:
                # 更新現有記錄
                phone = data['phone']
                landlordName = data['landlordName']
                landlordPhone = data['landlordPhone']
                studentAddress = data['studentAddress']
                monthlyRent = data['monthlyRent']
                deposit = data['deposit']
                houseType = data['houseType']
                roomType = data['roomType']
                recommend = data['recommend']
                woodStructure = data['woodStructure']
                fireAlarm = data['fireAlarm']
                escapeRoute = data['escapeRoute']
                lockManagement = data['lockManagement']
                lighting = data['lighting']
                circuitSafety = data['circuitSafety']
                emergencyContacts = data['emergencyContacts']
                electricEquipment = data['electricEquipment']
                fireExtinguisher = data['fireExtinguisher']
                hotwater = data['hotwater']
                roombed = data['roombed']
                CCTVyes = data['CCTVyes']
                law = data['law']
                
                # 組合完整的茶訪細節
                st_detail = f"{phone}%{landlordName}%{landlordPhone}%{studentAddress}%{monthlyRent}%{deposit}%{houseType}%{roomType}%{recommend}%{woodStructure}%{fireAlarm}%{escapeRoute}%{lockManagement}%{lighting}%{circuitSafety}%{emergencyContacts}%{electricEquipment}%{fireExtinguisher}%{hotwater}%{roombed}%{CCTVyes}%{law}"
                
                # 更新資料到資料庫
                cursor.execute(
                    "UPDATE visit_detail SET stu_detail = %s WHERE visit_id = %s",
                    (st_detail, results[0][2])
                )
                conn.commit()
                
                return jsonify({'message': 'Record updated successfully'}), 201
            else:
                # 插入新記錄
                cursor.execute("SELECT teacher_id FROM student WHERE id = %s", (id,))
                teacher_id = cursor.fetchone()[0]

                phone = data['phone']
                landlordName = data['landlordName']
                landlordPhone = data['landlordPhone']
                studentAddress = data['studentAddress']
                monthlyRent = data['monthlyRent']
                deposit = data['deposit']
                houseType = data['houseType']
                roomType = data['roomType']
                recommend = data['recommend']
                woodStructure = data['woodStructure']
                fireAlarm = data['fireAlarm']
                escapeRoute = data['escapeRoute']
                lockManagement = data['lockManagement']
                lighting = data['lighting']
                circuitSafety = data['circuitSafety']
                emergencyContacts = data['emergencyContacts']
                electricEquipment = data['electricEquipment']
                fireExtinguisher = data['fireExtinguisher']
                hotwater = data['hotwater']
                roombed = data['roombed']
                CCTVyes = data['CCTVyes']
                law = data['law']

                # 查询当前数据库中的记录数
                cursor.execute("SELECT COUNT(*) FROM visit_detail")
                visit_count = cursor.fetchone()[0]

                # 将visit_id设置为记录数加1
                visit_id = str(visit_count + 1)

                st_detail = f"{phone}%{landlordName}%{landlordPhone}%{studentAddress}%{monthlyRent}%{deposit}%{houseType}%{roomType}%{recommend}%{woodStructure}%{fireAlarm}%{escapeRoute}%{lockManagement}%{lighting}%{circuitSafety}%{emergencyContacts}%{electricEquipment}%{fireExtinguisher}%{hotwater}%{roombed}%{CCTVyes}%{law}"
                
                # 插入新資料到資料庫
                cursor.execute(
                    "INSERT INTO visit_detail (visit_id, teacher_id, student_id, date, tea_detail, stu_detail) VALUES (%s, %s, %s, %s, %s, %s)",
                    (visit_id, teacher_id, id, '2024-02-02', '', st_detail)
                )
                conn.commit()

                return jsonify({'message': 'Record inserted successfully'}), 200

    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'message': 'Internal Server Error'}), 500
    
# @app.route('/login/<string:username>/<string:password>', methods=['GET','POST'])
# def Find_login(username,password):
#     try:
#         if request.method == 'GET':
#             # 查詢資料
#             cursor.execute(f"SELECT * FROM `account` WHERE id='{username}' AND password='{password}'")
#             results = cursor.fetchall()
#             if results:
#                 tea_names = []
#                 for result in results:
#                     name = {
#                         'username': result[0],
#                         'password': result[1],
#                         'type': result[2]
#                     }
#                     tea_names.append(name)
#                 return jsonify({'login': tea_names})
#             else:
#                 return jsonify({'message': 'Name not found'}), 404
#     except Exception as e:
#         app.logger.error(f"Error occurred: {e}")
#         return jsonify({'message': 'Internal Server Error'}), 500
#--------------------------------------------------------------TCS----------------------------------------------------------------
@app.route('/api/all_comment', methods=['GET'])# 用法是運行後在網址後面加上/data/要查詢的資料表名稱，例如127.0.0.1:5000/data/account
def all_comment():
    try:
        cursor.execute("USE final_project;")
        sql = f"""
        SELECT comment_id,post_id,COALESCE(ad.name, l.name, s.name, t.name),COALESCE(ad.personal_pic, l.personal_pic, s.personal_pic, t.personal_pic),comment_detail,a.id FROM comment a
LEFT JOIN administrator ad ON a.id = ad.id
LEFT JOIN landlord l ON a.id = l.id
LEFT JOIN student s ON a.id = s.id
LEFT JOIN teacher t ON a.id = t.id;
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        response_object = {'status': 'success'}
        response_object['data'] = []
        for row in result:
            response_object['data'].append({'comment_id': row[0],'post_id': row[1],'username': row[2],'avatar': row[3],'content': row[4],'id': row[5]})
        response_object['status'] = 'success'
        #print(response_object)
        return jsonify(response_object)
    except:
        return jsonify({'status': 'fail'})

@app.route('/api/all_rent_comment', methods=['GET'])# 用法是運行後在網址後面加上/data/要查詢的資料表名稱，例如127.0.0.1:5000/data/account
def all_rent_comment():
    try:
        cursor.execute("USE final_project;")
        sql = f"""
       SELECT 
    rent_comment_id,
    rent_id,
    COALESCE(ad.name, l.name, s.name, t.name) AS name,
    COALESCE(ad.personal_pic, l.personal_pic, s.personal_pic, t.personal_pic) AS personal_pic,
    comment_detail,
    rating,
    COALESCE(ad.id, l.id, s.id, t.id) AS user_id
FROM 
    rent_comment a
LEFT JOIN 
    administrator ad ON a.id = ad.id
LEFT JOIN 
    landlord l ON a.id = l.id
LEFT JOIN 
    student s ON a.id = s.id
LEFT JOIN 
    teacher t ON a.id = t.id;

        """
        cursor.execute(sql)
        result = cursor.fetchall()
        response_object = {'status': 'success'}
        response_object['data'] = []
        for row in result:
            response_object['data'].append({'comment_id': row[0],'rent_id': row[1],'username': row[2],'avatar': row[3],'content': row[4],'rating': row[5],'user_id': row[6]})
        response_object['status'] = 'success'
        #print(response_object)
        return jsonify(response_object)       
    except:
        return jsonify({'status': 'fail'})
    
@app.route('/api/get_rent_info', methods=['GET'])# 用法是運行後在網址後面加上/data/要查詢的資料表名稱，例如127.0.0.1:5000/data/account
def get_rent_info():
    try:
        cursor.execute("USE final_project;")
        sql = f"""
        SELECT * FROM rent_information;
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        response_object = {'status': 'success'}
        response_object['data'] = []
        for row in result:
            response_object['data'].append({'rent_id': row[0],'build_year': row[1],'build_type': row[2],'address': row[3],'rent_limitation': row[4],'rent': row[5],'picture': row[7],'publish_time': row[8],'other_info': row[9],'landlord_id': row[6]})
        response_object['status'] = 'success'
        #print(response_object)
        return jsonify(response_object)
    except:
        return jsonify({'status': 'fail'})
    
@app.route('/api/get_landlord_phone/<string:id>', methods=['GET'])# 用法是運行後在網址後面加上/data/要查詢的資料表名稱，例如127.0.0.1:5000/data/account
def get_landlord_phone(id):
    cursor.execute(f"SELECT phone FROM landlord WHERE id = '{id}'")
    result = cursor.fetchone()

    if result:
                info = {
                    'phone': result[0],
                }
                return jsonify({'landlord_phone': info})
    else:
                return jsonify({'message': 'Info not found'}), 404
    
@app.route('/api/message', methods=['POST'])
def addMessage():
    try:
        cursor.execute("USE final_project;")
        sql = f"SELECT contract_id FROM contract;"
        cursor.execute(sql)
        result = cursor.fetchall()
        no_in = "C001"
        result = [result[i][0] for i in range(len(result))]
        for i in range(1,1000):
            x = "C"
            x+=str(i).zfill(3)
            if x not in result:
                no_in = x
                break
        data = request.get_json()
        print(data)
        post_id = data["post_id"]
        id = data["user_id"]
        comment_detail = data["text"]
        cursor.execute("INSERT INTO final_project.comment (post_id,id,comment_detail) VALUES (%s,%s,%s)", (post_id, id, comment_detail))
        conn.commit()
        response_object = {'status': 'success'}
        return jsonify(response_object)
    except Exception as e:
        print(e)
        return jsonify({'status': 'fail'})
    
@app.route('/api/insert_comment_two', methods=['POST'])
def insert_comment_two():
    try:
        #input_string = input_string.split(',')
        input_string = [0]*4
        data = request.json
        input_string[1] = data['post_id']
        input_string[0] = data['user_id']
        input_string[2] = data['content']
        print(input_string)
        cursor.execute("USE final_project;")
        sql = f"SELECT comment_id FROM comment;"
        cursor.execute(sql)
        result = cursor.fetchall()
        no_in = "C001"
        result = [result[i][0] for i in range(len(result))]
        for i in range(1,1000):
            x = "C"
            x+=str(i).zfill(3)
            if x not in result:
                no_in = x
                break
        #print(no_in)
        sql = f"INSERT INTO comment VALUES ('{no_in}','{input_string[0]}', '{input_string[1]}','{input_string[2]}','0','0');"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        sql = f"""
        SELECT COALESCE(ad.personal_pic, l.personal_pic, s.personal_pic, t.personal_pic),COALESCE(ad.name, l.name, s.name, t.name) FROM  account a
LEFT JOIN administrator ad ON a.id = ad.id
LEFT JOIN landlord l ON a.id = l.id
LEFT JOIN student s ON a.id = s.id
LEFT JOIN teacher t ON a.id = t.id WHERE a.id = "{input_string[0]}";
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        response_object = {'avatar_picture': f'{result[0][0]}'}
        response_object['username'] = f'{result[0][1]}'
        #print(response_object)
        #print(sql)
        return jsonify(response_object)
    except:
        return jsonify({'status': 'fail'})

@app.route('/api/insert_rent_comment', methods=['POST'])
def insert_rent_comment():
    try:
        #input_string = input_string.split(',')
        input_string = [0]*4
        data = request.json
        input_string[1] = data['rent_id']
        input_string[0] = data['user_id']
        input_string[2] = data['content']
        input_string[3] = data['rating']
        print(input_string)
        cursor.execute("USE final_project;")
        sql = f"SELECT rent_comment_id FROM rent_comment;"
        cursor.execute(sql)
        result = cursor.fetchall()
        no_in = "RC001"
        result = [result[i][0] for i in range(len(result))]
        for i in range(1,1000):
            x = "RC"
            x+=str(i).zfill(3)
            if x not in result:
                no_in = x
                break
        #print(no_in)
        sql = f"INSERT INTO rent_comment VALUES ('{no_in}','{input_string[0]}', '{input_string[1]}','{input_string[2]}',{str(input_string[3])});"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        response_object = {'status': 'success'}
        sql = f"""
        SELECT COALESCE(ad.personal_pic, l.personal_pic, s.personal_pic, t.personal_pic),COALESCE(ad.name, l.name, s.name, t.name) FROM  account a
LEFT JOIN administrator ad ON a.id = ad.id
LEFT JOIN landlord l ON a.id = l.id
LEFT JOIN student s ON a.id = s.id
LEFT JOIN teacher t ON a.id = t.id WHERE a.id = "{input_string[0]}";
        """
        cursor.execute(sql)
        result = cursor.fetchall()
        response_object = {'avatar_picture': f'{result[0][0]}'}
        response_object['username'] = f'{result[0][1]}'
        #print(response_object)
        #print(sql)
        return jsonify(response_object)
    except:
        return jsonify({'status': 'fail'})

@app.route('/api/delete_rent_comment/<string:comment_id>', methods=['GET'])
def delete_rent_comment(comment_id):
    try:
        cursor.execute("USE final_project;")
        sql = f"DELETE FROM rent_comment WHERE rent_comment_id = '{comment_id}';"
        cursor.execute(sql)
        conn.commit()
        response_object = {'status': 'success'}
        return jsonify(response_object)
    except Exception as e:
        print(e)  # Optional: log the error
        return jsonify({'status': 'fail'}), 500
    

@app.route('/api/update_rent_comment/<comment_id>', methods=['POST'])
def update_rent_comment(comment_id):
    try:
        data = request.json
        new_content = data.get('content')

        cursor.execute("USE final_project;")
        sql = f"UPDATE rent_comment SET comment_detail='{new_content}' WHERE rent_comment_id = '{comment_id}';"
        cursor.execute(sql)
        conn.commit()

        if cursor.rowcount > 0:
            result = {"status": "success"}
        else:
            result = {"status": "error"}

        return jsonify(result)
    except Exception as e:
        print(str(e))
        result = {"status": "error"}
        return jsonify(result)
    
@app.route('/api/advertisement/insert_advertisement/<input_string>', methods=['GET'])
def insert_advertisement(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        sql = f"SELECT ad_id FROM advertisement;"
        cursor.execute(sql)
        result = cursor.fetchall()
        no_in = "AD001"
        result = [result[i][0] for i in range(len(result))]
        for i in range(1,1000):
            x = "AD"
            x+=str(i).zfill(3)
            if x not in result:
                no_in = x
                break
        ad_id = no_in
        sql = f"SELECT rent_id FROM rent_information;"
        cursor.execute(sql)
        result = cursor.fetchall()
        no_in = "R001"
        result = [result[i][0] for i in range(len(result))]
        for i in range(1,1000):
            x = "R"
            x+=str(i).zfill(3)
            if x not in result:
                no_in = x
                break
        #print(no_in)
        sql = f"INSERT INTO rent_information VALUES ('{no_in}','{input_string[6]}', '{input_string[5]}','{input_string[3]}','',{input_string[2]},'{input_string[0]}','{input_string[7]}','','');"
        #print(sql)
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        sql = f"INSERT INTO advertisement VALUES ('{ad_id}','{no_in}', '{input_string[4]}','{input_string[1]}','0');"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)
    
@app.route('/api/insert_post/<input_string>', methods=['GET'])
def insert_post(input_string):
    try:
        input_string = input_string.split(',')
        cursor.execute("USE final_project;")
        sql = f"SELECT post_id FROM post;"
        cursor.execute(sql)
        result = cursor.fetchall()
        no_in = "P001"
        result = [result[i][0] for i in range(len(result))]
        for i in range(1,1000):
            x = "P"
            x+=str(i).zfill(3)
            if x not in result:
                no_in = x
                break
        sql = f"INSERT INTO post VALUES ('{no_in}','{input_string[0]}', '{input_string[1]}','{input_string[2]}','0');"
        cursor.execute(sql)
        conn.commit()  # Commit the changes to the database
        if cursor.rowcount > 0:
            result = "success"
        else:
            result = "error"
        return jsonify(result)
    except:
        result = "error"
        return jsonify(result)
    
if __name__ == '__main__':
    app.run()
