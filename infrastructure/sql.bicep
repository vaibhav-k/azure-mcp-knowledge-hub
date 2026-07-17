param sqlServerName string

param databaseName string = 'knowledgehub'


resource sqlServer 'Microsoft.Sql/servers@2022-05-01-preview' existing = {

  name: sqlServerName

}


resource database 'Microsoft.Sql/servers/databases@2022-05-01-preview' existing = {

  parent: sqlServer

  name: databaseName

}


output sqlServerName string = sqlServer.name

output databaseName string = database.name

output databaseId string = database.id
