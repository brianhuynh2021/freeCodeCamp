from config import config
import psycopg2

args = {
   "user_id":"7250f8f6-6cf0-488e-87b2-346111603aad",
   "phaseIds":["aflajf823", "kfdlkf89"],
   "activityIds":["flafkj83i", "fasnkg092"],
   "e_profile_id":"dkfal89l",
   "profiles":[
      "profile1",
      "profile2",
      " profile3"
   ],
   "profileStatus": "Draft"
}
def load_data_from_eprofiles():
    sql = f'''select name
            where name = 'HAL'; '''
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(result)
    return result

if __name__ == '__main__':
    load_data_from_eprofiles()