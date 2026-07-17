targetScope = 'resourceGroup'


param location string = resourceGroup().location

param environment string = 'dev'


@secure()
param sqlAdminPassword string


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
    location: location
    environment: environment
    administratorPassword: sqlAdminPassword
  }

}


module keyvault './keyvault.bicep' = {

  name: 'keyvault'
  params: {
    location: location
    environment: environment
  }

}


module monitor './monitor.bicep' = {

  name: 'monitor'
  params: {
    location: location
    environment: environment
  }

}