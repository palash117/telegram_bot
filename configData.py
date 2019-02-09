from readCfg import read_config

#merge all into one config dictionary
class ConfigData:
    def __init__(self):
        config      = read_config(['local.properties'])

        if(config == None):
            return

        # get the current branch (from local.properties)
        env      = config.get('branch','env')

        # proceed to point everything at the 'branched' resources
        self.dbUrl       = config.get(env+'.mysql','dbUrl')
        self.dbUser      = config.get(env+'.mysql','dbUser')
        self.dbPwd       = config.get(env+'.mysql','dbPwd')
        self.dbName      = config.get(env+'.mysql','dbName')
        self.botId       = config.get(env+'.bot','id')
        self.chatId      = config.get(env+'.bot','chatId')
        print(self.botId)

        # global values

    def getBotId(self):
        return self.botId;