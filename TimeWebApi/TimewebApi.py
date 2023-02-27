from requests import get


class TimewebApi:
    def __init__(self, TOKEN: str):
        self.TOKEN = TOKEN
        self.url = 'https://api.timeweb.cloud/api/v1'
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TOKEN}',
        }

        self.__check_token()
        
    def __check_token(self):
        if not get(self.url + '/auth/access', headers=self.headers):
            raise AuthError('Указан неверный API ключ')
    
    def account_status(self) -> dict:
        with get(self.url + '/account/status', headers=self.headers) as response:
            return response.json()
        
    def account_finances(self) -> dict:
        with get(self.url + '/account/finances', headers=self.headers) as response:
            return response.json()
    
    def all_databases(self) -> dict:
        with get(self.url + '/dbs', headers=self.headers) as response:
            return response.json()
    
    def database_info(self, db_id: int) -> dict:
        with get(self.url + f'/dbs/{db_id}', headers=self.headers) as response:
            return response.json()
    
    def databases_backups(self, db_id: int) -> dict:
        with get(self.url + f'/dbs/{db_id}/backups', headers=self.headers) as response:
            return response.json()
        
    def all_dedicated_servers(self) -> dict:
        with get(self.url + f'/dedicated-servers', headers=self.headers) as response:
            return response.json()
    
    def dedicated_server_info(self, dedicated_id: int) -> dict:
        with get(self.url + f'/dedicated-servers/{dedicated_id}', headers=self.headers) as response:
            return response.json()
    
    def all_cloud_servers(self) -> dict:
        with get(self.url + f'/servers', headers=self.headers) as response:
            return response.json()

    def cloud_server_info(self, server_id: int) -> dict:
        with get(self.url + f'/servers/{server_id}/statistics', headers=self.headers) as response:
            return response.json()
    
           
class AuthError(Exception):
    pass