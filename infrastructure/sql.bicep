param location string

param environment string


param administratorLogin string = 'sqladmin'


@secure()
param administratorPassword string


resource sqlServer 'Microsoft.Sql/servers@2022-05-01-preview' = {

name: 'azmcp-sql-${environment}-${uniqueString(resourceGroup().id)}'


  location: location


  properties: {

    administratorLogin: administratorLogin

    administratorLoginPassword: administratorPassword

  }

}


resource database 'Microsoft.Sql/servers/databases@2022-05-01-preview' = {

  parent: sqlServer

  name: 'knowledgehub'


  location: location


  sku: {

    name: 'Basic'

    tier: 'Basic'

  }

}
