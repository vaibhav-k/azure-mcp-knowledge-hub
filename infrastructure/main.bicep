targetScope = 'resourceGroup'


param location string = resourceGroup().location
param environment string = 'dev'

@secure()
param databaseUrl string


module storage './storage.bicep' = {

  name: 'storage'
  params: {
    location: location
    environment: environment
  }

}


module sql './sql.bicep' = {

  name: 'sql'
  params: {
    sqlServerName: 'azure-mcp-knowledgehub-sql'
    databaseName: 'knowledgehub'
  }

}


module keyvault './keyvault.bicep' = {

  name: 'keyvault'
  params: {
    location: location
  }

}


module monitor './monitor.bicep' = {

  name: 'monitor'
  params: {
    location: location
    environment: environment
  }

}


module appservice './appservice.bicep' = {

  name: 'appservice'
  params: {
    location: location
    environment: environment
    keyVaultUri: keyvault.outputs.keyVaultUri
    storageAccountName: storage.outputs.storageAccountName
  }

}


// Commented out to avoid RBAC issues
// module roles './roles.bicep' = {

//   name: 'roles'
//   params: {
//     storageAccountName: storage.outputs.storageAccountName
//     documentAppPrincipalId: appservice.outputs.documentPrincipalId
//   }

// }


module secrets './secrets.bicep' = {

  name: 'secrets'
  params: {
    keyVaultName: keyvault.outputs.keyVaultName
    databaseUrl: databaseUrl
  }

}
