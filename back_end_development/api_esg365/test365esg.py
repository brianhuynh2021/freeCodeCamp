from common.db import Database

class  Eprofiles:
    def __init__(self):
        self.db = Database()

    def handle(self, args):
        profiles = []
        self.args = args
        phaseIds = self.args["phaseIds"]
        activityIds = self.args["activityIds"]
        userEmail = self.args['email']
        profileStatus = self.args['profileStatus']
        permissionRole = self.query_user_id(userEmail)
        if permissionRole[1] == "Viewer":
            profileStatus =  profileStatus[1]
        elif permissionRole[1] == "Editor":
            permissionRole = profileStatus[1:]
        get_profiles = self.query_profiles(phaseIds, activityIds, profileStatus, permissionRole)
        profiles.append(get_profiles)
        return profiles

    def get_role(self, userEmail):
        sql = f'''select r."name" role_name, p.code permission_code, r.id role_id , p.id  permission_id from users u 
            join roles r on r.id = u.role_id 
            join roles_permissions rp on rp.role_id = r.id 
            join permissions p on p.id = rp.permission_id 
            where u.email = '{userEmail}' '''
        result = self.db.query(sql)
        return result[0][0]

    def query_profiles_viewer(self, activity_ids: list, phaseIds: list):
        permission_code = "PROFILE_R"
        # check role
        if not self.check_role(args["email"], permission_code):
            return []
        else: 
            sql = f'''select ep.user_id, u.email ,ep."name" , pa.phase_id, pa.activity_id, ep.phase_activity_id
                        from e_profiles ep 
                        join phase_activities pa
                        on pa.id = ep.phase_activity_id
                        join users u 
                        on u.id = ep.user_id 
                        where pa.phase_id in ('{"','".join(phaseIds)}') and pa.activity_id in ('{"','".join(pa.activity_id)}') ep.is_deleted is not true
                    '''
        return self.db.query(sql)
