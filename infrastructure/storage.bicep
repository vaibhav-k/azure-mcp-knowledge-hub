param location string

param environment string


resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {

  name: 'azmcphub${environment}${uniqueString(resourceGroup().id)}'


  location: location


  sku: {

    name: 'Standard_LRS'

  }


  kind: 'StorageV2'


  properties: {

    accessTier: 'Hot'

  }

}


resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2023-01-01' = {

  parent: storageAccount

  name: 'default'

}


resource container 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {

  parent: blobService

  name: 'documents'


  properties: {

    publicAccess: 'None'

  }

}
