import psycopg2

# Connection parameters
dbname = 'postgres'
user = 'postgres'
password = 'zack'
host = 'localhost'
port = 5432

try:
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port)
    
    
    #queries
    print("Connection Successful")
    print("Here are your queries")
    print("1. INSERT INTO agency (agencyCode,agencyName,agencyType,city) VALUES ('mycode','myagency','police','Ashburn')")
    print("2. DELETE FROM agency WHERE agencyCode = 'mycode'")
    print("3. UPDATE agency SET agencyName = 'myagency1' where agencyCode = 'mycode'")
    print("4. Select * FROM agency WHERE city = 'Anchorage'")
    print("5. SELECT max(recordId) FROM crime")
    print("6. SELECT recordId, victimSex, victimAge FROM victim ORDER BY victimAge desc")
    print("7. SELECT agency.agencyName, agency.city, locations.states FROM agency JOIN locations ON agency.city = locations.city")
    print("8. SELECT COUNT(recordId),perpetratorSex from perpetrators GROUP BY perpetratorSex")
    print("9. SELECT COUNT(recordId),weapon FROM crime WHERE agencyCode IN (SELECT agencyCode from agency where agency.city = 'Anchorage') GROUP BY weapon")
    print("10. Error Testing")
    user_query = int(input("Please type the number of the query you want "))
    
    #cursor
    cur = conn.cursor()

    match(user_query):
        case 1:
            cur.execute("INSERT into agency (agencyCode,agencyName,agencyType,city) values ('mycode','myagency','police','Ashburn')")
            conn.commit()
            print('Insert successful')

        case 2:
            cur.execute("DELETE FROM agency WHERE agencyName = 'myagency'")
            conn.commit()
            print("DELETE successful")
        
        case 3:
            cur.execute("UPDATE agency SET agencyName = 'myagency1' where agencyCode = 'mycode'")
            conn.commit()
            print("UPDATE successful")

        case 4:
            cur.execute("Select * FROM agency WHERE city = 'Anchorage'")
            query = cur.fetchall()
            for row in query:
                print(row)

        case 5:
            cur.execute("SELECT max(recordId) FROM crime")
            query = cur.fetchall()
            for row in query:
                print(row)
        case 6:
            cur.execute("SELECT recordId, victimSex, victimAge FROM victim ORDER BY victimAge desc")
            query = cur.fetchall()
            for row in query:
                print(row)

        case 7:
            cur.execute("SELECT agency.agencyName, agency.city, locations.states FROM agency JOIN locations ON agency.city = locations.city")
            query = cur.fetchall()
            for row in query:
                print(row)

        case 8:
            cur.execute("SELECT COUNT(recordId),perpetratorSex from perpetrators GROUP BY perpetratorSex")
            query = cur.fetchall()
            for row in query:
                print(row)

        case 9:
            cur.execute("SELECT COUNT(recordId),weapon FROM crime WHERE agencyCode IN (SELECT agencyCode from agency where agency.city = 'Anchorage') GROUP BY weapon")
            query = cur.fetchall()
            for row in query:
                print(row)

        case 10:
            raise

except (Exception, psycopg2.Error) as error:
    conn.rollback()
    print("Error Raised: ",error)

finally:
    if conn is not None:
        conn.close()
